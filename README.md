[![smithery badge](https://smithery.ai/badge/@devalexandre/mcp-servers)](https://smithery.ai/server/@devalexandre/mcp-servers)

# MCP Servers

[![smithery badge](https://smithery.ai/badge/@devalexandre/mcp-servers)](https://smithery.ai/server/@devalexandre/mcp-servers)

## Description

The **MCP Servers with Pyppeteer** is a tool that allows you to control a headless browser using [Pyppeteer](https://github.com/pyppeteer/pyppeteer), enabling automated navigation, screenshot capturing, interaction with page elements, and more. This project was developed to facilitate the creation of automation servers based on the MCP (Multi-Context Protocol) framework.

---

## Features

- **Automated Navigation:** Navigate to specific URLs.
- **Screenshot Capture:** Take screenshots of visited pages.
- **Element Interaction:** Click on page elements using CSS selectors, XPath, or class names.
- **Dynamic Resources:** Access dynamic page information, such as the current URL.
- **Server Lifecycle Management:** Controlled initialization and shutdown of the browser.

---

## Prerequisites

Make sure you have the following installed before getting started:

1. **Python 3.7+**: The project has been tested with Python 3.12, but earlier versions (3.7+) should also work.
2. **pip**: Python package manager.
3. **Git**: To clone the repository.

---

## Installation

### Installing via Smithery

To install MCP Servers for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@devalexandre/mcp-servers):

```bash
npx -y @smithery/cli install @devalexandre/mcp-servers --client claude
```

### Via Pip GitHub

1. **Install the Package:**

   ```bash
   pip install -e git+https://github.com/devalexandre/mcp-servers.git#egg=mcp-servers
   ```

### Via Git

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/devalexandre/mcp-servers.git
   cd mcp-servers

2. **Create a Virtual Environment (Optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **nstall the Package in Editable Mode:**

   ```bash
   pip install -e .
   ```
