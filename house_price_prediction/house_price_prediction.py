# Tutorial Docker instructions from current directory
#
# -Build the Docker image:
# docker build -t house-price-prediction .
#
# -Run the container
# docker run -d -p 80:80 house-price-prediction
#
# Test the endpoint with curl
# curl -X 'POST' 'http://127.0.0.1:80/predict' -H 'Content-Type: application/json' \ -d '{ "MedInc": 3.5, "AveRooms": 5.0, "AveOccup": 2.}'
#
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the California Housing dataset
data = fetch_california_housing(as_frame=True)
X = data.data
y = data.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

