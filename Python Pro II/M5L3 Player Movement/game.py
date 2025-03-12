from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.land = MapManager()
        self.land.load_land('land.txt')
        self.hero = Hero((1, 5, 1 ), self.land)
        # x, y = self.land.load_land("land.txt")
        # self.hero = Hero((x//2, y//2, 2), self.land)

        base.camLens.setFov(90)

game = Game()
game.run()
