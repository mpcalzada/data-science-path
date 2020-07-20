from programacion_orientada_objetos.vehiculos import Vehiculos


class Jet(Vehiculos):

    def __init__(self, marca, color):
        super(Jet, self).__init__('Aereo')
        self.marca = marca
        self.color = color

    def acelerar(self):
        print(f'Estoy volando muy rapido en mi {self.marca} color {self.color}')

    def frenar(self):
        print(f'Estoy comenzando a frenar en mi {self.marca} color {self.color}')
