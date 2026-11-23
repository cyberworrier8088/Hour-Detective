import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv("data/train.csv")

# Hours distribution
plt.hist(data["hours_spent"], bins=30)
plt.title("Project Development Hours")
plt.xlabel("Hours")
plt.ylabel("Number of Projects")
plt.show()

category_hours = data.groupby(
    "project_category"
)["hours_spent"].mean().sort_values()

category_hours.plot(kind="bar")

plt.title("Average houres by project category")
plt.xlabel("project category")
plt.ylabel("Average hours")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Commit vs hours
plt.scatter(
    data["num_commits"],
    data["hours_spent"]
)

plt.title("Commits vs Development Houres")
plt.xlabel("Number of commits")
plt.ylabel("Hours spent")
plt.show()