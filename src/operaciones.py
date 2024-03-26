class Operaciones:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        result = self.n1 + self.n2
        return result

    def resta(self):
        result = self.n1 - self.n2
        return result

    def producto(self):
        result = self.n1 * self.n2
        return result

    def cociente(self):
        result = self.n1 / self.n2
        return result