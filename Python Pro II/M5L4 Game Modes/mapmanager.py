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
        self.startNew()
        # self.addBlock((0,10, 0))


    def startNew(self):
        """crea la base para un nuevo mapa"""
        self .land = render.attachNewNode ( "Land" ) # el nodo al cual todos los bloques de mapa están vinculados


    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]


    def addBlock(self, position):
        # crear bloques de construcción
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)

        self.block.setTag("at", str(position))

        self.block.reparentTo(self.land)


    def clear(self):
        """restablece el mapa"""
        self.land.removeNode()
        self.startNew()


    def loadLand(self, filename):
        """crea un mapa de tierra desde un archivo de texto, devuelve sus dimensiones"""
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x,y
    
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))


    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True


    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)


    def buildBlock(self, pos):
        """Colocamos el bloque, considerando la gravedad:"""
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)


    def delBlock(self, position):
        """elimina bloques en la posición especificada""" 
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()


    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z - 1
        for block in self.findBlocks(pos):
                block.removeNode()
