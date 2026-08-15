import pandas as pd
import numpy as np

ids = np.random.normal(500000, 1000, 30).astype(int)

ventas = pd.DataFrame({
    
    "id": ids,
    "fecha": pd.date_range(start="2026-08-01", periods=30, freq="D").strftime("%Y-%m-%d"),
    "producto": [
        "Laptop", "Mouse", "Teclado", "Monitor", "Audífonos", "Impresora", "Silla Gamers", "Escritorio",
        "Webcam", "Disco Duro", "Tablet", "Smartphone", "Cargador", "Cable HDMI", "Funda Laptop",
        "Altavoces", "Micrófono", "Router", "Memoria USB", "Tarjeta SD", "Teclado Mecánico", "Mousepad",
        "Soporte Laptop", "Powerbank", "Hub USB", "Lámpara LED", "Monitor Curvo", "Teclado Inalámbrico",
        "Audífonos Bluetooth", "Proyector"
    ],
    "categoria": [
        "Electrónica", "Accesorios", "Accesorios", "Monitores", "Audio", "Oficina", "Muebles", "Muebles",
        "Accesorios", "Almacenamiento", "Electrónica", "Electrónica", "Accesorios", "Accesorios", "Accesorios",
        "Audio", "Audio", "Redes", "Almacenamiento", "Almacenamiento", "Accesorios", "Accesorios",
        "Accesorios", "Accesorios", "Accesorios", "Oficina", "Monitores", "Accesorios",
        "Audio", "Electrónica"
    ],
    "cantidad": [1, 5, 2, 1, 3, 1, 2, 1, 4, 2, 1, 1, 6, 8, 3, 2, 1, 2, 10, 5, 2, 4, 3, 5, 4, 2, 1, 3, 2, 1],
    "precio": [
        850.00, 25.50, 45.00, 220.00, 60.00, 150.00, 180.00, 210.00, 35.00, 80.00,
        300.00, 650.00, 15.00, 10.00, 20.00, 45.00, 95.00, 55.00, 12.00, 18.00,
        75.00, 15.00, 25.00, 30.00, 22.00, 28.00, 320.00, 50.00, 85.00, 400.00
    ],
    "cliente": [
        "Ana Gómez", "Carlos Ruiz", "María López", "Juan Pérez", "Laura Torres",
        "Pedro Sánchez", "Sofia Castro", "Diego Morales", "Lucia Fernández", "Miguel Ángel",
        "Elena Vargas", "Javier Mendoza", "Carmen Ortíz", "Pablo Silva", "Natalia Reyes",
        "Andrés Ramos", "Valeria Cruz", "Gabriel Medina", "Daniela Vega", "Fernando Flores",
        "Adriana Guerrero", "Ricardo Campos", "Patricia Delgado", "Hugo Romero", "Isabel Peña",
        "Esteban Benítez", "Claudia Paredes", "Gonzalo Navarro", "Mónica Serrano", "Jorge Ibáñez"
    ]

})

print(ventas)

ventas.to_csv("ventas.csv", index = False)