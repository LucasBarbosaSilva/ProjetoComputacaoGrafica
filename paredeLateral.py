from PIL import Image as Image
import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from variaveisGlobais import *

def paredeLateral():
    glPushMatrix()    

    glTranslate(0, 0, 0)
    tex = read_texture('imagens/concretetiles.jpg')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex)

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
