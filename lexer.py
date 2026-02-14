"""Lexer for Nexus programming language"""

import re
from enum import Enum, auto
from typing import List

class TokenType(Enum):
    # Keywords
    LET = auto()
    FUNC = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    RETURN = auto()
    
    # Literals
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUALS = auto()
    NOT_EQUALS = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    SEMICOLON = auto()
    COMMA = auto()
    
    # Special
    EOF = auto()

class Token:
    def __init__(self, type: TokenType, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, '{self.value}', {self.line}:{self.column})"

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        
        self.keywords = {
            'let': TokenType.LET,
            'func': TokenType.FUNC,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'return': TokenType.RETURN
        }
    
    def current_char(self) -> str:
        if self.pos >= len(self.source):
            return '\0'
        return self.source[self.pos]
    
    def peek_char(self) -> str:
        if self.pos + 1 >= len(self.source):
            return '\0'
        return self.source[self.pos + 1]
    
    def advance(self):
        if self.current_char() == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() in ' \t\n\r':
            self.advance()
    
    def read_number(self) -> Token:
        start_col = self.column
        num = ''
        
        while self.current_char().isdigit() or self.current_char() == '.':
            num += self.current_char()
            self.advance()
        
        return Token(TokenType.NUMBER, num, self.line, start_col)
    
    def read_string(self) -> Token:
        start_col = self.column
        string = ''
        self.advance()  # Skip opening quote
        
        while self.current_char() != '"' and self.current_char() != '\0':
            string += self.current_char()
            self.advance()
        
        if self.current_char() == '"':
            self.advance()  # Skip closing quote
        
        return Token(TokenType.STRING, string, self.line, start_col)
    
    def read_identifier(self) -> Token:
        start_col = self.column
        ident = ''
        
        while self.current_char().isalnum() or self.current_char() == '_':
            ident += self.current_char()
            self.advance()
        
        # Check if it's a keyword
        token_type = self.keywords.get(ident, TokenType.IDENTIFIER)
        
        return Token(token_type, ident, self.line, start_col)
    
    def tokenize(self) -> List[Token]:
        while self.current_char() != '\0':
            self.skip_whitespace()
            
            if self.current_char() == '\0':
                break
            
            # Numbers
            if self.current_char().isdigit():
                self.tokens.append(self.read_number())
                continue
            
            # Strings
            if self.current_char() == '"':
                self.tokens.append(self.read_string())
                continue
            
            # Identifiers and keywords
            if self.current_char().isalpha() or self.current_char() == '_':
                self.tokens.append(self.read_identifier())
                continue
            
            # Operators and delimiters
            col = self.column
            char = self.current_char()
            
            if char == '+':
                self.tokens.append(Token(TokenType.PLUS, char, self.line, col))
                self.advance()
            elif char == '-':
                self.tokens.append(Token(TokenType.MINUS, char, self.line, col))
                self.advance()
            elif char == '*':
                self.tokens.append(Token(TokenType.MULTIPLY, char, self.line, col))
                self.advance()
            elif char == '/':
                self.tokens.append(Token(TokenType.DIVIDE, char, self.line, col))
                self.advance()
            elif char == '=':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.EQUALS, '==', self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, char, self.line, col))
                    self.advance()
            elif char == '!':
                if self.peek_char() == '=':
                    self.tokens.append(Token(TokenType.NOT_EQUALS, '!=', self.line, col))
                    self.advance()
                    self.advance()
            elif char == '<':
                self.tokens.append(Token(TokenType.LESS_THAN, char, self.line, col))
                self.advance()
            elif char == '>':
                self.tokens.append(Token(TokenType.GREATER_THAN, char, self.line, col))
                self.advance()
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, char, self.line, col))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, char, self.line, col))
                self.advance()
            elif char == '{':
                self.tokens.append(Token(TokenType.LBRACE, char, self.line, col))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, char, self.line, col))
                self.advance()
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, char, self.line, col))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, char, self.line, col))
                self.advance()
            else:
                print(f"Unknown character: {char} at {self.line}:{col}")
                self.advance()
        
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
