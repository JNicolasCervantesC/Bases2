class Operaciones:
    def __init__(self, n1: int = None, n2: int = None):
        self.n1 = n1
        self.n2 = n2

    def ejecutar(self, tipo: str):
        if tipo == "suma":
            e1 = self.suma()
        if tipo == "resta":
            e1 = self.resta()
        if tipo == "producto":
            e1 = self.producto()
        if tipo == "division":
            e1 = self.division()
        return e1

    def suma(self):

        if self.n1 != None and self.n2 != None:
            result = self.n1 + self.n2

        else:
            print("Warning")
            result = None

        return result

    def resta(self):
        if self.n1 != None and self.n2 != None:
            result = self.n1 - self.n2

        if self.n1 != None and self.n2 == None:
            result = self.n1

        if self.n1 == None and self.n2 != None:
            result = (self.n2*-1)

        if self.n1 == None and self.n2 == None:
            result = None

        return result

    def producto(self):
        if self.n1 != None and self.n2 != None:
            result = self.n1 * self.n2

        if self.n1 != None and self.n2 == None:
            result = None

        if self.n1 == None and self.n2 != None:
            result = None

        if self.n1 == None and self.n2 == None:
            result = None

        return result

    def division(self):

        if self.n2 == 0:
            result = None
            print("Warning - No puede dividir por cero.")

        else:
            result = self.n1 / self.n2

        return result



#arreglar metodos
#unit test
#new clas funciones