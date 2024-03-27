class Operaciones:
    def __init__(self,
                 n1: int = None,
                 n2: int = None,
                 n3: str = 'Hola'):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def suma(self):
        result = self.n1 + self.n2
        return result

    def resta(self):
        result = self.n1 - self.n2
        return result

    def producto(self):
        result = self.n1 * self.n2
        return result

    def division(self):

        if self.n2 == 0:
            result = None
            print("Warning - No puede dividir por cero.")

        else:
            result = self.n1 / self.n2

        return result


#arreglar las operaciones con los parametros inicializados en None
#metodo 'ejeccurar', con una variablede de entrada con 4 nombres(operaciones), que retorne la operacion