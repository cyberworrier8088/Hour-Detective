import pandas as pd

# load dataset
data = pd.read_csv("data/train.csv")

# 1. Dataset size
print("Dataset shape: ")
print(data.shape)

# 2. First 5 projects
print("\nFirst 5 projects: ")
print(data.head())

# 3. column names
print("\nColumns: ")
print(data.columns.tolist())

# 4. Missing value
print("\nMissing value: ")
print(data.isnull().sum())

# 5. Hours information
print("\nHours statistics")
print(data["hours_spent"].describe())

# 6. Project categores
print("\nproject categores:")
print(data["project_category"].value_counts())