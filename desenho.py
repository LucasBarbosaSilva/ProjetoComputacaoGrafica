from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import eixos
import variaveisGlobais
from piso import *

def desenho():
    global aux1
    global aux2
    global tempoesteira
    global liga_esteira_dir
    global fire
    global angulocanhao
    global bala_xi

    eixos.eixos()

    piso()
