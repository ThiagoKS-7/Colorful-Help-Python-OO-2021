# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:59:55 2020

@author: Thiago Kasper de Souza
"""


def serial_send(serial, ctg, color):
    # FUNÇÕES PARA RODAR EM CONJUNTO COM ARDUINO
    sum = (str(ctg) + color)
    print("Código concatenado: ", sum)
    # codifica_dados(int(sum))
    # serial.write(str(codifica_dados(int(sum))).encode())
    serial.close()
    return True


# FUNÇÃO QUE REDIMENSIONA A IMAGEM
def prepare(filepath):
    import cv2
    image_size = 40
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(image, (image_size, image_size))
    return resized_image.reshape(1, image_size, image_size, -1)


def ai_one():
    import cv2
    import tensorflow as tf
    # from ..lib.color.color_analysis import color_distinct
    from matplotlib import pyplot as plt
    import numpy as np
    import imageio
    import pyttsx3  # TTS = Text-To-Speech

    engine = pyttsx3.init()
    engine.setProperty('voice', 'pt')

    class_names = ["Bota", "Camisa", "Camiseta", "Tenis"]

    model = tf.keras.models.load_model("../models/AUG_K_TUNED-CNN2.model")
    print("Testes de predição:")
    print()
    captura = cv2.VideoCapture(0)
    cont = 0

    # ****************
    #   RECORDING DATA
    # ****************
    ##
    while True:
        ret, frame = captura.read()
        cont += 1
        if cont >= 25:
            break
             
    cv2.imwrite("new_img.jpg", frame)
    captura.release()
    cv2.destroyAllWindows()
        
    roupa = "new_img.jpg"

    # ****************
    #   PREDICTIONS
    # ****************
    ##
    prediction = model.predict([prepare(roupa)])
    print("Fig #1:")
    ctg = np.argmax(prediction.flatten())
    print(class_names[ctg])

    if ctg < 3 and ctg >= 0:   # 'Bota', 'Camisa' & 'Camiseta' = female article; 'Tenis' = male article
        engine.say("isso é uma" + class_names[ctg], )
    elif ctg == 3:
        engine.say("isso é um tênis")
    print("Posição da predição encontrada:", ctg)

    #TODO: CORREÇÃO DAS CORES DA IMAGEM, PRA APARECER NO PYPLOT
    #TODO: BOUNDING BOX ESTÁTICA CENTRALIZADA (NÃO LOCALIZA NOS CANTOS DA IMG)

    img = imageio.imread(roupa)
    img = cv2.resize(img, (200, 200))
    obj_found = cv2.rectangle(img, (45, 30), (170, 190), (0, 255, 0), 2)
    img_predicted = cv2.putText(obj_found, "Label: {}".format(class_names[ctg]), (12, 25), cv2.FONT_HERSHEY_SIMPLEX,
                                0.58, (0, 254, 0), 2)
    plt.imshow(img_predicted)
    plt.show()
    print()

    # DISTINÇÃO DA COR E FALA DELA
    #color = color_distinct(roupa)
    #engine.say("e sua cor é:" + color)
    engine.runAndWait()
    engine.stop()

    # ****************
    #   CLEANING VARIABLES
    # ****************
    ##

    # del class_names
    # del roupa
    del prediction
    del ctg, img, img_predicted
    del color, engine
    # del serial
    # del sum
    # del captura, ret,frame,cont


if __name__ == '__main__':
    ai_one()
