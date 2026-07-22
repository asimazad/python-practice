import numpy as np
import pandas as pd

data=[10,12,13,15,18,20,100]

#convert to array
arr=np.array(data)
mean=np.mean(arr)
print("mean:" , mean)

#varience and std 
varience =np.var(arr)
std_dev=np.std(arr)
print("varience:",varience)
print ("std dev :",std_dev)

# Quartile
q1 = np.percentile(arr , 25)
q2 = np.percentile(arr , 50)
q3 = np.percentile(arr , 75)

iqr = q3-q1
print("Q1:", q1 , "Q2:", q2 , "Q3:", q3)
print("IQR:", iqr)

import numpy as np
import pandas as pd

# Sample dataset (student marks)
data = [55, 60, 62, 65, 70, 72, 75, 80, 200]

df = pd.DataFrame(data, columns=["Marks"])

print(df)

mean = df["Marks"].mean()
variance = df["Marks"].var()
std_dev = df["Marks"].std()

q1 = df["Marks"].quantile(0.25)
q2 = df["Marks"].quantile(0.50)
q3 = df["Marks"].quantile(0.75)

iqr = q3 - q1

print("Mean:", mean)
print("Variance:", variance)
print("Std Dev:", std_dev)
print("Q1:", q1, "Median:", q2, "Q3:", q3)
print("IQR:", iqr)

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df["Marks"] < lower_bound) | (df["Marks"] > upper_bound)]
print("Outliers:\n", outliers)

df_clean = df[(df["Marks"] >= lower_bound) & (df["Marks"] <= upper_bound)]

print("Original Std Dev:", df["Marks"].std())
print("Cleaned Std Dev:", df_clean["Marks"].std())

import matplotlib.pyplot as plt

plt.boxplot(df["Marks"])
plt.title("Marks Distribution")
plt.show()