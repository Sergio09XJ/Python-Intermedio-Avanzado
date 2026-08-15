import pandas as pd


nueva_tabla_venta = pd.read_csv("ventas.csv")


nueva_tabla_venta["ingresos"] = nueva_tabla_venta["cantidad"] * nueva_tabla_venta["precio"]

print(nueva_tabla_venta)

nueva_tabla_venta.to_csv("ventas_ingresos.csv", index=False)