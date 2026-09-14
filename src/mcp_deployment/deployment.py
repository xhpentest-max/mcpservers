from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Calculator", "1.0.0", "A simple calculator application", "This application performs basic arithmetic operations such as addition, subtraction, multiplication, and division.", "")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b



