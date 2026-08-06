
from dataclasses import dataclass 
from src.utils.validatorsYutils  import verificar_nombre, verificar_iD, verificar_correo, genAleatorio

@dataclass
class Usuario: 

 __nombre : str
 __correo : str
 __iD  = genAleatorio()

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

 @nombre.setter
 def nombre(self, nuevoNombre) -> None:
    if verificar_nombre(nuevoNombre) == True: 
       self.__nombre = nuevoNombre
    else: 
       raise TypeError("El nombre no es del tipo correcto. ")

 @property
 def iD(self) -> int: 
     return self.__iD

 @iD.setter
 def iD(self, nuevoiD) -> None:
    if verificar_iD(nuevoiD) == True: 
       self.__iD = nuevoiD
    else: 
       raise TypeError("El nuevo iD o es de longitud diferente o tipo incorrecto. ")

 @property
 def correo(self) -> str: 
     return self.__correo

 @correo.setter
 def correo(self, nuevoCorreo) -> None:
    if verificar_correo(nuevoCorreo) == True: 
       self.__correo = nuevoCorreo
    else: 
       raise TypeError("El correo no tiene el formato correcto ")




