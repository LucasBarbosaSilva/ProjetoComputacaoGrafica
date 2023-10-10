from variaveisGlobais import *

def personagem():
    glPushMatrix()
    color = [0.4, 0.4, 0.2, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glutSolidSphere(0.5, 100, 20)
    glPopMatrix()