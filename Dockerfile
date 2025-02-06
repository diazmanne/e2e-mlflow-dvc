# Use a lightweight Python 3.8 image as the base image
FROM python:3.8-slim-buster

# Update package lists and install AWS CLI (and any other OS-level dependencies)
RUN apt-get update -y && \
    apt-get install -y awscli && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container to /app
WORKDIR /app

# Copy the entire project into the container at /app
COPY . /app

# Install project dependencies from requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Define the command to run your application.
# This assumes that your Flask (or other) server is started by app.py.
CMD ["python3", "app.py"]
