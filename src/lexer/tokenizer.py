from enum import Enum
from typing import List, Tuple

class TokenType(Enum):
    """Token types for the Nexus Programming Language"""
    IDENTIFIER = 1
    KEYWORD = 2
    INTEGER_LITERAL = 3
    FLOAT_LITERAL = 4
    STRING_LITERAL = 5
    SYMBOL = 6
    OPERATOR = 7
    EOF = 8

class Token:
    """Represents a single token in the Nexus Programming Language"""
    def __init__(self, token_type: TokenType, value: str, line: int, column: int):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.token_type}, {self.value}, {self.line}, {self.column})"

class Tokenizer:
    """Tokenizes the input source code into a list of tokens"""
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self) -> List[Token]:
        """Tokenizes the input source code into a list of tokens"""
        tokens = []
        while self.position < len(self.source_code):
            char = self.source_code[self.position]
            if char.isspace():
                self.skip_whitespace()
            elif char.isalpha():
                token = self.tokenize_identifier()
                tokens.append(token)
            elif char.isdigit():
                token = self.tokenize_integer_literal()
                tokens.append(token)
            elif char == '"':
                token = self.tokenize_string_literal()
                tokens.append(token)
            elif char in "+-*/%<>!=&|":
                token = self.tokenize_operator()
                tokens.append(token)
            elif char in ",;(){}[]":
                token = self.tokenize_symbol()
                tokens.append(token)
            else:
                raise SyntaxError(f"Invalid character '{char}' at line {self.line}, column {self.column}")
        tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return tokens

    def skip_whitespace(self):
        """Skips whitespace characters in the source code"""
        while self.position < len(self.source_code) and self.source_code[self.position].isspace():
            if self.source_code[self.position] == "\n":
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1

    def tokenize_identifier(self) -> Token:
        """Tokenizes an identifier in the source code"""
        start_position = self.position
        while self.position < len(self.source_code) and self.source_code[self.position].isalnum():
            self.position += 1
            self.column += 1
        value = self.source_code[start_position:self.position]
        if value in ["let", "const", "fn", "if", "else", "while", "for"]:
            token_type = TokenType.KEYWORD
        else:
            token_type = TokenType.IDENTIFIER
        return Token(token_type, value, self.line, self.column - len(value))

    def tokenize_integer_literal(self) -> Token:
        """Tokenizes an integer literal in the source code"""
        start_position = self.position
        while self.position < len(self.source_code) and self.source_code[self.position].isdigit():
            self.position += 1
            self.column += 1
        value = self.source_code[start_position:self.position]
        return Token(TokenType.INTEGER_LITERAL, value, self.line, self.column - len(value))

    def tokenize_string_literal(self) -> Token:
        """Tokenizes a string literal in the source code"""
        start_position = self.position + 1
        self.position += 1
        self.column += 1
        while self.position < len(self.source_code) and self.source_code[self.position] != '"':
            if self.source_code[self.position] == "\n":
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1
        if self.position >= len(self.source_code):
            raise SyntaxError("Unterminated string literal")
        value = self.source_code[start_position:self.position]
        self.position += 1
        self.column += 1
        return Token(TokenType.STRING_LITERAL, value, self.line, self.column - len(value) - 2)

    def tokenize_operator(self) -> Token:
        """Tokenizes an operator in the source code"""
        value = self.source_code[self.position]
        self.position += 1
        self.column += 1
        return Token(TokenType.OPERATOR, value, self.line, self.column - 1)

    def tokenize_symbol(self) -> Token:
        """Tokenizes a symbol in the source code"""
        value = self.source_code[self.position]
        self.position += 1
        self.column += 1
        return Token(TokenType.SYMBOL, value, self.line, self.column - 1)

# Example usage:
if __name__ == "__main__":
    source_code = """
    let x = 5;
    const y = "hello";
    fn add(a, b) {
        return a + b;
    }
    """
    tokenizer = Tokenizer(source_code)
    tokens = tokenizer.tokenize()
    for token in tokens:
        print(token)