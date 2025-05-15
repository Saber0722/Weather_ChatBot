# Use the official Rasa image
FROM rasa/rasa:3.6.21

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install any additional dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Rasa server port
EXPOSE 5005

# Run Rasa server with API enabled
CMD ["run", "--enable-api", "--cors", "*", "--debug"]
