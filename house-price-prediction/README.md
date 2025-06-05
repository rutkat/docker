# House Price Prediction Model Docker Deployment	
Download or clone this repo to run it locally with Docker.
###
__Tutorial Docker instructions from current directory__
<br>-Build the Docker image:
```
docker build -t house-price-prediction .
```
<br>-Run the container
```
docker run -d -p 80:80 house-price-prediction
```
###  
__Test the endpoint with curl__
```
curl -X 'POST' 'http://127.0.0.1:80/predict' -H 'Content-Type: application/json' \ -d '{ "MedInc": 3.5, "AveRooms": 5.0, "AveOccup": 2.}'
```
###
Dockerfile used for building the image
```
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
```

