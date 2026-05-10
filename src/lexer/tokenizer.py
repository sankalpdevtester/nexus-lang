```python
import enum
from typing import List, Tuple

class TokenType(enum.Enum):
    """Token types for the Nexus Programming Language"""
    KEYWORD = 1
    IDENTIFIER = 2
    INTEGER_LITERAL = 3
    FLOAT_LITERAL = 4
    STRING_LITERAL = 5
    SYMBOL = 6
    OPERATOR = 7
    EOF = 8

class Token:
    """Represents a single token in the source code"""
    def __init__(self, token_type: TokenType, value: str, line: int, column: int):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.token_type}, {self.value}, {self.line}, {self.column})"

class Tokenizer:
    """Responsible for breaking the source code into individual tokens"""
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self) -> List[Token]:
        """Tokenize the entire source code"""
        tokens = []
        while self.position < len(self.source_code):
            char = self.source_code[self.position]
            if char.isspace():
                self._consume_whitespace()
            elif char.isdigit() or char == '.':
                token = self._consume_number_literal()
                tokens.append(token)
            elif char.isalpha() or char == '_':
                token = self._consume_identifier()
                tokens.append(token)
            elif char == '"':
                token = self._consume_string_literal()
                tokens.append(token)
            elif char in '+-*/%<>!=&|':
                token = self._consume_operator()
                tokens.append(token)
            elif char in '(){}[];,':
                token = self._consume_symbol()
                tokens.append(token)
            else:
                raise SyntaxError(f"Invalid character '{char}' at line {self.line}, column {self.column}")
        tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return tokens

    def _consume_whitespace(self):
        """Consume whitespace characters"""
        while self.position < len(self.source_code) and self.source_code[self.position].isspace():
            if self.source_code[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1

    def _consume_number_literal(self) -> Token:
        """Consume a number literal (integer or float)"""
        start_position = self.position
        has_decimal = False
        while self.position < len(self.source_code) and (self.source_code[self.position].isdigit() or self.source_code[self.position] == '.'):
            if self.source_code[self.position] == '.':
                if has_decimal:
                    raise SyntaxError(f"Invalid number literal at line {self.line}, column {self.column}")
                has_decimal = True
            self.position += 1
        value = self.source_code[start_position:self.position]
        if '.' in value:
            token_type = TokenType.FLOAT_LITERAL
        else:
            token_type = TokenType.INTEGER_LITERAL
        return Token(token_type, value, self.line, self.column - len(value))

    def _consume_identifier(self) -> Token:
        """Consume an identifier (variable or keyword)"""
        start_position = self.position
        while self.position < len(self.source_code) and (self.source_code[self.position].isalpha() or self.source_code[self.position].isdigit() or self.source_code[self.position] == '_'):
            self.position += 1
        value = self.source_code[start_position:self.position]
        if value in ['if', 'else', 'while', 'for', 'func', 'return']:
            token_type = TokenType.KEYWORD
        else:
            token_type = TokenType.IDENTIFIER
        return Token(token_type, value, self.line, self.column - len(value))

    def _consume_string_literal(self) -> Token:
        """Consume a string literal"""
        start_position = self.position
        self.position += 1  # Consume the opening quote
        while self.position < len(self.source_code) and self.source_code[self.position] != '"':
            if self.source_code[self.position] == '\n':
                raise SyntaxError(f"Unterminated string literal at line {self.line}, column {self.column}")
            self.position += 1
        if self.position >= len(self.source_code):
            raise SyntaxError(f"Unterminated string literal at line {self.line}, column {self.column}")
        self.position += 1  # Consume the closing quote
        value = self.source_code[start_position + 1:self.position - 1]
        return Token(TokenType.STRING_LITERAL, value, self.line, self.column - len(value) - 2)

    def _consume_operator(self) -> Token:
        """Consume an operator"""
        start_position = self.position
        self.position += 1
        value = self.source_code[start_position:self.position]
        return Token(TokenType.OPERATOR, value, self.line, self.column - len(value))

    def _consume_symbol(self) -> Token:
        """Consume a symbol (parenthesis, bracket, etc.)"""
        start_position = self.position
        self.position += 1
        value = self.source_code[start_position:self.position]
        return Token(TokenType.SYMBOL, value, self.line, self.column - len(value))

def main():
    source_code = """
    x = 5
    y = 3.14
    print("Hello, world!")
    """
    tokenizer = Tokenizer(source_code)
    tokens = tokenizer.tokenize()
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
```