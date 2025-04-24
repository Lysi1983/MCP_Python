# server.py
from mcp.server.fastmcp import FastMCP
import os
from pathlib import Path
from typing import List

# Create an MCP server
mcp = FastMCP("Demo")





# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# File operations tools

@mcp.tool()
def list_files(directory_path: str) -> List[str]:
    """
    List all files in a given directory.
    
    Args:
        directory_path: The path to the directory to list files from
        
    Returns:
        A list of file names in the directory
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            return [f"Error: Directory '{directory_path}' does not exist"]
        if not path.is_dir():
            return [f"Error: '{directory_path}' is not a directory"]
            
        return [str(item.name) for item in path.iterdir()]
    except Exception as e:
        return [f"Error listing files: {str(e)}"]


@mcp.tool()
def create_file(file_path: str, content: str = "") -> str:
    """
    Create a new file with optional initial content.
    
    Args:
        file_path: The path where the file should be created
        content: Optional initial content for the file
        
    Returns:
        A message indicating success or failure
    """
    try:
        path = Path(file_path)
        
        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Check if file already exists
        if path.exists():
            return f"Error: File '{file_path}' already exists"
            
        # Create the file with initial content
        with open(file_path, 'w') as f:
            f.write(content)
            
        return f"Successfully created file: {file_path}"
    except Exception as e:
        return f"Error creating file: {str(e)}"


@mcp.tool()
def add_to_file(file_path: str, content: str) -> str:
    """
    Add information to an existing file.
    
    Args:
        file_path: The path to the file to append to
        content: The content to append to the file
        
    Returns:
        A message indicating success or failure
    """
    try:
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"Error: File '{file_path}' does not exist"
            
        # Append content to the file
        with open(file_path, 'a') as f:
            f.write(content)
            
        return f"Successfully added content to: {file_path}"
    except Exception as e:
        return f"Error adding to file: {str(e)}"


@mcp.tool()
def read_file(file_path: str) -> str:
    """
    Read and return the contents of a file.
    
    Args:
        file_path: The path to the file to read
        
    Returns:
        The content of the file or an error message
    """
    try:
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"Error: File '{file_path}' does not exist"
            
        # Read the file content
        with open(file_path, 'r') as f:
            content = f.read()
            
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"


@mcp.tool()
def delete_file(file_path: str) -> str:
    """
    Delete a file from the filesystem.
    
    Args:
        file_path: The path to the file to delete
        
    Returns:
        A message indicating success or failure
    """
    try:
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"Error: File '{file_path}' does not exist"
            
        # Delete the file
        os.remove(file_path)
            
        return f"Successfully deleted file: {file_path}"
    except Exception as e:
        return f"Error deleting file: {str(e)}"


@mcp.tool()
def search_in_file(file_path: str, search_term: str) -> str:
    """
    Search for a term in a file and return matching lines.
    
    Args:
        file_path: The path to the file to search in
        search_term: The term to search for
        
    Returns:
        Matching lines or an error message
    """
    try:
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"Error: File '{file_path}' does not exist"
            
        # Search in the file
        matching_lines = []
        with open(file_path, 'r') as f:
            for i, line in enumerate(f, 1):
                if search_term in line:
                    matching_lines.append(f"Line {i}: {line.strip()}")
                    
        if matching_lines:
            return "\n".join(matching_lines)
        else:
            return f"No matches found for '{search_term}' in {file_path}"
    except Exception as e:
        return f"Error searching in file: {str(e)}"


@mcp.tool()
def rename_file(old_path: str, new_path: str) -> str:
    """
    Rename or move a file.
    
    Args:
        old_path: The current path of the file
        new_path: The new path for the file
        
    Returns:
        A message indicating success or failure
    """
    try:
        old = Path(old_path)
        new = Path(new_path)
        
        # Check if source file exists
        if not old.exists():
            return f"Error: File '{old_path}' does not exist"
            
        # Check if destination already exists
        if new.exists():
            return f"Error: Destination '{new_path}' already exists"
            
        # Create parent directories if they don't exist
        new.parent.mkdir(parents=True, exist_ok=True)
        
        # Rename/move the file
        os.rename(old_path, new_path)
            
        return f"Successfully moved/renamed file from {old_path} to {new_path}"
    except Exception as e:
        return f"Error renaming file: {str(e)}"


# Run the server if this script is executed directly
if __name__ == "__main__":
    mcp.run(transport="stdio")