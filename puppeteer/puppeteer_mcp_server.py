#!/usr/bin/env python3
import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator, Dict
from mcp.server.fastmcp import FastMCP, Context
from mcp.types import TextContent, Tool, Resource, ResourceContents
from pyppeteer import launch

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global variable to store the browser
_browser = None

# Server lifespan function
@asynccontextmanager
async def server_lifespan(ctx: Context) -> AsyncIterator[None]:
    """Manages the MCP server lifecycle."""
    global _browser
    _browser = await launch()
    logger.info("Server started - browser launched")
    try:
        yield
    finally:
        await _browser.close()
        logger.info("Server stopped - browser closed")

# Create the MCP server
mcp = FastMCP("pyppeteer_server", lifespan=server_lifespan)

@mcp.tool()
async def pyppeteer_navigation(url: str):
    """
    Navigates to the URL specified in the parameter
    """
    global _browser
    page = await _browser.newPage()
    await page.goto(url)
    return {"status": "success", "url": url}

@mcp.tool()
async def take_screenshot(name: str):
    """
    Takes a screenshot of the current page and saves it with the specified name
    """
    global _browser
    pages = await _browser.pages()
    page = pages[-1]  # gets the current page
    await page.screenshot({'path': name})
    return {"status": "success", "file": name}

@mcp.tool()
async def click_element(selector: str, by: str = "css"):
    """
    Clicks an element on the page using the specified selector
    This selector can be css, xpath, or class_name
    """
    global _browser
    pages = await _browser.pages()
    page = pages[-1]
    
    if by == "css":
        await page.click(selector)
    elif by == "xpath":
        elements = await page.xpath(selector)
        if elements:
            await elements[0].click()
    elif by == "class_name":
        await page.evaluate(f'document.getElementsByClassName("{selector}")[0].click()')
    
    return {"status": "success", "selector": selector, "by": by}

@mcp.tool()
async def exit_server():
    """
    Stops the server
    """
    return {"status": "Server will exit"}

# Define the resource
@mcp.resource("page://current")
async def current_page() -> ResourceContents:
    """
    Returns the URL of the current page
    """
    global _browser
    pages = await _browser.pages()
    if not pages:
        return ResourceContents(content=TextContent(text="No open pages"), mime_type="text/plain")
    
    page = pages[-1]
    url = await page.evaluate('window.location.href')
    return ResourceContents(content=TextContent(text=url,body=body), mime_type="text/plain")

# Run the server
if __name__ == "__main__":
    mcp.run()