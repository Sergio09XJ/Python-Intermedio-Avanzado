import numpy as np

ventas = np.array([[100, 200, 300],[150, 250, 350],[200, 300, 400]])

print(f"\nTabla de Ventas: ")
print(f"             Enero Febrero Marzo \n Producto_A {ventas[0:1]} \n Producto_B {ventas[1:2]} \n Producto_C {ventas[2:]}")

ventas_mas_diez_porci = ventas + ( 0.10 * ventas)

print(f"\nTabla de Ventas mas 10%: ")
print(f"\n             Enero Febrero Marzo \n Producto_A {ventas_mas_diez_porci[0:1]} \n Producto_B {ventas_mas_diez_porci[1:2]} \n Producto_C {ventas_mas_diez_porci[2:]}")

ventas_mas_cincuenta = ventas + 50

print(f"\nTabla de Ventas mas 50: ")
print(f"\n             Enero Febrero Marzo \n Producto_A {ventas_mas_cincuenta[0:1]} \n Producto_B {ventas_mas_cincuenta[1:2]} \n Producto_C {ventas_mas_cincuenta[2:]}")

impuestos = np.array([16, 20, 10])

try: 
   ventas_mas_impuestos =  ventas + (impuestos/100 * ventas) 
   print(f"\nTabla de Ventas mas impuestos: ")
   print(f"\n             Enero Febrero Marzo \n Producto_A {ventas_mas_impuestos[0:1]} \n Producto_B {ventas_mas_impuestos[1:2]} \n Producto_C {ventas_mas_impuestos[2:]}")

except ValueError as e: 
   print(f"Error Lanzado: {e}")

descuentos = np.array([16,20,10])

try: 
   ventas_menos_descuentos = ventas - (descuentos/100* ventas)
   print(f"\nTabla de Ventas menos descuentos: ")
   print(f"\n             Enero Febrero Marzo \n Producto_A {ventas_menos_descuentos[0:1]} \n Producto_B {ventas_menos_descuentos[1:2]} \n Producto_C {ventas_menos_descuentos[2:]}")
except ValueError as e: 
   print(f"Error Lanzado: {e}")
   
