import pandas as pd

df = pd.DataFrame({"Name": ["John", "Harry", "Jim", "Jack"], 
                   "Age": [20, 60, 52, 30],
                   "Salary": [10000, 20000, 30000, 40000], })

df["Average Salary"] = df["Salary"] - df["Age"]

df_sorted = df.sort_values(by="Age", ascending=True)

print(df)
