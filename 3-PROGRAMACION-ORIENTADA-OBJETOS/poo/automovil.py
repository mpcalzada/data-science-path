from programacion_orientada_objetos.vehiculos import Vehiculos


class Automovil(Vehiculos):

    def __init__(self, modelo, marca, color):
        super().__init__('Automovil')
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'despacio':
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(3)

        self._estado = 'movimiento'

    def frenar(self):
        self._estado = 'resposo'
        self._motor.enfriar()


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyectar_gasolina(self, cantidad):
        self.temperatura = cantidad * 80

    def enfriar(self):
        self.temperatura = self.temperatura / 2
