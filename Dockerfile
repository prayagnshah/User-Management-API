# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

ARG port

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=application.py

# Expose $port for Flask to listen on
ENV PORT=$port

# Define the command to run the app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
