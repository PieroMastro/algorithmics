import pickle
from time import sleep

class Mapmanager():
    """Gestión del mapa"""
    def __init__(self):
        self.model = 'block' # el modelo del cubo está en el archivo block.egg
        # # se utilizan las siguientes texturas:
        self.texture = 'block.png'         
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ] #rgba
        # crea el nodo principal del mapa:
        self.start_new()
        # self.add_block((0,10, 0))


    def start_new(self):
        """crea la base para un nuevo mapa"""
        self .land = render.attachNewNode ( "Land" ) # el nodo al cual todos los bloques de mapa están vinculados


    def get_color(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]


    def add_block(self, position):
        # crear bloques de construcción
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.get_color(int(position[2]))
        self.block.setColor(self.color)
        self.block.setTag("at", str(position))
        self.block.reparentTo(self.land)


    def clear_node(self):
        """restablece el mapa"""
        self.land.removeNode()
        self.start_new()


    def load_land(self, filename):
        """crea un mapa de tierra desde un archivo de texto, devuelve sus dimensiones"""
        self.clear_node()
        with open(filename) as file:
            for y, row in enumerate(file):
                row = map(int, row.split(' '))
                for x, col in enumerate(row):
                    height = col + 1
                    for z in range(height):
                        self.add_block((x, y, z))
        return x, y
    
    def find_blocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))


    def is_empty(self, pos):
        blocks = self.find_blocks(pos)
        if blocks:
            return False
        else:
            return True


    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.is_empty((x, y, z)):
            z += 1
        return (x, y, z)


    def build_block(self, pos):
        """Colocamos el bloque, considerando la gravedad:"""
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.add_block(new)

    def delete_block(self, position):
        """elimina bloques en la posición especificada""" 
        blocks = self.find_blocks(position)
        for block in blocks:
            block.removeNode()

    def delete_block_from(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z - 1
        for block in self.find_blocks(pos):
                block.removeNode()


    def save_map(self):
        blocks = self.land.getChildren()
        # acceder a un archivo ninario para preservear
        with open('map.dat', 'wb') as data:
            # guardamos la cantidad e bloques al inicio del archivo binario
            pickle.dump(len(blocks), data)
            # iterar todos los bloques de esa lista
            for block in blocks:
                # determianmos la posiciond e cada bloque
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                # preservar la posicion
                pickle.dump(pos, data)
        print('Mapa guardado!')

    def load_map(self):
        print('Cargando mapa...')
        sleep(1)
        self.clear_node()
        with open('map.dat', 'rb') as data:
            block_data = pickle.load(data)
            for i in range(block_data):
                pos = pickle.load(data)
                self.add_block(pos)
        print('Mapa Cargado!')
