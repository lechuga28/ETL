import pandas as pd

df = pd.read_parquet("dataset/extracted.parquet")

df = df.rename(columns={
    "name": "company_name",
    "paid_at": "updated_at"
})

df["id"] = df["id"].str[:24]
df["company_id"] = df["company_id"].str[:24]
df["amount"] = df["amount"].astype(float)

df["created_at"] = pd.to_datetime(df["created_at"], format="ISO8601")
df["updated_at"] = pd.to_datetime(df["updated_at"], format="ISO8601")

df.to_parquet("dataset/transformed.parquet", index=False)

print("Transformación completada")