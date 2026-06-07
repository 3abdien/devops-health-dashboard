# Start with official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Create data directory
RUN mkdir -p data

# Tell Docker which port Flask uses
EXPOSE 5000

# Command to run when container starts
CMD ["python", "src/dashboard.py"]