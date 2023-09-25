class sistema_drones:
    def __init__(self, nombre, alturaMaxima, cantidadDrones, lista_drones, lista_alturas):
        self.nombre = nombre
        self.alturaMaxima = alturaMaxima
        self.cantidadDrones = cantidadDrones

        # Listas que conforman el sistema de drones
        self.lista_drones = lista_drones
        self.lista_alturas = lista_alturas
