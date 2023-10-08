from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from variaveisGlobais import angulo, angulocanhao, aux1, aux2, aux3, aux4, bala_xi, cimabaixo, esqdir, fire, liga_esteira_dir, tempoesteira

def iluminacao_da_cena():
    global aux1
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[aux1, 50.0, 50.0, 1.0]

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60

    # Especifica que a cor de fundo da janela sera branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorizacao de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletancia do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentracao do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parametros da luz de numero 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

    # Habilita a definicao da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminacao
    glEnable(GL_LIGHTING)
    # Habilita a luz de numero 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)