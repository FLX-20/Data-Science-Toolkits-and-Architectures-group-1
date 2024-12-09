FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --default-timeout=100000 tensorflow==2.18.0
RUN pip install --no-cache-dir --default-timeout=100000 -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["python", "src/main.py", "--mode", "all"]
