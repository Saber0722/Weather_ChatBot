# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Install uv package manager globally
RUN pip install uv

# Copy project files
COPY . /app

# Install dependencies with uv
RUN uv pip install --no-cache-dir -r requirements.txt

# Expose Rasa server port
EXPOSE 5005

# Run Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
