
class MapManager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors =[(0.5, 0.3, 0.0, 1),
                    (0.2, 0.2, 0.3, 1),
                    (0.5, 0.5, 0.2, 1),
                    (0.0, 0.6, 0.0, 1)]
        self.start_new()
        # self.add_block((0, 10, 0))
    
    def start_new(self):
        self.land = render.attachNewNode('Land')
    
    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.color = self.get_color(position[2])
        self.block.setTexture(loader.loadTexture(self.texture), 1)
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def load_land(self, filename):
        self.clear_node()
        with open(filename, 'r') as file:
            for y, line in enumerate(file):
                columns = map(int, line.split())
                for x, col in enumerate(columns):
                    for z in range(col + 1):
                        self.add_block((x, y, z))
                        
    def clear_node(self):
        self.land.removeNode()
        self.start_new()
        
    def get_color(self, pos_z):
        if pos_z < len(self.colors):
            return self.colors[pos_z]
        return self.colors[len(colors) - 1]
        
