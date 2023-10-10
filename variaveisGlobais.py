from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

widthTela = 1080
heigthTela = 720
esqDirCamIni = 0
widthCampo = 4
xPersonagem = 0
zPersonagem = 0
yPersonagem = 0.25
zPersonagem = 4
xCamFim = 0
yCamFim = 0.25
zCamFim = 0
aux3 = 0
aux4 = 0
angulo = 30
tempoesteira = 0
liga_esteira_dir = 0
fire = 0
angulocanhao = 0
bala_xi= 0
posiLuz = 0
widthPersonagem = 0.5
raioPersonagem = widthPersonagem/2
mode = 0

velocidade = 0.5#0.05
espacamentoParedes = 6 # Espaço até a próxima parede
numParedes = 4 # Número de paredes visíveis
minPorta = 1
maxPorta = 2.8

larguraCampo = 4
variaveisIniciais = [xPersonagem, yPersonagem, zPersonagem, xCamFim, yCamFim, zCamFim, mode]
statusJogo = 0