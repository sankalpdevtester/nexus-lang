import math
from src.interpreter.interpreter import Interpreter
from src.lexer.tokenizer import Token
from src.parser.parser import Parser

class MathModule:
    def __init__(self):
        self.functions = {
            'sin': self.sin,
            'cos': self.cos,
            'tan': self.tan,
            'asin': self.asin,
            'acos': self.acos,
            'atan': self.atan,
            'sqrt': self.sqrt,
            'pow': self.pow,
            'log': self.log,
            'exp': self.exp
        }

    def sin(self, args):
        if len(args) != 1:
            raise Exception("sin function expects one argument")
        return math.sin(args[0])

    def cos(self, args):
        if len(args) != 1:
            raise Exception("cos function expects one argument")
        return math.cos(args[0])

    def tan(self, args):
        if len(args) != 1:
            raise Exception("tan function expects one argument")
        return math.tan(args[0])

    def asin(self, args):
        if len(args) != 1:
            raise Exception("asin function expects one argument")
        return math.asin(args[0])

    def acos(self, args):
        if len(args) != 1:
            raise Exception("acos function expects one argument")
        return math.acos(args[0])

    def atan(self, args):
        if len(args) != 1:
            raise Exception("atan function expects one argument")
        return math.atan(args[0])

    def sqrt(self, args):
        if len(args) != 1:
            raise Exception("sqrt function expects one argument")
        return math.sqrt(args[0])

    def pow(self, args):
        if len(args) != 2:
            raise Exception("pow function expects two arguments")
        return math.pow(args[0], args[1])

    def log(self, args):
        if len(args) != 1:
            raise Exception("log function expects one argument")
        return math.log(args[0])

    def exp(self, args):
        if len(args) != 1:
            raise Exception("exp function expects one argument")
        return math.exp(args[0])

def add_math_module(interpreter):
    math_module = MathModule()
    for func_name, func in math_module.functions.items():
        interpreter.add_builtin_function(func_name, func)

def main():
    interpreter = Interpreter()
    add_math_module(interpreter)
    while True:
        try:
            text = input('nexus> ')
        except EOFError:
            break
        if not text:
            continue
        try:
            parser = Parser(text)
            result = interpreter.interpret(parser.parse())
            print(result)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()