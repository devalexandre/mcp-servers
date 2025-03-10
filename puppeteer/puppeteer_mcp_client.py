#!/usr/bin/env python3
import asyncio
import logging
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def run():
    # Configure server parameters for STDIO connection
    server_params = StdioServerParameters(
        command="python",
        args=["simple_mcp_server.py"],
        env=None
    )
    
    # Connect to the server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            logger.info("Initializing connection...")
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            logger.info(f"Available tools: {tools}")
            
            # List available resources
            resources = await session.list_resources()
            logger.info(f"Available resources: {resources}")
            
            # Navigate to a URL
            result_navigate = await session.call_tool("pyppeteer_navigation", arguments={"url": "http://selenium.dev"})
            logger.info(f"Navigation result: {result_navigate}")
            
            try:
                # Take a screenshot
                result_screenshot = await session.call_tool("take_screenshot", arguments={"name": "selenium_dev.png"})
                logger.info(f"Screenshot result: {result_screenshot}")
                
                # Click an element (using a more specific selector)
                result_click = await session.call_tool("click_element", arguments={"selector": "a", "by": "css"})
                logger.info(f"Click result: {result_click}")
                
                # Read a resource
                content, mime_type = await session.read_resource("page://current")
                logger.info(f"Current page URL: {content} (MIME type: {mime_type})")
            except Exception as e:
                logger.error(f"Error during execution: {e}")
            
            # Stop the server
            result_exit = await session.call_tool("exit_server")
            logger.info(f"Exit result: {result_exit}")

if __name__ == "__main__":
    asyncio.run(run())