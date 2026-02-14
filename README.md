# Nexus Lang - Programming Language

A dynamically-typed programming language implemented in Python with lexer, parser, and interpreter.

## Features

- 🔤 Lexical analysis
- 🌳 Abstract Syntax Tree (AST)
- 🚀 Interpreter
- 📝 REPL (Read-Eval-Print Loop)
- 🔧 Variables and functions
- ⚙️ Control flow (if/else, while)

## Syntax Example

```nexus
let x = 10;
let y = 20;

func add(a, b) {
    return a + b;
}

let result = add(x, y);
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run REPL
```bash
python repl.py
```

### Execute file
```bash
python nexus.py script.nx
```

## Project Structure

```
├── lexer.py       # Tokenization
├── parser.py      # AST generation
├── interpreter.py # Execution
├── repl.py        # Interactive shell
└── examples/      # Sample programs
```

## License

MIT
