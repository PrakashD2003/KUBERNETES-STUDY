# Use the official lightweight Python image as the base image
FROM python:3.9-slim

# Prevent Python from writing .pyc files to disk (bytecode)
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is sent straight to the terminal (useful for logs)
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container to /app
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY requirements.txt /app/

# Copy application files into the container
COPY app.py /app/
COPY templates/ /app/templates/
COPY static/ /app/static/


# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world (Flask default)
EXPOSE 5000

# Set the command to run the application using Python
CMD ["python", "app.py"]
