class sistema_drones:
    def __init__(self, nombre, alturaMaxima, cantidadDrones, lista_contenido):
        self.nombre = nombre
        self.alturaMaxima = alturaMaxima
        self.cantidadDrones = cantidadDrones

        # Listas que conforman el sistema de drones
        self.lista_contenido = lista_contenido
