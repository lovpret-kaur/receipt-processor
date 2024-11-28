# Use Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./app /app/

ENV PYTHONPATH=/app

RUN ls -l /app

# Specify the command to run the application
CMD ["python", "api.py"]
