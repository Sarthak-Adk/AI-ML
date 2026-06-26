import pandas as pd
import numpy as np

np.random.seed(42)

data = []

for _ in range(100):
    hours = np.random.randint(1, 11)       # 1–10 hours
    attendance = np.random.randint(40, 101)  # 40–100%

    # More realistic pass rule
    if hours >= 5 and attendance >= 70:
        passed = 1
    elif hours <= 3 and attendance < 65:
        passed = 0
    else:
        # uncertain cases
        passed = np.random.choice([0, 1])

    data.append([hours, attendance, passed])

df = pd.DataFrame(data, columns=[
    "hours_studied", "attendance", "passed"
])

df.to_csv("student_data.csv", index=False)

print(df.head())
print("Dataset created successfully")