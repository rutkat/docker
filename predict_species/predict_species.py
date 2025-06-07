# Tutorial API demo to predict iris flower species based on sepal and petal measurements.
#
# -Build the Docker image:
# docker build -t predict_species .
#
# -Run the container
# docker run -p 8000:8000 predict_species
#
# Test the endpoint with curl
# curl -X 'POST' 'http://localhost:8000/predict/' -H 'Content-Type: application/json' -d '{ "sepal_length": 5.1,  "sepal_width": 3.1, "petal_length": 1.2, "petal_width": 0.4 }'
#
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from fastapi import FastAPI


app = FastAPI()

iris = load_iris()
X, y = iris.data, iris.target

# Train
model = LogisticRegression(solver='lbfgs', max_iter=300)
model.fit(X, y)

def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    return iris.target_names[prediction[0]]

# BaseModel for data validation
from pydantic import BaseModel

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# API endpoint
@app.post("/predict/")
async def predict_species_api(iris_data: IrisData):
    species = predict_species(iris_data.sepal_length, iris_data.sepal_width, iris_data.petal_length, iris_data.petal_width)
    return {"species": species}



