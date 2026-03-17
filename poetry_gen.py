#!/usr/bin/env python3
"""
🎭 Code Poetry Generator
Transform code into beautiful poetry
"""

import click
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
import pygments
from pygments.lexers import get_lexer_for_filename

console = Console()


class CodeAnalyzer:
    """Analyzes code structure and semantics"""
    
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language
        self.tokens = []
        self.structure = {}
        
    def analyze(self):
        """Extract meaningful elements from code"""
        # Tokenize
        lexer = get_lexer_for_filename(self.language)
        self.tokens = list(pygments.lex(self.code, lexer))
        
        # Analyze structure
        self.structure = {
            'functions': self._extract_functions(),
            'loops': self._extract_loops(),
            'conditions': self._extract_conditions(),
            'variables': self._extract_variables(),
            'complexity': self._calculate_complexity(),
        }
        
        return self.structure
    
    def _extract_functions(self):
        """Extract function definitions"""
        # Simplified - in real version, use tree-sitter
        return [line.strip() for line in self.code.split('\n') 
                if 'def ' in line or 'function ' in line]
    
    def _extract_loops(self):
        """Extract loop constructs"""
        return [line.strip() for line in self.code.split('\n')
                if any(kw in line for kw in ['for ', 'while ', 'loop'])]
    
    def _extract_conditions(self):
        """Extract conditional statements"""
        return [line.strip() for line in self.code.split('\n')
                if 'if ' in line or 'else' in line or 'switch' in line]
    
    def _extract_variables(self):
        """Extract variable declarations"""
        return [line.strip() for line in self.code.split('\n')
                if '=' in line and not '==' in line]
    
    def _calculate_complexity(self):
        """Calculate code complexity score"""
        lines = len(self.code.split('\n'))
        return min(10, lines // 5)


class PoetEngine:
    """Generates poetry from code analysis"""
    
    def __init__(self, style: str = 'haiku', language: str = 'code'):
        self.style = style
        self.language = language
        self.metaphors = {
            'function': ['dance', 'ritual', 'transformation', 'journey'],
            'loop': ['cycle', 'spiral', 'rhythm', 'heartbeat'],
            'condition': ['crossroads', 'choice', 'fork in the path', 'decision'],
            'variable': ['vessel', 'container', 'keeper', 'memory'],
            'recursion': ['mirror', 'echo', 'reflection', 'infinite depth'],
        }
    
    def generate(self, structure: dict, code: str) -> str:
        """Generate poetry based on code structure"""
        generators = {
            'haiku': self._generate_haiku,
            'free-verse': self._generate_free_verse,
            'sonnet': self._generate_sonnet,
            'abstract': self._generate_abstract,
        }
        
        generator = generators.get(self.style, self._generate_haiku)
        return generator(structure, code)
    
    def _generate_haiku(self, structure: dict, code: str) -> str:
        """Generate a 5-7-5 haiku"""
        # Analyze essence of code
        has_loops = len(structure['loops']) > 0
        has_functions = len(structure['functions']) > 0
        has_recursion = any('recursion' in str(structure).lower() for _ in [1])
        
        if has_recursion:
            return """Patterns repeat
Like echoes in an endless hall
Truth reflects itself"""
        
        elif has_loops and has_functions:
            actions = self.metaphors['function'][0]
            cycles = self.metaphors['loop'][0]
            return f"""{actions.capitalize()} unfolds
In {cycles}s of purposeful steps
Code becomes rhythm"""
        
        elif has_functions:
            action = self.metaphors['function'][0]
            return f"""{action.capitalize()} begins
Each line a step toward meaning
Logic finds its voice"""
        
        else:
            return """Silent lines of thought
Waiting to be brought to life
Dormant potential"""
    
    def _generate_free_verse(self, structure: dict, code: str) -> str:
        """Generate free verse poetry"""
        lines = []
        
        # Opening
        if structure['functions']:
            lines.append(f"In the realm of {self.language},")
            lines.append(f"Where {structure['functions'][0].split('(')[0].replace('def ', '').replace('function ', '')} dwells,")
        
        # Middle - explore structure
        if structure['loops']:
            lines.append("")
            lines.append("Round and round,")
            lines.append("Like planets in orbit,")
            lines.append("The loops spin their tales.")
        
        if structure['conditions']:
            lines.append("")
            lines.append("At the crossroads of logic,")
            lines.append("Choices branch like rivers,")
            lines.append("Each path a different destiny.")
        
        # Closing
        lines.append("")
        lines.append("This is not merely code,")
        lines.append("But poetry written in logic's tongue,")
        lines.append("Waiting to be heard.")
        
        return '\n'.join(lines)
    
    def _generate_sonnet(self, structure: dict, code: str) -> str:
        """Generate a 14-line sonnet"""
        # Simplified sonnet structure
        return f"""Upon the screen where characters take flight,
A {self.metaphors['function'][0]} emerges from the programmer's sight.
Through {self.metaphors['loop'][0]}s that spin with grace and might,
The algorithm dances, purely code-born light.

When {self.metaphors['condition'][0]}s appear to test the flow,
The logic branches, choosing where to go.
Each {self.metaphors['variable'][0]} holds secrets the program will show,
In this digital world where patterns grow.

Fourteen lines to capture what code conveys,
The beauty hidden in syntax arrays.
Not cold computation, but art displays,
A symphony of bits in ordered ways.

So when you read this code, do see it true:
Not just instructions, but poetry for you."""
    
    def _generate_abstract(self, structure: dict, code: str) -> str:
        """Generate abstract, experimental poetry"""
        import random
        
        words = []
        for key, values in self.metaphors.items():
            words.extend(values[:2])
        
        random.shuffle(words)
        
        lines = []
        for i in range(0, len(words), 2):
            if i + 1 < len(words):
                lines.append(f"{words[i]} . {words[i+1]} . void")
            else:
                lines.append(f"{words[i]} . . .")
        
        lines.append("")
        lines.append(">>> [SYNTAX DISSOLVES]")
        lines.append(">>> [MEANING EMERGES]")
        lines.append(">>> [CODE = POETRY]")
        
        return '\n'.join(lines)


@click.command()
@click.argument('code_file', type=click.Path(exists=True))
@click.option('--style', type=click.Choice(['haiku', 'free-verse', 'sonnet', 'abstract']), 
              default='haiku', help='Poetry style')
@click.option('--output', '-o', type=click.Path(), help='Output file')
@click.option('--show-code', is_flag=True, help='Display original code')
def main(code_file: str, style: str, output: Optional[str], show_code: bool):
    """Transform code into poetry 🎭"""
    
    # Read code
    code_path = Path(code_file)
    code = code_path.read_text()
    language = code_path.suffix
    
    # Show original code if requested
    if show_code:
        console.print(Panel(
            Syntax(code, language.lstrip('.'), theme="monokai"),
            title="📜 Original Code",
            border_style="blue"
        ))
    
    # Analyze
    console.print("\n🔍 Analyzing code structure...", style="yellow")
    analyzer = CodeAnalyzer(code, language)
    structure = analyzer.analyze()
    
    # Generate poetry
    console.print(f"✍️  Generating {style} poetry...", style="yellow")
    poet = PoetEngine(style, language.lstrip('.'))
    poetry = poet.generate(structure, code)
    
    # Display result
    console.print(Panel(
        poetry,
        title=f"🎭 Generated Poetry ({style})",
        border_style="magenta"
    ))
    
    # Save to file if requested
    if output:
        output_path = Path(output)
        output_path.write_text(poetry)
        console.print(f"\n✅ Poetry saved to {output}", style="green")


if __name__ == '__main__':
    main()
