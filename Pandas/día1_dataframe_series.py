import pandas as pd
import numpy as np

precios = pd.Series([1.23,32.2, 43], name="Precio")
print(f"Imprimimos los Precios: \n {precios}")

ids = np.random.normal(500000,1000, 10).astype(int)

datos_productos = {
     "id" : ids, 
     "nombre" : ["Cargador", "Cargador_QI2", "SmartPhone", "SmartTV", "Ring", "Necklace", "GPU","CPU", "Smart_Watch", "Tracker"],
     "categoria" : ["Tech", "Tech", "Tech", "Tech", "Tech","Joyeria", "Joyeria", "Tech", "Tech", "Tech"],
     "precio" : [500.00, 1200.00, 25000.00, 30000.00, 1500.00, 2000.00, 85000.00, 4500.00, 10000.00, 400.00],
     "stock" : [20, 30, 52, 5, 18, 23, 10, 12, 30, 39]
}
productos = pd.DataFrame(datos_productos)

print(f"Imprimimos los Productos: \n {productos} \n | Imprimimos el Shape:  {productos.shape}  \n | Columnas: {productos.columns} \n | Tipos: \n {productos.dtypes} \n | Primeros 3: \n {productos.head(3)} \n | Ultimos 3: \n {productos.tail(3)} \n | Precios: \n {productos["precio"]} \n | Nombre y Stock \n {productos[["nombre", "stock"]]}")

cant_product = 0
for i in range(productos.shape[0]):
  cant_product += productos.stock[i]
print(f"Cantidad de productos: {cant_product}")
print(f"Precio Máximo: {productos.precio.max()}")
print(f"Precio Minimo: {productos.precio.min()}")
print(f"Promedio Precio: {productos.precio.mean()}")
print(f"Stock Total: \n {productos.stock.sum()}")