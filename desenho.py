from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import eixos
import variaveisGlobais
from parede import *
from piso import *
from paredeLateral import *

def desenho():
    global xPersonagem
    global yPersonagem
    global zPersonagem
    global xCamFim
    global yCamFim
    global zCamFim
    global tempoesteira
    global liga_esteira_dir
    global fire
    global angulocanhao
    global bala_xi

    # eixos.eixos()
    # glPushMatrix()
    # glTranslate(-2, 0, -6)
    # parede()
    # glPopMatrix()
    # glPushMatrix()
    # glTranslate(-2, 0, 0)
    # parede()
    # glPopMatrix()

    eixos.eixos()

    for p in paredes:
        p.desenhar()

    piso()

    # Paredes laterais
    glPushMatrix()
    glTranslate(-2, 0, 6)
    paredeLateral()    
    glPopMatrix()
    glPushMatrix()
    glTranslate(2, 0, 6)
    paredeLateral()    
    glPopMatrix()    
    

