
# Clase para gestionar el mapa

class MapManager:
    def __init__(self):
        # Inicialización de la clase MapManager
        self.model = 'block'
        self.texture = 'block.png'
        self.color = (0.0, 0.6, 0.0, 1)
        # crea el nodo principal del mapa
        self.startNew()
        # crear bloques de construcción 
        self.addBlock((0, 10, 0))

    def startNew(self):
        # Crear una nueva base para el mapa
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        # Agregar un bloque al mapa en la posición dada
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

# class MapManager():
#     def __init__(self, model= 'block', texture= 'block.png', color= (0.2, 0.2, 0.35, 1)):
#         # Inicialización de la clase MapManager
#         self.model = model
#         self.texture = texture
#         self.color = color
#         self.start_new()
#         self.add_block((0, 10, 0))

#     def start_new(self):
#         # Crear una nueva base para el mapa
#         self.land = render.attachNewNode('land')

#     def add_block(self, position):
#         # Agregar un bloque al mapa en la posición dada
#         block = loader.loadModel(self.model)
#         block.setTexture(loader.loadTexture(self.texture))
#         block.setColor(self.color)
#         block.setPos(position)
#         block.reparentTo(self.land)

