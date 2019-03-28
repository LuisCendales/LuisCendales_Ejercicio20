class Complejo:
    def __init__(self,real,imaginario):
        self.real = real
        self.imaginario = imaginario
        self.norma = (real**2)+(imaginario**2)
    def conjugado(self):
        self.imaginario = -self.imaginario
        z = complex(self.real,self.imaginario)
        return z
    def calcula_norma(self):
        return self.norma
    def pow(self,n):
        z = complex(self.real,self.imaginario)
        z = z**n
        return z