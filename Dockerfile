# Use a lightweight official Python image
FROM python:3.10-slim

# Set a non-root user for security
RUN useradd --create-home appuser
WORKDIR /home/appuser/app

# Copy only necessary files first to leverage Docker caching
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project after dependencies are installed
COPY . .

# Ensure execute.py has execution permissions
RUN chmod +x execute.py

# Change ownership to the non-root user
RUN chown -R appuser:appuser /home/appuser/app

# Switch to the non-root user
USER appuser

# Default command to run the application
CMD ["python", "execute.py"]