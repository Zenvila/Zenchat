# Use Python base image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]
