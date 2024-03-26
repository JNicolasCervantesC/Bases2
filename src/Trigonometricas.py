class OperacionesT:
    def __init__(self, CO: float, H: float, CA:float):
        self.CO = CO
        self.H = H
        self.CA = CA

    def sen(self):
        result = self.CO / self.H
        return result

    def cos(self):
        result = self.CA / self.H
        return result


cae = float(input("Ingrese el Cateto Adayacente: "))
coe = float(input("Ingrese el Cateto Opuesto: "))
he = float(input("Ingrese la Hipoyenusa "))
print("\nIngrese la opcion segun sea el calculo que desea realizar: \n1) Sen\n2)Cos\n")

trig= OperacionesT(CO=coe, H=he, CA=cae)

e1: float = (float(input("Ingrese la opcion deseada(1 Sen - 2 Cos): ")))
while(e1<1 or e1>2):
    e1: float = float(input("Ingrese la opcion deseada(1 Sen - 2 Cos): "))

if e1 == 1:
    ec1 = trig.sen()
    print(ec1)
else:
    ec2 = trig.cos()
    print(ec2)



