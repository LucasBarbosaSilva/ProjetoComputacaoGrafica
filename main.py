# Aula sobre composicao de objetos e uso do teclado.
from math import cos
from math import pi
from math import sin
from math import tan
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global tempoesteira
global fire
global angulocanhao
global liga_esteira_dir
global bala_xi
global distancia
from variaveisGlobais import *
from iluminacao import *
from desenho import *
from parede import *

def tela():
    global angulo
    global mode
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(0, 0, 0, 0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projecao
    glLoadIdentity()# carrega a matriz identidade

    #gluPerspective(angulo, aspecto , near, far )
    #  angulo = angulo em graus na direcao y.
    #  aspecto = deformacao da janela. normalmente e a razao entre a largura e altura
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    gluPerspective(angulo,1,0.1,500) # Especifica a projecao perspectiva

    #glOrtho(left,right,bottom, top, near, far)
    #  left,right,bottom, top = limites da projecao
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado 
    #glOrtho(-5,5,-5,5,0.1,500) # Especifica a projecao paralela ortogonal

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posicao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posicao vertical da camera.
    if(mode == 0):
    #                    (x, y, z) Câmera                   |   (x, y, z,) Objeto      |   posicao 
        gluLookAt(xCamIni, 1 + yCamIni, cos(zCamIni)*4, xCamFim, yCamFim, zCamFim, 0,1,0) # Especifica posicao do observador e do alvo
    else:
        gluLookAt(0, 5, 8, xCamFim, yCamFim, zCamFim, 0,1,0) # Especifica posicao do observador e do alvo
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d
    
    desenho()                    
    
    glFlush()                    # Aplica o desenho

def resetGame():
    global xCamIni
    global yCamIni
    global zCamIni
    global xCamFim
    global yCamFim
    global zCamFim
    global mode
    xCamIni, yCamIni, zCamIni, xCamFim, yCamFim, zCamFim, mode = 0, 1, 0, 0, 1, 0, 0

# Funcao callback chamada para gerenciar eventos de teclas normais 
def Teclado (tecla, x, y):
    global esqDirCamIni
    global xCamIni
    global yCamIni
    global zCamIni
    global zCamIni
    global xCamFim
    global yCamFim
    global zCamFim
    global aux1
    global aux2
    global esqdir
    global esqdir
    global tempoesteira
    global liga_esteira_dir
    global fire
    global angulocanhao
    global mode

    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)
	
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A -> Esqueda
        print((-widthTela/2)+(widthPersonagem/2))
        print(xCamFim)
        if (xCamFim - 0.1 >= (-widthTela/2)+(widthPersonagem/2)):
            xCamFim -= 0.1
            xCamIni -= 0.1
            print("Andou")
	
    if tecla == b'd': # D -> Direita
        print((widthTela/2)-(widthPersonagem/2))
        print(xCamFim)
        if (xCamFim + 0.1 <= (widthTela/2)-(widthPersonagem/2)):
            xCamFim += 0.1
            xCamIni += 0.1
            print("Andou")

    if tecla == b'r':
        resetGame()

    if tecla == b'c':
        mode = (mode+1) % 2
    
    tela()
    glutPostRedisplay()

# Funcao callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global xCamFim
    global yCamFim
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        xCamFim -= 0.1
    elif tecla == GLUT_KEY_RIGHT:
        xCamFim += 0.1
    elif tecla == GLUT_KEY_UP:
        yCamFim += 0.1
    elif tecla == GLUT_KEY_DOWN:
        yCamFim -= 0.1
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()   

def Timer(tempo):
    print("Timer rodando")
    glutPostRedisplay()
    glutTimerFunc(33,Timer, 0)

# Funcao callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
            if (angulo >= 10):
                angulo -= 2
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(widthTela,heigthTela)
glutCreateWindow(b"Projeto Final CG")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutTimerFunc(33,Timer, 0)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laco de eventos da GLUT



