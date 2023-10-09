from variaveisGlobais import *

def parede():
    glColor3f(0, 0, 1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    
    glTranslate( 0, 0, 0)  #Transtacao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0) 
    glVertex3f(0, 2, 0) 
    glVertex3f(2, 2, 0) 
    glVertex3f(2, 0, 0)     
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(3, 0, 0) 
    glVertex3f(3, 2, 0) 
    glVertex3f(4, 2, 0) 
    glVertex3f(4, 0, 0)     
    glEnd()
    
    glPopMatrix()
