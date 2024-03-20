#Se importó la clase y el metodo de el archivo operaciones
from operaciones import Operaciones

#Solicitu de variables por consola
val1 = int(input("Ingresu su primer número: "))
val2 = int(input("Ingrese su segundo número: "))

#Creación del objeto de la clase tipo "Sumas"
operadores = Operaciones(n1=val1, n2=val2)

#Llamado del metodo, donde se le pasan los valores que tomo el contructor para la
#ejecución de la suma.
total = operadores.suma()

#Impresion del resultado de la suma.
print(total)


#que es el init en una clase:
#Constructor que me permite acceder a los atributos de la Clase.

#agregar init a esta clase:
#Completado.

#que es "self"
#palabra reservada del contrucotor para referirse a un atributo de esa clase.

#como compartir rama
#commentarios