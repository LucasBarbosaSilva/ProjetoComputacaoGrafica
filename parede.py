from variaveisGlobais import *

def parede():
    glColor3f(0, 0, 1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    
    glTranslate( 0, 0, 0)  #Transtacao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, -1) 
    glVertex3f(0, 180, -1) 
    glVertex3f(600, 180, -1) 
    glVertex3f(600, 0, -1)     
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(700, 0, -1) 
    glVertex3f(700, 180, -1) 
    glVertex3f(820, 180, -1) 
    glVertex3f(820, 0, -1)     
    glEnd()
    
    glPopMatrix()
