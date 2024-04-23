class MapManager():
    # Gestión del mapa
    def __init__(self):
        self.model = 'block.egg'
        # se utilizan las siguientes texturas:
        self.texture = 'block.png'
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ] #rgba
        # crea el nodo principal del mapa:
        self.land = render.attachNewNode("Land")

        # self.startNew()
        # self.addBlock((0,10, 0))


    # def startNew(self):
    #     # Crea la base para un nuevo mapa
    #     self.land = render.attachNewNode ("Land") # el nodo al cual todos los bloques de mapa están vinculados


    def getColor(self, z):
        #  Este método devuelve un color basado en la altura z del bloque
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]


    def addBlock(self, position):
        # Crea bloques de construcción y agrega al mapa en la posición especificada
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)


    def clear(self):
        # Restablece el mapa, eliminando el nodo land y llamando a startNew() para crear un nuevo nodo
        self.land.removeNode()
        self.land = render.attachNewNode("Land")
        # self.startNew()


    def loadLand(self, filename):
        # Limpia el mapa antes de cargar uno nuevo
        self.clear()

        # Abre el archivo de texto que contiene el mapa
        with open(filename) as file:
            # Itera sobre cada línea en el archivo
            for y, line in enumerate(file):
                # Divide la línea en una lista de alturas de bloques
                for x, height in enumerate(line.split()):
                    # Agrega bloques en la posición (x, y, z) según la altura especificada en la línea
                    for z in range(int(height) + 1):
                        self.addBlock((x, y, z))

    # def loadLand(self, filename):
    #     # Crea un mapa de tierra desde un archivo de texto, devuelve sus dimensiones
    #     self.clear()
    #     with open(filename) as file:
    #         y = 0
    #         for line in file:
    #             x = 0
    #             line = line.split(' ')
    #             for z in line:
    #                 for z0 in range(int(z) + 1):
    #                     block = self.addBlock((x, y, z0))
    #                 x += 1
    #             y += 1