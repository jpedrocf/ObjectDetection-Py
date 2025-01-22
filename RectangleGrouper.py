import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

map_path = 'https://github.com/jpedrocf/MachineLearningStudies/blob/main/ObjectDetection/poringmap.jpg'
poring_path = 'https://github.com/jpedrocf/MachineLearningStudies/blob/main/ObjectDetection/poringclose.jpg'

def localizadorPosicao(map_path, poring_path, pontodecorte=0.65, mododemarcar=None):
    map_img = cv.imread(map_path, cv.IMREAD_UNCHANGED)
    poring_img = cv.imread(poring_path, cv.IMREAD_UNCHANGED)

    # dimensões da imagem
    poring_largura = poring_img.shape[1]
    poring_altura = poring_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED

    metodo = cv.TM_CCOEFF_NORMED
    resultado = cv.matchTemplate(map_img, poring_img, metodo)

    # Pegar coordenadas que estejam acima do pontodecorte (zip combina os index elemento por elemento, [::-1] inverte)
    coordenadas = np.where(resultado >= pontodecorte)
    coordenadas = list(zip(*coordenadas[::-1]))

    # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
    # locations by using groupRectangles().
    # First we need to create the list of [x, y, w, h] rectangles

    retangulos = []
    for coord in coordenadas:
        retang = [int(coord[0]), int(coord[1]), poring_largura, poring_altura]

        # 2 appends pois o código estava sumindo com os retangulos sem overlap, dessa forma todos vão ter pelo menos 1 overlap
        retangulos.append(retang)
        retangulos.append(retang)

    retangulos, pesos = cv.groupRectangles(retangulos, groupThreshold=1, eps=0.5)
    # print(retangulos)

    pontos = []
    if len(retangulos):

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (22, 222, 25)
        marker_type = cv.MARKER_CROSS

        # Loop para todos os retangulos
        for (x, y, w, h) in retangulos:

            # Determinar o centro de x e y (utilizei inteiro para não cair uma coordenada quebrada)
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            pontos.append((center_x, center_y))

            if mododemarcar == 'retangulos':
                top_esquerdo = (x, y)
                bot_direito = (x+w, y+h)
                cv.rectangle(map_img, top_esquerdo, bot_direito, color=line_color, lineType=line_type, thickness=2)

            elif mododemarcar == 'pontos':
                cv.drawMarker(map_img, (center_x, center_y), color=marker_color, markerType=marker_type, thickness=2)
            
        if mododemarcar:
            cv.imshow('Coords', map_img)
            cv.waitKey()

    return pontos


marcador = localizadorPosicao(map_path, poring_path, mododemarcar='retangulos')
print(marcador)

print('Localizador efetuado com sucesso.')
