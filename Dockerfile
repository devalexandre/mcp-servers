# Base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Avoid Chromium download by Pyppeteer
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

# Install system dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    apt-get install -y fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf \
    libxss1 libgtk2.0-0 libnss3 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libgbm1 libasound2 && \
    apt-get install -y chromium && \
    apt-get clean

# Define the path to the installed Chromium
ENV BROWSER_EXECUTABLE_PATH=/usr/bin/chromium
ENV DOCKER_CONTAINER=true

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

# Run the server
CMD ["mcp-puppeteer"]
