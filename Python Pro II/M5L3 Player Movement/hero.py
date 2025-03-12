

class Hero():
    def __init__(self, position, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor((1, 0.7, 0, 1))
        self.hero.setScale(0.4)
        self.hero.setPos(position)
        self.hero.reparentTo(render)
        self.mode = True

        self.camera_bind()
        self.accept_events()

    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 2)
        self.camera_on = True

    def camera_free(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1]+5, -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_on = False

    def accept_events(self):
        base.accept('c', self.change_view)
        base.accept('n', self.turn_left)
        base.accept('n-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m-repeat', self.turn_right)
        base.accept('w', self.forward)
        base.accept('w-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s-repeat', self.back)
        base.accept('a', self.left)
        base.accept('a-repeat', self.left)
        base.accept('d', self.right)
        base.accept('d-repeat', self.right)


    def change_view(self):
        if not self.camera_on:
            self.camera_bind()
        else:
            self.camera_free()
    
    def turn_left(self):
        self.hero.setH(
            (self.hero.getH() + 5) % 360
        )

    def turn_right(self):
        self.hero.setH(
            (self.hero.getH() - 5) % 360
        )

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pass

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
        
    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)
