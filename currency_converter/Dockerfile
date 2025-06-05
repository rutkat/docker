# Get Python slim image from docker hub
FROM python:3.11-slim

# Set directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy files from current directory 
COPY . .

EXPOSE 8000

# Run the python app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
