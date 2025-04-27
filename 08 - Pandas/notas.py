import pandas as pd
import os

path = os.getcwd()
file = path + "/notas.csv"

df = pd.read_csv(file)

print(df)
print(df.describe())