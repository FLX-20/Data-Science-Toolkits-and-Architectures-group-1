# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during the installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    curl \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Install TensorFlow and other Python dependencies
RUN pip3 install --no-cache-dir tensorflow==2.11.0

# Set the working directory inside the container
WORKDIR /app

# Install TensorFlow and other dependencies (add this after the WORKDIR or any system dependencies)
RUN pip install --upgrade tensorflow

# Copy the local project files to the container
COPY . /app

# Install other additional Python dependencies from the requirements file
RUN pip3 install --no-cache-dir -r requirements_new.txt

# Create a directory for saving models
RUN mkdir -p /app/saved_models

# Command to run the script (replace "main.py" with your actual Python script)
CMD ["python3", "main.py"]


