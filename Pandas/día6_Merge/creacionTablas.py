import pandas as pd
import numpy as np

# 1. DATAFRAME CLIENTES (50 elementos) 
clientes = pd.DataFrame({
    "cliente_id": list(range(1, 51)),
    "nombre_id": [
        "Ana Gómez", "Carlos Ruiz", "María López", "Juan Pérez", "Laura Torres",
        "Pedro Sánchez", "Sofia Castro", "Diego Morales", "Lucia Fernández", "Miguel Ángel",
        "Elena Vargas", "Javier Mendoza", "Carmen Ortíz", "Pablo Silva", "Natalia Reyes",
        "Andrés Ramos", "Valeria Cruz", "Gabriel Medina", "Daniela Vega", "Fernando Flores",
        "Adriana Guerrero", "Ricardo Campos", "Patricia Delgado", "Hugo Romero", "Isabel Peña",
        "Esteban Benítez", "Claudia Paredes", "Gonzalo Navarro", "Mónica Serrano", "Jorge Ibáñez",
        "Alicia Bravo", "Roberto Gil", "Lorena Marín", "Santi Rivas", "Camila Molina",
        "Raúl Orozco", "Silvia Campos", "Tomas Prieto", "Rosa Merino", "Héctor Beltrán",
        "Beatriz Solís", "Felipe Parra", "Verónica Cano", "Óscar Naranjo", "Irene Cordero",
        "Rubén Pastor", "Miriam Vidal", "César Esteban", "Nuria Moya", "Víctor Luque"
    ],
    "ciudad": [
        "CDMX", "Guadalajara", "Monterrey", "Puebla", "Querétaro",
        "CDMX", "Guadalajara", "Monterrey", "Toluca", "Puebla",
        "CDMX", "Querétaro", "Guadalajara", "Monterrey", "CDMX",
        "Puebla", "Toluca", "CDMX", "Guadalajara", "Querétaro",
        "Monterrey", "CDMX", "Puebla", "Guadalajara", "Toluca",
        "CDMX", "Querétaro", "Monterrey", "CDMX", "Guadalajara",
        "Puebla", "Toluca", "CDMX", "Querétaro", "Guadalajara",
        "Monterrey", "CDMX", "Puebla", "Toluca", "CDMX",
        "Guadalajara", "Querétaro", "Monterrey", "CDMX", "Puebla",
        "Toluca", "CDMX", "Guadalajara", "Querétaro", "Monterrey"
    ]
})

# 2. DATAFRAME PRODUCTOS (50 elementos)
productos = pd.DataFrame({
    "producto_id": list(range(101, 151)),
    "producto": [
        "Laptop Pro", "Mouse Óptico", "Teclado USB", "Monitor 24", "Audífonos BT",
        "Impresora Laser", "Silla Gamer", "Escritorio Madera", "Webcam HD", "Disco Duro 1TB",
        "Tablet 10", "Smartphone 5G", "Cargador Cápido", "Cable HDMI 2m", "Funda Laptop",
        "Altavoces PC", "Micrófono USB", "Router Wi-Fi 6", "Memoria USB 64GB", "Tarjeta SD 128GB",
        "Teclado Mecánico", "Mousepad XXL", "Soporte Laptop", "Powerbank 10k", "Hub USB-C",
        "Lámpara LED", "Monitor Curvo 27", "Teclado Inalámbrico", "Audífonos Noise Canc", "Proyector Mini",
        "SSD 500GB", "Base Enfriadora", "Camara Web 4K", "Lápiz Óptico", "Adaptador Ethernet",
        "Cable DisplayPort", "Batería UPS", "Soporte Monitor", "Micrófono Lavalier", "Bolsa Antirrobo",
        "Lector Tarjetas", "Switch Ethernet", "Consola Mini", "Gafas VR", "Control Blanco",
        "Filtro Privacidad", "Pastillas Limpieza", "Organizador Cables", "Luz Anillo LED", "Capturadora Video"
    ],
    "categoria": [
        "Tecnología", "Accesorios", "Accesorios", "Monitores", "Audio",
        "Oficina", "Muebles", "Muebles", "Accesorios", "Almacenamiento",
        "Tecnología", "Tecnología", "Accesorios", "Accesorios", "Accesorios",
        "Audio", "Audio", "Redes", "Almacenamiento", "Almacenamiento",
        "Accesorios", "Accesorios", "Accesorios", "Accesorios", "Accesorios",
        "Oficina", "Monitores", "Accesorios", "Audio", "Tecnología",
        "Almacenamiento", "Accesorios", "Accesorios", "Accesorios", "Redes",
        "Accesorios", "Oficina", "Muebles", "Audio", "Accesorios",
        "Almacenamiento", "Redes", "Tecnología", "Tecnología", "Accesorios",
        "Accesorios", "Oficina", "Accesorios", "Accesorios", "Tecnología"
    ],
    "costo": [
        12000, 15, 25, 140, 35, 90, 110, 130, 20, 45,
        180, 400, 8, 5, 10, 25, 55, 30, 6, 10,
        40, 8, 12, 18, 12, 15, 200, 28, 50, 250,
        35, 15, 60, 20, 10, 6, 50, 25, 18, 22,
        8, 20, 60, 150, 35, 12, 5, 4, 15, 80
    ]
})

# 3. DATAFRAME VENTAS (50 elementos)
# Fechas generadas para el año 2026
fechas_2026 = pd.date_range(start="2026-01-01", periods=50, freq="5D").strftime("%Y-%m-%d")

ventas = pd.DataFrame({
    "venta_id": list(range(5001, 5051)),
    "cliente_id": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
        46, 47, 48, 49, 50
    ],
    "producto_id": [
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
        121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
        131, 132, 133, 134, 135, 136, 137, 138, 139, 140,
        141, 142, 143, 144, 145, 146, 147, 148, 149, 150
    ],
    "cantidad": [
        1, 5, 2, 1, 3, 1, 2, 1, 4, 2,
        1, 1, 6, 8, 3, 2, 1, 2, 10, 5,
        2, 4, 3, 5, 4, 2, 1, 3, 2, 1,
        2, 3, 1, 2, 4, 5, 1, 2, 3, 2,
        5, 2, 1, 1, 2, 3, 10, 8, 2, 1
    ],
    "precio": [
        18000, 25.5, 45.0, 220.0, 60.0, 150.0, 180.0, 210.0, 35.0, 80.0,
        300.0, 650.0, 15.0, 10.0, 20.0, 45.0, 95.0, 55.0, 12.0, 18.0,
        75.0, 15.0, 25.0, 30.0, 22.0, 28.0, 320.0, 50.0, 85.0, 400.0,
        60.0, 25.0, 95.0, 35.0, 18.0, 12.0, 80.0, 45.0, 30.0, 35.0,
        15.0, 35.0, 90.0, 230.0, 55.0, 20.0, 10.0, 8.0, 25.0, 130.0
    ],
    "fecha": fechas_2026
})

clientes.to_csv("clientes.csv", index=False)
productos.to_csv("productos.csv", index=False)
ventas.to_csv("ventas.csv", index=False)

