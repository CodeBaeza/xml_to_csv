

class Catalogo:
    def __init__(self, identificador, cancion, artista, precio):
        self.identificador = identificador
        self.cancion = cancion
        self.artista = artista
        self.precio = precio

    def __str__(self):
        cadena = self.identificador + "," + self.cancion + "," + self.artista + "," + self.precio
        return cadena






