# MCP Server Demo

## Overview
This is a demonstration implementation of a Model Context Protocol (MCP) server. The MCP protocol facilitates communication between clients and AI models, providing a standardized way to exchange prompts, context, and model responses.

## Purpose

The purpose of this project is to demonstrate the implementation of a Model Context Protocol (MCP) server using the `FastMCP` framework. The server provides tools for file operations, such as creating, reading, deleting, and searching files, and includes a dynamic resource for personalized greetings. It serves as an example of how to use MCP for efficient communication between clients and AI models.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or uv package manager

### Setup
1. Clone this repository
2. Set up a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/macOS: `source .venv/bin/activate`
4. Install dependencies:
   ```
   pip install -e .
   ```

## Usage
Run the server with:
```
python main.py
```

The server will start listening for client connections on the default port.

## Project Structure
- `main.py`: Entry point for the MCP server application
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Dependency lock file

## API
The server implements the Model Context Protocol specification, which includes:
- Request/response format for model interactions
- Context management
- Authentication mechanisms
- Rate limiting

## Functions

The following functions are implemented in the MCP server:

- **Dynamic Greeting Resource**: `@mcp.resource("greeting://{name}")`
  - Provides a personalized greeting for the given name.

- **File Operations Tools**:
  - `list_files(directory_path: str) -> List[str]`: Lists all files in a given directory.
  - `create_file(file_path: str, content: str = "") -> str`: Creates a new file with optional initial content.
  - `add_to_file(file_path: str, content: str) -> str`: Appends content to an existing file.
  - `read_file(file_path: str) -> str`: Reads and returns the contents of a file.
  - `delete_file(file_path: str) -> str`: Deletes a file from the filesystem.
  - `search_in_file(file_path: str, search_term: str) -> str`: Searches for a term in a file and returns matching lines.
  - `rename_file(old_path: str, new_path: str) -> str`: Renames or moves a file.


Last updated: April 24, 2025
