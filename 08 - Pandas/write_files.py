import pandas as pd
import os


df = pd.DataFrame({
    "Carnet": [123, 456, 789, 987, 654],
    "Hoja de trabajo 1": [80, 85, 75, 40, 100],
    "Hoja de trabajo 2": [90, 90, 75, 61, 100],
    "Hoja de trabajo 3": [80, 80, 0, 50, 85],
})

# print(df)

nuvas_notas = [100, 100, 100, 100, 100]

df["Hoja de trabajo 4"] = nuvas_notas

# print(df)

df = df.rename(columns={"Hoja de trabajo 1": "HT1"})

# print(df)

df = df.rename(columns={
    "Hoja de trabajo 2": "HT2",
    "Hoja de trabajo 3": "HT3"
})

# print(df)

del df["Hoja de trabajo 4"]

# print(df)

df.loc[df["Carnet"] == 123, "HT1"] = 100

print(df)

path = os.getcwd()
file = path + "/notas.csv"
print(file)

df.to_csv(file, index=False)

print("Archivo escrito extiosamente")
