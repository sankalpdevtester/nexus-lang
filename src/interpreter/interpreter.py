```python
from typing import Dict, List
from src.parser.ast import ASTNode, ProgramNode, FunctionNode, CallNode, VariableNode, LiteralNode
from src.parser.parser import Parser
from src.lexer.tokenizer import Tokenizer

class Interpreter:
    def __init__(self, ast: ASTNode):
        self.ast = ast
        self.environment: Dict[str, object] = {}

    def execute(self) -> object:
        return self._execute_node(self.ast)

    def _execute_node(self, node: ASTNode) -> object:
        if isinstance(node, ProgramNode):
            for child in node.children:
                self._execute_node(child)
        elif isinstance(node, FunctionNode):
            self.environment[node.name] = node
        elif isinstance(node, CallNode):
            func = self.environment.get(node.name)
            if func is None:
                raise RuntimeError(f"Function '{node.name}' not defined")
            args = [self._execute_node(arg) for arg in node.args]
            return self._execute_function_call(func, args)
        elif isinstance(node, VariableNode):
            return self.environment.get(node.name)
        elif isinstance(node, LiteralNode):
            return node.value
        else:
            raise RuntimeError(f"Unsupported node type: {type(node)}")

    def _execute_function_call(self, func: FunctionNode, args: List[object]) -> object:
        # Create a new scope for the function call
        scope: Dict[str, object] = {}
        for i, arg in enumerate(func.args):
            scope[arg] = args[i]
        # Execute the function body
        for node in func.body:
            self._execute_node(node)
        # Return the result of the function call
        return self.environment.get(func.name)

def interpret(source_code: str) -> object:
    tokenizer = Tokenizer(source_code)
    parser = Parser(tokenizer)
    ast = parser.parse()
    interpreter = Interpreter(ast)
    return interpreter.execute()

# Example usage:
if __name__ == "__main__":
    source_code = """
    def add(a, b) {
        return a + b;
    }
    result = add(2, 3);
    """
    result = interpret(source_code)
    print(result)
```