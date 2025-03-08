# Use a lightweight official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set a non-root user for security
RUN useradd --create-home appuser
WORKDIR /home/appuser/app

# Copy dependencies first and install them
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project after dependencies are installed
COPY --chown=appuser:appuser . .

# Ensure execute.py has execution permissions
RUN chmod +x execute.py

# Switch to the non-root user
USER appuser

# Use an entrypoint for flexibility
ENTRYPOINT ["python", "execute.py"]