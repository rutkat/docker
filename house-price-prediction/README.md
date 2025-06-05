<h2 align="left">House Price Prediction Model Docker Deployment</h2>
	
###
<div align="left">
  <p>Tutorial Docker instructions from current directory</p>
  <p>-Build the Docker image:
  <code> docker build -t house-price-prediction .</code>
  </p>
  <p>-Run the container
  <code>docker run -d -p 80:80 house-price-prediction</code>
  </p>
  <p> Test the endpoint with curl
  <code> curl -X 'POST' 'http://127.0.0.1:80/predict' -H 'Content-Type: application/json' \ -d '{ "MedInc": 3.5, "AveRooms": 5.0, "AveOccup": 2.}'</code>
  </p>
</div>
<div align="left">
<code>
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
</code>
</div>

