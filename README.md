# Agent Tool Documentation

## Overview

This project consists of an Agent that integrates various functionalities using LlamaIndex. The main features include a simple binary tree implementation and interaction with MCP (Model Context Protocol) tools such as Playwright.

## Table of Contents

- [Functions as Tools](#functions-as-tools)
- [MCP Interaction](#mcp-interaction)
- [How to Use](#how-to-use)

## Functions as Tools

### `SimpleTree` Class

This class is a basic implementation of a binary tree with the following methods:
- `insert(value)`: Inserts a new value into the tree.
- `inorder_traversal()`: Returns a list of values from the tree in inorder.

### File Operations

Two functions for file handling:
- `read_file(file_path)`: Reads content from a specified file.
- `write_file(file_path, content)`: Writes the given content to a specified file.

### Usage Example

To use the `SimpleTree`:
```python
from agent_tool import SimpleTree

tree = SimpleTree(10)
numbers = [5, 15, 3, 7, 12, 18]
for number in numbers:
    tree.insert(number)
print("Inorder Traversal of the Tree:", tree.inorder_traversal())
```

## MCP Interaction

The MCP interaction is implemented using Playwright to take a screenshot of a webpage.

### Usage Example

To use the Playwright example:
```python
from mcp_interaction import run_playwright_example

run_playwright_example('https://example.com')
```

## How to Use

1. Clone the repository.
2. Install required libraries:
   ```bash
   pip install playwright
   playwright install
   ```
3. Run the scripts as demonstrated in the usage examples.

## Conclusion

This project integrates programming constructs and external tools to create functional and interactive agents. Future improvements could include enhancing the tree structure and exploring additional MCP interactions.