import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# dataset
data = {
    "Experience": [1, 2, 3, 4],
    "Salary": [30000, 35000, 40000, 50000]
}

df = pd.DataFrame(data)

# input (X) and output (y)
X = df[["Experience"]]
y = df["Salary"]

# model
model = LinearRegression()

# training
model.fit(X, y)

# prediction
pred = model.predict([[5]])

print("Predicted salary for 5 years:", pred[0])