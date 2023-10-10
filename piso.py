from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import variaveisGlobais

def piso():
    glColor3f(0.5, 0.5, 0.5)

    glPushMatrix()

    glTranslate(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(2.0, 0.0, -12.0)
    glVertex3f(2.0, 0.0, 6.0)
    glVertex3f(-2.0, 0.0, 6.0)
    glVertex3f(-2.0, 0.0, -12.0)
    glEnd()

    glPopMatrix()
