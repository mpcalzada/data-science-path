class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2

        return (x_diff + y_diff) ** 2


if __name__ == '__main__':
    coord_1 = Coordenadas(3, 30)
    coord_2 = Coordenadas(4, 8)
    print(coord_1.distancia(coord_2))
    print(isinstance(coord_1, Coordenadas))
