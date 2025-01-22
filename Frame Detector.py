import cv2 as cv
import numpy as np


map_img = cv.imread('https://github.com/jpedrocf/MachineLearningStudies/blob/main/ObjectDetection/poringmap.jpg', cv.IMREAD_UNCHANGED)
poring_img = cv.imread('https://github.com/jpedrocf/MachineLearningStudies/blob/main/ObjectDetection/poringclose.jpg', cv.IMREAD_UNCHANGED)

resultado = cv.matchTemplate(map_img, poring_img, cv.TM_CCOEFF_NORMED) 

# Teste de imagem
# cv.imshow('Resultado', resultado)
# cv.waitKey()

# os melhores matchs
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultado)

print('Melhor Match Position: %s' % str(max_loc))
print('Melhor Match Confidence: %s' % max_val)


pontodecorte = 0.8

if max_val >= pontodecorte:
    print('Achei')

    # pegando as dimensões da imagem do poring w = largura | h = altura
    poring_largura = poring_img.shape[1]
    poring_altura = poring_img.shape[0]

    coord_cima_esq = max_loc
    coord_baixo_dir = (coord_cima_esq[0] + poring_largura, coord_cima_esq[1] + poring_altura)

    # Desenha um retângulo ao redor levando em consideração as coordenadas do max_loc (ponto alto - esquerda) e o ponto máximo de baixo - direita, que é o max_loc[0] + largura da imagem por max_loc[1] + altura da imagem  
    cv.rectangle(map_img, coord_cima_esq, coord_baixo_dir,
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    
    cv.imshow('Resultado', map_img)
    cv.waitKey()

else:
    print('Não encontrado')
