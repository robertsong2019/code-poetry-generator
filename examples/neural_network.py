import random

class SimpleNeuron:
    """A simple artificial neuron"""
    
    def __init__(self, weights_count):
        self.weights = [random.uniform(-1, 1) for _ in range(weights_count)]
        self.bias = random.uniform(-1, 1)
        self.learning_rate = 0.1
    
    def activate(self, inputs):
        """Calculate neuron output"""
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs))
        weighted_sum += self.bias
        return self._sigmoid(weighted_sum)
    
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + pow(2.71828, -x))
    
    def train(self, inputs, target):
        """Train the neuron with backpropagation"""
        output = self.activate(inputs)
        error = target - output
        
        # Update weights
        for i in range(len(self.weights)):
            gradient = error * output * (1 - output) * inputs[i]
            self.weights[i] += self.learning_rate * gradient
        
        # Update bias
        self.bias += self.learning_rate * error * output * (1 - output)
        
        return abs(error)

# Create a neuron that learns XOR
neuron = SimpleNeuron(2)

# Training data for XOR
training_data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0),
]

# Train the neuron
for epoch in range(10000):
    total_error = 0
    for inputs, target in training_data:
        error = neuron.train(inputs, target)
        total_error += error
    
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Error: {total_error:.4f}")

# Test the trained neuron
print("\nTesting trained neuron:")
for inputs, target in training_data:
    output = neuron.activate(inputs)
    print(f"Input: {inputs}, Target: {target}, Output: {output:.3f}")
