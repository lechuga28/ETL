import pandas as pd
import sqlalchemy as sa
from urllib.parse import quote_plus

#Nueva prueba GIT
# CONFIGURACIÓN CONEXIÓN
password = quote_plus("root123")

engine = sa.create_engine(
    f"postgresql://postgres:{password}@localhost:5432/charges_db"
)

# LEER DATOS TRANSFORMADOS
df = pd.read_parquet("dataset/transformed.parquet")

# LIMPIEZA DE DATOS
# Eliminar registros sin id o company_id
df = df.dropna(subset=["id", "company_id"])

# Limpiar espacios
df["company_id"] = df["company_id"].str.strip()

# Eliminar company_id vacíos
df = df[df["company_id"] != ""]

# Eliminar company_id corruptos (ej: ********)
df = df[~df["company_id"].str.contains(r"\*", na=False)]

# Convertir a numérico
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Eliminar nulos después de conversión
df = df.dropna(subset=["amount"])

# Eliminar valores fuera del rango permitido por NUMERIC(16,2)
df = df[df["amount"].abs() < 10**14]

# Redondear a 2 decimales
df["amount"] = df["amount"].round(2)

# CREAR TABLA COMPANIES
companies = (
    df[["company_id", "company_name"]]
    .dropna(subset=["company_id"])
    .drop_duplicates(subset=["company_id"], keep="first")
)

# CREAR TABLA CHARGES
charges = df.drop(columns=["company_name"])

# TRUNCAR TABLAS (modo prueba)
with engine.connect() as conn:
    conn.execute(sa.text("TRUNCATE TABLE charges CASCADE"))
    conn.execute(sa.text("TRUNCATE TABLE companies CASCADE"))
    conn.commit()

# INSERTAR DATOS
companies.to_sql("companies", engine, if_exists="append", index=False)
charges.to_sql("charges", engine, if_exists="append", index=False)

print("Carga completada correctamente")