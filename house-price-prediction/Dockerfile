# Use the Python base image 
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script file
COPY house_price_prediction.py .

# Set the command to run your Python script
CMD ["python", "house_price_prediction.py"]


