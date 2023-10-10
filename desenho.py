from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import eixos
import variaveisGlobais
from parede import *
from piso import *

def desenho():
    global xCamIni
    global yCamIni
    global zCamIni
    global xCamFim
    global yCamFim
    global zCamFim
    global tempoesteira
    global liga_esteira_dir
    global fire
    global angulocanhao
    global bala_xi

    eixos.eixos()
    glPushMatrix()
    glTranslate(-2, 0, -6)
    parede()
    glPopMatrix()
    glPushMatrix()
    glTranslate(-2, 0, 0)
    parede()
    glPopMatrix()
    piso()
