function binarySearch(arr: number[], target: number): number {
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Not found
}

// Example
const sortedArray = [1, 3, 5, 7, 9, 11, 13, 15, 17];
const index = binarySearch(sortedArray, 7);
console.log(`Found at index: ${index}`);
