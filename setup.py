from setuptools import setup, find_packages

setup(
    name="mcp-servers",  # Altere aqui para "mcp-servers"
    version="0.0.1",
    description="MCP Servers",
    author="Alexandre E Souza",
    author_email="progsphp@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pyppeteer",
        "mcp",
    ],
    entry_points={
        "console_scripts": [
            "mcp-puppeteer=pyppeteer_server.puppeteer_mcp_server:main",
        ],
    },
)
