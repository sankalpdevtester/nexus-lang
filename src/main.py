```python
import sys
import argparse
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from ast import AST

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Nexus Programming Language')
    parser.add_argument('file', help='Path to the Nexus source file')
    args = parser.parse_args()

    # Read the source code from the file
    try:
        with open(args.file, 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    # Create a lexer and tokenize the source code
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    # Create a parser and parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse()

    # Create an interpreter and execute the AST
    interpreter = Interpreter(ast)
    interpreter.execute()

def run_repl():
    # Create a lexer and parser for the REPL
    lexer = Lexer('')
    parser = Parser([])

    # Create an interpreter for the REPL
    interpreter = Interpreter(None)

    # Run the REPL loop
    while True:
        # Read a line of input from the user
        try:
            line = input('>>> ')
        except EOFError:
            break

        # Tokenize the input line
        lexer.source_code = line
        tokens = lexer.tokenize()

        # Parse the tokens into an AST
        parser.tokens = tokens
        ast = parser.parse()

        # Execute the AST
        interpreter.ast = ast
        interpreter.execute()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        run_repl()

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.pos = 0
        self.tokens = []

    def tokenize(self):
        # Tokenize the source code
        while self.pos < len(self.source_code):
            char = self.source_code[self.pos]
            if char.isspace():
                self.pos += 1
            elif char.isdigit():
                self.tokenize_number()
            elif char.isalpha():
                self.tokenize_identifier()
            else:
                self.tokenize_symbol()
        return self.tokens

    def tokenize_number(self):
        # Tokenize a number
        start = self.pos
        while self.pos < len(self.source_code) and self.source_code[self.pos].isdigit():
            self.pos += 1
        self.tokens.append(('NUMBER', self.source_code[start:self.pos]))

    def tokenize_identifier(self):
        # Tokenize an identifier
        start = self.pos
        while self.pos < len(self.source_code) and self.source_code[self.pos].isalnum():
            self.pos += 1
        self.tokens.append(('IDENTIFIER', self.source_code[start:self.pos]))

    def tokenize_symbol(self):
        # Tokenize a symbol
        char = self.source_code[self.pos]
        self.tokens.append(('SYMBOL', char))
        self.pos += 1

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = []

    def parse(self):
        # Parse the tokens into an AST
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token[0] == 'NUMBER':
                self.parse_number()
            elif token[0] == 'IDENTIFIER':
                self.parse_identifier()
            elif token[0] == 'SYMBOL':
                self.parse_symbol()
        return self.ast

    def parse_number(self):
        # Parse a number
        token = self.tokens[self.pos]
        self.ast.append(('NUMBER', token[1]))
        self.pos += 1

    def parse_identifier(self):
        # Parse an identifier
        token = self.tokens[self.pos]
        self.ast.append(('IDENTIFIER', token[1]))
        self.pos += 1

    def parse_symbol(self):
        # Parse a symbol
        token = self.tokens[self.pos]
        self.ast.append(('SYMBOL', token[1]))
        self.pos += 1

class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def execute(self):
        # Execute the AST
        for node in self.ast:
            if node[0] == 'NUMBER':
                print(node[1])
            elif node[0] == 'IDENTIFIER':
                print(node[1])
            elif node[0] == 'SYMBOL':
                print(node[1])

class AST:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

# Run the main function
if __name__ == '__main__':
    main()
```