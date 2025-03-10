# Base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if necessary)
EXPOSE 8000

# Run the server
CMD ["mcp-puppeteer"]
