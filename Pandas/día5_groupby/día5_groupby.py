
import pandas as pd
from datetime import datetime

ventas_DataFrame = pd.read_csv("ventas.csv")

#0. Imprimimos la tabla: 
print(f"\n Tabla de ventas: \n {ventas_DataFrame}")

#1. Filtramos las ventas totales por categoría
print(f"\n Ventas por categoría: \n {ventas_DataFrame.groupby("categoria")["ingresos"].sum().reset_index()}")

#2. Promedio de venta por Categoría: 
print(f"\n Promedio de venta por categoría: \n {ventas_DataFrame.groupby("categoria")["ingresos"].mean().reset_index()} ")

#3. Producto con Mayor ingreso: 
print(f"\n Producto con mayor Ingreso: \n {ventas_DataFrame.groupby("producto")["ingresos"].sum().sort_values(ascending= False).reset_index()}")

#3.5 Cantidad total por producto: 
print(f"\n Cantidad total por producto: \n {ventas_DataFrame.groupby("producto")["cantidad"].sum().sort_values(ascending= False).reset_index()}")

#4. Categoria con Mayor Ingreso: 
print(f"\n Categoría con mayor Ingreso: \n {ventas_DataFrame.groupby("categoria")["ingresos"].sum().sort_values(ascending= False).reset_index()}")

#5. Transformamos la fecha a datetime y mostramos las fechas por mes: 
ventas_DataFrame["fecha"] = pd.to_datetime(ventas_DataFrame["fecha"])

ventasMes = ventas_DataFrame.groupby(ventas_DataFrame["fecha"].dt.month_name(locale="es_ES"))["ingresos"].sum().reset_index()

print(f"\n Ventas por mes usando solo groupby: \n {ventasMes}")

#6. Obtenemos las ventas por categoria, producto y fecha

print(f"\n Ventas por fecha, promedio, suma y conteo \n {
    ventas_DataFrame.groupby(
        ventas_DataFrame["fecha"].dt.month_name(locale="es_ES"))["ingresos"].agg(
            ["mean","sum", "count"]).rename(
                columns={
                    "mean" : "Promedio_ingresos",
                    "sum" : "Suma_ingresos",
                    "count" : "Conteo_ingresos"

                }).reset_index()}")


ventas_DataFrame.groupby(
        ventas_DataFrame["fecha"].dt.month_name(locale="es_ES"))["ingresos"].agg(
            ["mean","sum", "count"]).rename(
                columns={
                    "mean" : "Promedio_ingresos",
                    "sum" : "Suma_ingresos",
                    "count" : "Conteo_ingresos"

                }).reset_index().to_csv("ventas_mes.csv", index=False)
