from forma import Forma 
    class triangulo(Forma):


    def __init__ (self,nome,base,altura):
        super().__init__(nome)

        self.base = base
        self.altura = altura

    def calculaArea(self, base, altura):
         return base * altura

    

    def __str__(self):
        return (f"{super().__str__()} com medida de base = {self.base} e altura co medida {self.altura}")
