#Clase suma, implementando metodo "__init__" (Constructor)
class Sumas:
    def __init__(self,num1,num2):
        self.numero1 = num1
        self.numero2 = num2

#Metodo el cual me permite obtener la suma
def ejecucion_suma(n1, n2):
    result = n1+n2
    return result

#Solicitu de variables por consola
val1 = int(input("Ingresu su primer número: "))
val2 = int(input("Ingrese su segundo número: "))

#Creación del objeto de la clase tipo "Sumas"
mi_suma = Sumas(val1,val2)

#Llamado del metodo, donde se le pasan los valores que tomo el contructor para la
#ejecución de la suma.
total = ejecucion_suma(mi_suma.numero1,mi_suma.numero2)

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