import pandas 

pandas.read_csv("hash-rate.csv")

files = []

import os 

for _,_, file in os.walk("."):

  for file_name in file:

    if file_name.endswith("csv"):

      files.append(file_name)

files

dataframe = None

for file in files:

  if dataframe is None:

    dataframe = pandas.read_csv(f"{file}", 
                                names = ["time", 
                                         file.replace(".csv", "")])
    
  else: 

    temporary_dataframe = pandas.read_csv(f"{file}", 
                                          names = ["time",
                                                   file.replace(".csv", "")])

    dataframe = pandas.merge(dataframe, temporary_dataframe)
    
dataframe

dataframe = dataframe[1:]

dataframe

dataframe.info()

dataframe["time"] = pandas.to_datetime(dataframe["time"],
                    format="%Y-%m-%d %H:%M:%S")

dataframe.info()

dataframe = dataframe.apply(pandas.to_numeric,
                            errors="coerce")

dataframe.info()

dataframe

columns = list(dataframe.columns)

columns

columns.remove("time")

columns

import matplotlib.pyplot as pyplot 

fig = pyplot.figure(figsize=(35, 20))

COLUMNS = 2

ROWS = 4

for index in range(len(columns)):

  fig.add_subplot(ROWS, COLUMNS, index + 1)

  current_feature = columns[index]

  pyplot.plot(dataframe["time"],
              dataframe[current_feature])
  
pyplot.show()

NUMBER_OF_TRANSACTIONS_INDEX = 8

END_RANGE = NUMBER_OF_TRANSACTIONS_INDEX + 1

X = dataframe.iloc[:, NUMBER_OF_TRANSACTIONS_INDEX:END_RANGE]

X

MARKET_PRICE_INDEX = 7

y = dataframe.iloc[:, MARKET_PRICE_INDEX]

y

X = X.values

X

y = y.values

y

X.size

y.size

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

pyplot.figure(figsize=(10, 10))

pyplot.scatter(X, y)

pyplot.ylabel("Bitcoin Price")

pyplot.xlabel("Feature: Number of Transactions")

pyplot.plot(X, model.predict(X), color = "orange")

from sklearn.preprocessing import PolynomialFeatures

X_DEGREE = 2 

polynomial_features = PolynomialFeatures(degree = X_DEGREE)

X_polynomial = polynomial_features.fit_transform(X)

polynomial_features.fit(X_polynomial, y)

linear_model = LinearRegression()

linear_model.fit(X_polynomial, y)

pyplot.scatter(X, y)

pyplot.plot(X, 
            linear_model.predict(polynomial_features.fit_transform(X)),
            color = "orange")

from sklearn.preprocessing import PolynomialFeatures

X_DEGREE = 4

polynomial_features = PolynomialFeatures(degree = X_DEGREE)

X_polynomial = polynomial_features.fit_transform(X)

polynomial_features.fit(X_polynomial, y)

linear_model = LinearRegression()

linear_model.fit(X_polynomial, y)

pyplot.figure(figsize=(10, 10))

pyplot.scatter(X, y)

pyplot.plot(X, 
            linear_model.predict(polynomial_features.fit_transform(X)),
            color = "orange")