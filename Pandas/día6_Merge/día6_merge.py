import pandas as pd

DataFrame_clientes = pd.read_csv("clientes.csv")
DataFrame_productos=pd.read_csv("productos.csv")
DataFrame_ventas=pd.read_csv("ventas.csv")

DataFrame_ventas["ingreso"] = DataFrame_ventas["cantidad"] * DataFrame_ventas["precio"]

UniónVentas_Productos = pd.merge(DataFrame_ventas, DataFrame_productos, on= "producto_id", how="left")


UniónDataSets = pd.merge(UniónVentas_Productos, DataFrame_clientes, on="cliente_id", how="left")


GananciasPorCiudad = UniónDataSets.groupby("ciudad")["ingreso"].sum().sort_values(ascending= False).reset_index()
print(f"\n Ciudad con mas ingresos:  \n {GananciasPorCiudad}")

GananciasPorCategoria = UniónDataSets.groupby("categoria")["ingreso"].sum().sort_values(ascending= False).reset_index()
print(f"\n Categoria con mas ingresos:  \n {GananciasPorCategoria}")

GananciasPorCiudad.to_csv("GanaciasPorCiudad.csv", index=False)
GananciasPorCategoria.to_csv("GananciasPorCategoria.csv", index=False)