from keys import *

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True # modo espectador
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.7, 0)
        self.hero.setScale(0.4)
        self.hero.setH(180)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)

        self.camera_bind()
        self.accept_events()


    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 4, 2)
        self.camera_on = True


    def camera_free(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], pos[1] + 3, -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_on = False


    def switch_view(self):
        if self.camera_on:
            self.camera_free()
        else:
            self.camera_bind()


    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)


    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)


    def look_at(self, angle):
        '''devuelve las coordenadas a las que se desplaza el héroe en el punto (x, y)
        si caminan hacia un ángulo'''


        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())


        next_x, next_y = self.check_direction(angle)
        x_to = x_from + next_x
        y_to = y_from + next_y

        return x_to, y_to, z_from


    def just_move(self, angle):
        '''se mueve a las coordenadas deseadas en cualquier caso'''
        pos = self.look_at(angle)
        self.hero.setPos(pos)


    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
    def check_direction(self, angle):
        ''' devuelve cambios redondeados en las coordenadas X, Y
        correspondientes al movimiento hacia el ángulo.'''
        if angle >= 0 and angle <= 20:
            return (0, -1)
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


    def forward(self):
        angle =(self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)


    def change_mode(self):
        if self.mode:
            self.mode = False
            print('Modo Jugador')
        else:
            self.mode = True
            print('Modo Espectador')
    
    def try_move(self, angle):
        '''se mueve si puede'''
        pos = self.look_at(angle)
        if self.land.is_empty(pos):
            # hay un espacio libre frente a nosotros. Tal vez tengas que bajar:
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # no hay un espacio libre frente a nosotros. Si puedes, sube sobre ese bloque:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.is_empty(pos):
                self.hero.setPos(pos)
                # no se puede subir - nos quedamos quietos

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)
    
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.add_block(pos)
        else:
            self.land.build_block(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delete_block(pos)
        else:
            self.land.delete_block_from(pos)


    def accept_events(self):
        base.accept(key_switch_camera, self.switch_view)
        base.accept(key_switch_mode, self.change_mode)

        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)
        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)
        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)
        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)

        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept(key_save, self.land.save_map)
        base.accept(key_load, self.land.load_map)
