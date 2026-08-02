
from dataclasses import dataclass 
from src.utils  import verificar_nombre, verificar_iD, verificar_correo, genAleatorio

class Usuario: 

 __nombre : str
 __iD : int
 __correo : str

 def __post_init__(self):
    if verificar_nombre(self.__nombre) == False: 
       raise TypeError("El nombre no es del tipo correcto. ")
    if verificar_iD(self.__iD) == False: 
       raise TypeError("El nuevo iD o es de longitud diferente o tipo incorrecto. ")
    if verificar_correo(self._correo) == True: 
           raise TypeError("El correo no tiene el formato correcto ")
    return True
 
          
    

 @property
 def nombre(self) -> str: 
    return self.__nombre

 @property
 def iD(self) -> int: 
     return self.iD

 @property
 def correo(self) -> str: 
     return self.__correo

 @nombre.setter
 def nombre(self, nuevoNombre):
    if verificar_nombre(nuevoNombre) == True: 
       self.__nombre = nuevoNombre
    else: 
       raise TypeError("El nombre no es del tipo correcto. ")

 @iD.setter
 def iD(self, nuevoiD):
    if verificar_iD(nuevoiD) == True: 
       self.__nombre = nuevoiD
    else: 
       raise TypeError("El nuevo iD o es de longitud diferente o tipo incorrecto. ")

 @iD.correo
 def correo(self, nuevocorreo):
    if verificar_correo(nuevocorreo) == True: 
       self.__nombre = nuevocorreo
    else: 
       raise TypeError("El correo no tiene el formato correcto ")

    