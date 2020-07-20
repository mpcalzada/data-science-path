class Vehiculos:

    def __init__(self, tipo):
        self.tipo = tipo

    def acelerar(self):
        print(f'Estoy avanzando en un {self.tipo}')

    def frenar(self):
        print(f'Estoy deteniendome en un {self.tipo}')
