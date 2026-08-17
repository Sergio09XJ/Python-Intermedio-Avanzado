import pandas as pd
import numpy as np

Ventas_Raw = pd.read_csv("Ventas_raw.csv")
print(f"\nImprimimos las dimensiones antes de limpiar: \n{Ventas_Raw.shape}")

# 1. Limpieza: 
Ventas = Ventas_Raw.copy()

# 1.1 Usamos info para saber en donde hay valores de tipo null
#print(f"\n Información de datos nulos: \n {Ventas_Raw.info()}")

#1.2 Limpiamos los valores na de fecha: 

Ventas["fecha"] = Ventas["fecha"].fillna("2026-01-01") 
Ventas["fecha"] = pd.to_datetime(Ventas["fecha"], format="mixed") #Una vez limpios convertimos los valores a limpios
#print(f"\n Información de datos nulos:: \n {Ventas.info()}")

#1.3 Limpiamos los valores na de cliente: 
Ventas["cliente"] = Ventas["cliente"].fillna("Sin Cliente")
#print(f"\n Información de datos nulos:: \n {Ventas.info()}")

#1.4 Limpiamos los valores na de ciudad: 
Ventas["ciudad"] = Ventas["ciudad"].fillna("Sin Ciudad")
#print(f"\n Información de datos nulos:: \n {Ventas.info()}")


#1.5 Limpiamos los valores na de categoria: 
Ventas["categoria"] = Ventas["categoria"].fillna("Sin Categoria")
#print(f"\n Información de datos nulos:: \n {Ventas.info()}")


#1.6 Limpiamos los valores na de cantidad: 
Ventas["cantidad"] = Ventas["cantidad"].fillna(-999)
#print(f"\n Información de datos nulos:: \n {Ventas.info()}")


#1.7 Limpiamos los valores na de precio: 
Ventas["precio"] = Ventas["precio"].fillna(-999)
print(f"\n Información de datos nulos:: \n {Ventas.info()}")


#1.8 Corregimos tipos | Fecha ya fue corregida. 

Ventas["venta_id"] = pd.to_numeric(Ventas["venta_id"])
Ventas["cantidad"] = pd.to_numeric(Ventas["cantidad"])

#1.9 Corregimos erores númericos y de tipografía

Ventas["precio"] = Ventas["precio"].replace(-999, np.nan)
Ventas["cantidad"] = Ventas["cantidad"].replace(-999, np.nan)

media_precio = Ventas["precio"].median()
media_cantidad = Ventas["cantidad"].median()

Ventas["precio"] = Ventas["precio"].fillna(media_precio)
Ventas["cantidad"] = Ventas["cantidad"].fillna(media_cantidad)

#1.10 Eliminamos Duplicados 
Ventas["categoria"] =  (Ventas["categoria"].str.strip().str.lowe().replace({"técnología" : "tecnología"}).str.capitalize())

Ventas = Ventas.drop_duplicates(subset=["venta_id"],keep="first")
print(f"\nImprimimos las dimensiones después de limpiar: \n{Ventas.shape}")

# 2. Creación de Métricas: 

#2.1 Creamos ingreso
Ventas["ingreso"] = Ventas["cantidad"] * Ventas["precio"]

Ventas["mes"] = Ventas["fecha"].dt.year
Ventas["año"] = Ventas["fecha"].dt.month_name(locale="es_ES")

print(f"Año de ventas: \n {Ventas["año"]}")
print(f"Mes de ventas: \n {Ventas["mes"]}")



print(f"\n {Ventas["ingreso"].sort_values(ascending=False).idxmax()}")
print(f"\n {Ventas.groupby("categoria")["ingreso"].mean().sort_values(ascending=False)}")
print(f"\n {Ventas.groupby("mes")["ingreso"].sum()}")
print(f"\n {Ventas.groupby("categoria")["ingreso"].sum()}")
print(f"\n {Ventas.groupby("producto")["ingreso"].sum()}")
print(f"\n {Ventas.groupby("ciudad")["ingreso"].sum()}")
print(f"\n {Ventas["producto"]}")
print(f"\n {Ventas.groupby("producto")["ingreso"].sum().sort_values(ascending=False)}")
print(f"\n {Ventas.groupby("categoria")["ingreso"].sum().sort_values(ascending=False)}")

reporte_Ventas = pd.DataFrame({})

reporte_Ventas["mes"] = Ventas["año"]
reporte_Ventas["categoria"] = Ventas["categoria"]
reporte_Ventas["ingresos"] = Ventas["ingreso"]
reporte_Ventas["unidades_vendidas"] = Ventas["cantidad"]

print(f"\n Imprimimos el reporte de ventas: \n {reporte_Ventas}")
Ventas.to_csv("Ventas_Limpias.csv", index=False)
reporte_Ventas.to_csv("Reporte_Ventas.csv", index=False)