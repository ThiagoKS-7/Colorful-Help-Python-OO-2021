# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:24:29 2020

@author: Thiago Kasper de Souza
"""
# TODO: consertar lógica da análise de cor
from matplotlib import pyplot as plt
import numpy as np


def color_distinct(filepath):
    # redimensionamento da img pra distinguir a cor direito
    # img_col=imageio.imread(filepath)
    # resized_col = cv2.resize(img_col, (100,100))
    # centro_col= resized_col[40:60 , 40:60]  # área de interesse plotada  [40:60, 40:60

    img = cv2.imread(filepath)
    resized = cv2.resize(img, (100, 100))
    center = resized[40:60, 40:60]  # construção da área de interesse

    # plt.imshow(centro_col)
    # plt.show()
   color = ('b', 'g', 'r')  # lista dos canais para o histograma
   for i, col in enumerate(color):
       histr = cv2.calcHist([center], [i], None, [256], [0,256]) # constrói o histograma p/
       # cada posição da lista cor
       plt.plot(histr, color_recog = col) # mostra o gráfico
       plt.xlim([0,256]) #limite d x

       # Condições que guardam o valor da frequência e classe de cada histr (y e x)
       if i == 0:
           ymax = max(histr)
           xmax, _ = np.where(histr == ymax)
           blue = xmax[0]
       elif i == 1:
           ymax1 = max(histr)
           xmax1, _ = np.where(histr == ymax1)
           green = xmax1[0]
       else:
           ymax2 = max(histr)
           xmax2, _ = np.where(histr == ymax2)
           red = xmax2[0]
       #mostra o pico de cada gráfico, na mesma ordem q na lista cor
       print("Código:", "R:", red, "G:", green, "B:", blue)
        # condições q analisam o intervalo das cores

   if (red > (green + 20)) and (red > (blue + 10)) and (red >= 40 and red <= 255) and (green >= 20 and green <= 190) and (blue >= 3 and blue <= 120):
       color_name = "azul"
       number = '0'

   elif (red >= 0 and red <= 120) and (green >= 15 and green <= 110) and (blue >= 25 and blue <= 145):
       color_name= "marrom"
       number = 1

   elif (red >= 0 and red <= 108) and (green >= 0 and green <= 111) and (blue >= 0 and blue <= 35):
       color_name= "preto"
       number = 2

   elif (red >= 0 and red <= 148) and (green >= 100 and green <= 230) and (blue >= 170 and blue <= 254):
       color_name= "amarelo"
       number = 3

   elif (blue > (red + 20)) and  (blue > (green + 20)) and (red >= 15 and red <= 188) and (green >= 0 and green <= 130) and (blue >= 80 and blue <= 255):
      color_name= "vermelho"
      return color_name

   elif (green > (red + 20)) and (green > (blue + 20)) and (red >= 0 and red <= 170) and (green >= 55 and green <= 255) and (blue >= 10 and blue <= 90):
      color_name= "verde"
      number = 4
      return [color_name,'5']
   elif (red >= 0 and red <= 35) and (green >= 55 and green <= 190) and (blue >= 200 and blue <= 255):
      color_name= "laranja"
      number = 5

   else:
      color_name= "branco"
      number = 6

   response = [color_name, number]
   return response
"""
def codifica_dados(x):
    if x < 9: # bota
        codigos1 = ['0','1','2','3','4','5','6','7']
        print("Código enviado: ", codigos1[x])
        return  codigos1[x] 
    
    elif (x >= 10) and (x < 19): # camisa
        codigos2 = ['q','w','e','r','t','y','u','i']
        b = x % 10    
        print("Código enviado: ", codigos2[b])
        return codigos2[b]
    elif (x >= 20) and (x < 29): # camiseta
        codigos3 = ['a','s','d','f','g','h','j','k']
        c = x % 20    
        print("Código enviado: ", codigos3[c])
        return codigos3[c] 
    elif (x >= 30) and (x < 39): # tenis
        codigos4 = ['z','x','c','v','b','n','m',',']
        d = x % 30    
        print("Código enviado: ", codigos4[d])
        return codigos4[d] 

"""
#codifica_dados(11)
#codifica_dados(23)
