# Use an official Python runtime as a parent image
FROM python:3.8

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm


# Copy the current directory contents into the container at /app
COPY . .

WORKDIR /client

# Install any needed packages specified in package.json
RUN npm install

# Build the React application
RUN npm run build

WORKDIR /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory back to /app
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World


# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]