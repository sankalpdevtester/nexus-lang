```python
from typing import Dict, List
from src.parser.parser import ASTNode
from src.lexer.tokenizer import Token

class RuntimeEnvironment:
    def __init__(self):
        self.variables: Dict[str, object] = {}
        self.functions: Dict[str, callable] = {}

    def get_variable(self, name: str):
        return self.variables.get(name)

    def set_variable(self, name: str, value: object):
        self.variables[name] = value

    def get_function(self, name: str):
        return self.functions.get(name)

    def set_function(self, name: str, func: callable):
        self.functions[name] = func

class Interpreter:
    def __init__(self, ast: ASTNode):
        self.ast = ast
        self.runtime_env = RuntimeEnvironment()

    def execute(self):
        self._execute_node(self.ast)

    def _execute_node(self, node: ASTNode):
        if node.type == 'Program':
            for child in node.children:
                self._execute_node(child)
        elif node.type == 'VariableDeclaration':
            self._execute_variable_declaration(node)
        elif node.type == 'FunctionDeclaration':
            self._execute_function_declaration(node)
        elif node.type == 'FunctionCall':
            self._execute_function_call(node)
        elif node.type == 'Expression':
            self._execute_expression(node)

    def _execute_variable_declaration(self, node: ASTNode):
        name = node.children[0].value
        value = self._evaluate_expression(node.children[1])
        self.runtime_env.set_variable(name, value)

    def _execute_function_declaration(self, node: ASTNode):
        name = node.children[0].value
        params = [child.value for child in node.children[1].children]
        body = node.children[2]
        func = lambda *args: self._execute_function_body(body, params, args)
        self.runtime_env.set_function(name, func)

    def _execute_function_call(self, node: ASTNode):
        name = node.children[0].value
        args = [self._evaluate_expression(arg) for arg in node.children[1].children]
        func = self.runtime_env.get_function(name)
        if func:
            return func(*args)
        else:
            raise Exception(f"Function '{name}' not found")

    def _execute_function_body(self, node: ASTNode, params: List[str], args: List[object]):
        for param, arg in zip(params, args):
            self.runtime_env.set_variable(param, arg)
        return self._execute_node(node)

    def _evaluate_expression(self, node: ASTNode):
        if node.type == 'Literal':
            return node.value
        elif node.type == 'BinaryExpression':
            left = self._evaluate_expression(node.children[0])
            right = self._evaluate_expression(node.children[1])
            if node.children[1].type == 'Token' and node.children[1].value == '+':
                return left + right
            elif node.children[1].type == 'Token' and node.children[1].value == '-':
                return left - right
            elif node.children[1].type == 'Token' and node.children[1].value == '*':
                return left * right
            elif node.children[1].type == 'Token' and node.children[1].value == '/':
                return left / right
        elif node.type == 'VariableReference':
            return self.runtime_env.get_variable(node.value)

def main():
    # Example usage:
    # Create an AST node for a simple program
    ast = ASTNode('Program', [
        ASTNode('VariableDeclaration', [
            ASTNode('Token', 'x'),
            ASTNode('Literal', 5)
        ]),
        ASTNode('Expression', [
            ASTNode('VariableReference', 'x'),
            ASTNode('Token', '+'),
            ASTNode('Literal', 3)
        ])
    ])

    # Create an interpreter and execute the AST
    interpreter = Interpreter(ast)
    interpreter.execute()

    # Print the result
    print(interpreter.runtime_env.get_variable('x'))  # Output: 5

if __name__ == '__main__':
    main()
```