from PIL import Image as Image
import numpy
#from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from variaveisGlobais import *

def parede():
    glColor3f(0, 0, 1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    
    glTranslate( 0, 0, 0)
    tex = read_texture('gritwall2.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex)
    glColor3f(0, 0, 1)

    glBegin(GL_POLYGON)
    glTexCoord2f (0.0, 0.0);
    glVertex3f(0, 0, 0) 

    glTexCoord2f (3.0, 0.0);
    glVertex3f(0, 2, 0) 

    glTexCoord2f (3.0, 3.0);
    glVertex3f(2, 2, 0)

    glTexCoord2f (0.0, 3.0); 
    glVertex3f(2, 0, 0)     
    glEnd()

#    glDisable(GL_TEXTURE_2D)

    glBegin(GL_POLYGON)
    glTexCoord2f (0.0, 0.0);
    glVertex3f(3, 0, 0) 

    glTexCoord2f (3.0, 0.0);
    glVertex3f(3, 2, 0) 

    glTexCoord2f (3.0, 3.0);
    glVertex3f(4, 2, 0) 

    glTexCoord2f (0.0, 3.0);
    glVertex3f(4, 0, 0)     
   
    glEnd()

    glDisable(GL_TEXTURE_2D)
    
    glPopMatrix()

#def pisotextura():
    #glColor3f(0.7, 0.7, 0.7) # cor RGB
  #  glPushMatrix()
 #   glTranslate( 0.0, -1.0, 0.0)  #Transtacao do objeto
    # Textured 
    
    
#    glBegin(GL_POLYGON)
    #gluCylinder(textura, largura da base, largura do topo, altura, resoluc


def read_texture(filename):
      img = Image.open(filename)
      img_data = numpy.array(list(img.getdata()), numpy.int8)
      textID = glGenTextures(1)
      glBindTexture(GL_TEXTURE_2D, textID)
      glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
      #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)    #  Opcao para Truncar a figura
      #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)      
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)   #  Opcao para repetir a figura
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
      glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      #glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE)
      #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_SPOT_DIRECTIONAL)
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
      return textID
