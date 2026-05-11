```python
from typing import List, Optional
from src.lexer.tokenizer import Token, TokenType

class ASTNode:
    """Base class for all AST nodes."""
    pass

class BinaryOpNode(ASTNode):
    """Represents a binary operation node."""
    def __init__(self, op: Token, left: ASTNode, right: ASTNode):
        self.op = op
        self.left = left
        self.right = right

class UnaryOpNode(ASTNode):
    """Represents a unary operation node."""
    def __init__(self, op: Token, expr: ASTNode):
        self.op = op
        self.expr = expr

class LiteralNode(ASTNode):
    """Represents a literal value node."""
    def __init__(self, token: Token):
        self.token = token

class Parser:
    """Parses a list of tokens into an AST."""
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def parse(self) -> ASTNode:
        """Parses the tokens into an AST."""
        return self.parse_expr()

    def parse_expr(self) -> ASTNode:
        """Parses an expression."""
        node = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in (TokenType.PLUS, TokenType.MINUS):
            token = self.tokens[self.pos]
            self.pos += 1
            node = BinaryOpNode(token, node, self.parse_term())
        return node

    def parse_term(self) -> ASTNode:
        """Parses a term."""
        node = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in (TokenType.MUL, TokenType.DIV):
            token = self.tokens[self.pos]
            self.pos += 1
            node = BinaryOpNode(token, node, self.parse_factor())
        return node

    def parse_factor(self) -> ASTNode:
        """Parses a factor."""
        token = self.tokens[self.pos]
        if token.type == TokenType.NUMBER:
            self.pos += 1
            return LiteralNode(token)
        elif token.type == TokenType.MINUS:
            self.pos += 1
            return UnaryOpNode(token, self.parse_factor())
        elif token.type == TokenType.LPAREN:
            self.pos += 1
            node = self.parse_expr()
            self.pos += 1  # Consume the RPAREN
            return node
        else:
            raise SyntaxError(f"Unexpected token {token}")

    def error(self, message: str) -> None:
        """Raises a syntax error."""
        raise SyntaxError(message)

def main() -> None:
    # Example usage:
    tokens = [
        Token(TokenType.NUMBER, "2"),
        Token(TokenType.PLUS, "+"),
        Token(TokenType.NUMBER, "3"),
        Token(TokenType.MUL, "*"),
        Token(TokenType.NUMBER, "4")
    ]
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast.__dict__)

if __name__ == "__main__":
    main()
```