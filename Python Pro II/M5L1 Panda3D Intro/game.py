# Importación del módulo ShowBase (la clase ShowBase):
from direct.showbase.ShowBase import ShowBase
'''La clase ShowBase es una clase base proporcionada por Panda3D
que se utiliza para inicializar y ejecutar la aplicación de juego.'''

# Definición de la clase Game:
class Game(ShowBase):
    '''Aquí se define el método __init__ de la clase Game.
    Este método se llama automáticamente cuando se crea una nueva instancia de la clase Game.
    Dentro de este método, se llama al método __init__ de la clase base ShowBase
    utilizando ShowBase.__init__(self) para inicializar la aplicación de juego.'''
    
    # Inicialización del método constructor:
    def __init__(self):
        ShowBase.__init__(self)
        # Carga y manipulación de un modelo 3D:
        self.model = loader.loadModel('Boeing707.egg') # cargar modelo 3D
        texture = loader.loadTexture('BoeingTexture.tif') # cargar texturas para el modelo
        self.model.setTexture(texture) # establecer la textura
        self.model.reparentTo(render) # establecer el modelo como hijo del nodo 'render'
        self.model.setScale(0.1) # ajustando la escala del modelo
        self.model.setPos(-2, 25, -3) # establecer su posición en la escena

        base.camLens.setFov(90) # establecer el ángulo de visión a 90 grado

# Creación de una instancia de la clase Game y ejecución del juego
game = Game()
game.run()

'''Nodos del grafo de la escena: 
En Panda3D, la escena se organiza como un grafo de escena. 
Un grafo de escena es una estructura de datos que organiza los elementos de la escena en forma de nodos conectados entre sí.
Cada nodo puede representar un objeto en la escena, como un modelo 3D, una luz, una cámara, etc. 
Estos nodos están interconectados para formar una estructura jerárquica.

Árbol que contiene todos los modelos que necesitan ser mostrados: 
La escena se organiza en forma de árbol, donde cada nodo del árbol representa un objeto en la escena. 
Esta estructura jerárquica permite organizar los elementos de la escena de manera eficiente
y facilita la manipulación y renderizado de la misma. 
Todos los modelos y elementos que necesitan ser mostrados en la escena están contenidos dentro de este árbol de escena.'''

