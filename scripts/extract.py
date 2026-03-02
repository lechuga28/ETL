import pandas as pd

df = pd.read_csv(r"C:\Users\Lechuga\Documents\ETL\dataset\data_prueba_técnica.csv", sep=",")

# Limpiar filas vacías
df = df.dropna(subset=["id"])
df["id"] = df["id"].str.strip()
df = df[df["id"] != ""]

df.to_parquet("dataset/extracted.parquet", index=False)

print("Extracción completada")