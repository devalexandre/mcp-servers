from setuptools import setup, find_packages

setup(
    name="mcp-servers",  # Altere aqui para "mcp-servers"
    version="0.0.1",
    description="MCP Servers",
    author="Alexandre E Souza",
    author_email="progsphp@gmail.com",
    packages=find_packages(),
    install_requires=[
        "puppeteer",
    ],
    entry_points={
        "console_scripts": [
            "mcp-puppeteer=puppeteer.puppeteer_mcp_server:main",
        ],
    },
)
