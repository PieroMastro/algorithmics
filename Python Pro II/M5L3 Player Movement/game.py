from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadLand("land.txt")

        self.hero = Hero((1, 25, 2), self.land)
        base.camLens.setFov(90)


game = Game()
game.run()
