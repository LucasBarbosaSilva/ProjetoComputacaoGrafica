from variaveisGlobais import *

def paredeLateral():
    glPushMatrix()    
    glBegin(GL_POLYGON)
    glTexCoord2f (0.0, 3.0)
    glVertex3f(0, 3, 0)
    
    glTexCoord2f (3.0, 3.0)
    glVertex3f(0, 3, -18)

    glTexCoord2f (3.0, 0.0)
    glVertex3f(0, 0, -18)

    glTexCoord2f (0.0, 0.0)
    glVertex3f(0.0, 0.0, 0)    
    glEnd()
    glPopMatrix()