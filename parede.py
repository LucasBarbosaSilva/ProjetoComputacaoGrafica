from PIL import Image as Image
import numpy
#from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randrange, random

from variaveisGlobais import *


class Parede:
    def __init__(
        self,
        zIniPos,
        espacamento = espacamentoParedes,
        qtdParedes = numParedes
    ):
        self.zPos = zIniPos
        self.color = (0, 0, 1)


        self.portaLargura = minPorta + random()*(maxPorta-minPorta)
        self.portaPos = random()*(larguraCampo-self.portaLargura)

        self.espacamento = espacamento
        self.qtdParedes = qtdParedes

        # 2: normal; 1: próximo; 0: muito próximo
        self.proxPersonagem = 2

    @staticmethod
    def criarParedes(qtd, espacamento):
        return [
            Parede(-i*espacamento, espacamento=espacamento, qtdParedes=qtd) for i in range(qtd)
        ]
    
    def atualizarPos(self):
        self.zPos += velocidade

        if 3 > self.zPos >= 0: # 3 > self.zPos >= 1
            self.proxPersonagem = 2
        # elif 3 > self.zPos >= -2:
        #     self.proxPersonagem = 1
        else:
            self.proxPersonagem = 0


        if self.zPos >= self.espacamento:
            self.zPos = -self.espacamento*(self.qtdParedes-1)
            # Definindo largura da nova porta:
            self.portaLargura = minPorta + random()*(maxPorta-minPorta)
            
            # Definindo posição da passagem:
            self.portaPos = random()*(larguraCampo-self.portaLargura)


    def desenhar(self):
        glPushMatrix()
        glTranslate(-2, 0, self.zPos)
        
        glColor3f(0, 0, 1)
        glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
        
        glTranslate( 0, 0, 0)
        # tex = read_texture('parede.jpg')
        # glEnable(GL_TEXTURE_2D)
        # glBindTexture(GL_TEXTURE_2D, tex)

        glBegin(GL_POLYGON)
        
        # glVertex3f(self.portaPos, 2, 0) 
        # glVertex3f(self.portaPos, 0, 0)     

        glTexCoord2f (0.0, 0.0);
        glVertex3f(0, 0, 0) 

        glTexCoord2f (3.0, 0.0);
        glVertex3f(0, 2, 0) 

        glTexCoord2f (3.0, 3.0);
        glVertex3f(self.portaPos, 2, 0)

        glTexCoord2f (0.0, 3.0); 
        glVertex3f(self.portaPos, 0, 0)     
        glEnd()

    #    glDisable(GL_TEXTURE_2D)

        glBegin(GL_POLYGON)
        glTexCoord2f (0.0, 0.0);
        glVertex3f(self.portaPos+self.portaLargura, 0, 0) 

        glTexCoord2f (3.0, 0.0);
        glVertex3f(self.portaPos+self.portaLargura, 2, 0) 

        glTexCoord2f (3.0, 3.0);
        glVertex3f(4, 2, 0) 

        glTexCoord2f (0.0, 3.0);
        glVertex3f(4, 0, 0)     
    
        glEnd()

        glDisable(GL_TEXTURE_2D)
        
        glPopMatrix()
        glPopMatrix()


paredes = Parede.criarParedes(qtd=4, espacamento=6)



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
