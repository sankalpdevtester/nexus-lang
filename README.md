# Nexus Programming Language
[![Build Status](https://travis-ci.org/nexus-lang/nexus.svg?branch=main)](https://travis-ci.org/nexus-lang/nexus)
[![Code Coverage](https://codecov.io/gh/nexus-lang/nexus/branch/main/graph/badge.svg)](https://codecov.io/gh/nexus-lang/nexus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Description
Nexus is a modern interpreted programming language built from scratch with its own lexer, parser, Abstract Syntax Tree (AST), and runtime. It is designed to be efficient, flexible, and easy to use, with a focus on simplicity and readability.

## Features
* **Type Inference**: Nexus features a powerful type inference system, allowing developers to write type-safe code without explicit type annotations.
* **First-Class Functions**: Functions are first-class citizens in Nexus, enabling functional programming paradigms and higher-order functions.
* **Standard Library**: A comprehensive standard library provides a wide range of functions and data structures for common tasks, including file I/O, networking, and data processing.
* **Dynamic Typing**: Nexus is dynamically typed, allowing for flexibility and ease of use, while still maintaining type safety through its inference system.
* **Modular Design**: The Nexus language is designed to be modular, with a clear separation of concerns between the lexer, parser, AST, and runtime.

## Installation
To install Nexus, follow these steps:
1. Clone the repository: `git clone https://github.com/nexus-lang/nexus.git`
2. Change into the repository directory: `cd nexus`
3. Install dependencies: `pip install -r requirements.txt`
4. Build the Nexus interpreter: `python setup.py build`
5. Install the Nexus interpreter: `python setup.py install`

## Usage
To run the Nexus interpreter, simply execute the `nexus` command in your terminal:
```bash
nexus
```
This will start the Nexus REPL, where you can write and execute Nexus code.

## Architecture Overview
The Nexus language is built from the following components:
* **Lexer**: Responsible for tokenizing the source code into a stream of tokens.
* **Parser**: Parses the token stream into an Abstract Syntax Tree (AST) representation of the code.
* **AST**: Represents the source code as a tree-like data structure, enabling efficient analysis and execution.
* **Runtime**: Executes the AST, providing the necessary functionality for the language, including type inference, function calls, and variable management.

## Contributing
We welcome contributions to the Nexus language! If you're interested in contributing, please:
1. Fork the repository: `git fork https://github.com/nexus-lang/nexus.git`
2. Create a new branch: `git branch my-feature`
3. Make your changes and commit them: `git commit -m "My feature"`
4. Open a pull request: `git pull-request`

## License
Nexus is licensed under the Apache 2.0 license. See [LICENSE](LICENSE) for details.