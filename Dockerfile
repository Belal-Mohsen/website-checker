# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster AS builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the files needed for pip install
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Setup runtime environment
FROM python:3.10-slim-buster
WORKDIR /usr/src/app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the rest of the application
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# # Use an unprivileged user
# RUN useradd -m myuser
# USER myuser

# Define environment variable
ENV NAME World

# Run app.py when the container launches
ENTRYPOINT ["python", "check_sites/main.py"]
CMD []
