import pandas as pd

file = pd.read_csv("bs.csv")
data = file.loc[file["fecha"] == "14/12/2023"] 
print(data.drop(columns=["fecha"]))

