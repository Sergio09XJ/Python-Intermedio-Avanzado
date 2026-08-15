import pandas as pd
import numpy as np

DataFrame_ventas = pd.read_csv("ventas.csv")

#Ventas con precios mayores a mil
print(f"\nPrecios mayores a 1000: \n {DataFrame_ventas["precio"] > 1000}")


#Productos de la categoría Electrónica(Tecnología)

print(f"\nVentas del la categría Electrónica: \n {DataFrame_ventas[DataFrame_ventas["categoria"].isin(["Electrónica"])]}")

#Productos con stock mayor a 5 
print(f"\nProductos de venta mayor a 5: \n {DataFrame_ventas[DataFrame_ventas["cantidad"] > 5]}")

#Ventas entre 2026-08-06 y 2026-08-26

DataFrame_ventas["fecha"] = pd.to_datetime(DataFrame_ventas["fecha"]) #Convertimos las fechas a tipo Datetime
print(f"\n Ventas en un intervalo de fecha: \n {DataFrame_ventas[DataFrame_ventas["fecha"].between("2026-08-06", "2026-08-26")]}")

#Ventas que cumplen ser de la categoría Electrónica, con stock mayor a 5 y preció mayor a 500

print(f"\n Ventas con varias condiciones: \n {DataFrame_ventas[(DataFrame_ventas["categoria"] == "Electrónica") & (DataFrame_ventas["cantidad"] > 5) & (DataFrame_ventas["precio"] > 500) ]}")

#Creación de la nueva tabla: 
DataFrame_ventas.insert(5, "Ingreso", (DataFrame_ventas["cantidad"] * DataFrame_ventas["precio"]))

print(f"\n Tabla  con ingreso: \n {DataFrame_ventas}")

Data_Frame_extraida = DataFrame_ventas.iloc[:,np.r_[0:3,4:6]] #Usamos numpy ara un intervalo de Columnas

print(f"\n Tabla nueva: \n {Data_Frame_extraida}")

#Lo pasamos a CSV
Data_Frame_extraida.to_csv("TablaConIngresosFiltrada.csv", index=False)