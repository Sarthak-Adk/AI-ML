import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of students
n = 100

# Generate CGPA (2.0 to 4.0)
cgpa = np.round(np.random.uniform(2.0, 4.0, n), 2)

# Generate IQ (80 to 160)
iq = np.random.randint(80, 161, n)

# Placement logic
placement = []

for i in range(n):
    if cgpa[i] > 3.0 and iq[i] > 110:
        placement.append(1)
    else:
        placement.append(0)

# Create DataFrame
df = pd.DataFrame({
    "CGPA": cgpa,
    "IQ": iq,
    "Placement": placement
})

# Save to CSV
df.to_csv("student_data.csv", index=False)

print(df.head(10))