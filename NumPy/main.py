import numpy as np


marks = np.array([78, 85, 67, 90, 45])


total = np.sum(marks)


average = np.mean(marks)


highest = np.max(marks)
lowest = np.min(marks)


if np.all(marks >= 40):
    status = "Pass"
else:
    status = "Fail"


if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"



print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Status:", status)
print("Grade:", grade)