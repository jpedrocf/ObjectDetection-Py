import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


map_img = cv.imread('https://github.com/jpedrocf/MachineLearningStudies/blob/main/ObjectDetection/poringmap.jpg', cv.IMREAD_UNCHANGED)
poring_img = cv.imread('https://github.com/jpedrocf/MachineLearningStudies/blob/main/ObjectDetection/poringclose.jpg', cv.IMREAD_UNCHANGED)

# dimensões da imagem
poring_largura = poring_img.shape[1]
poring_altura = poring_img.shape[0]

# 6 métodos para teste:
# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED (testar os 6 para ver o que melhor se adequa a imagem)

metodo = cv.TM_CCOEFF_NORMED
resultado = cv.matchTemplate(map_img, poring_img, metodo)


# os melhores matchs
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultado)

print('Melhor Match Position: %s' % str(max_loc))
print('Melhor Match Confidence: %s' % max_val)


pontodecorte = 0.65
coord_cima_esq = max_loc
coord_baixo_dir = (coord_cima_esq[0] + poring_largura, coord_cima_esq[1] + poring_altura)
local = np.where(resultado >= pontodecorte)


for pt in zip(*local[::-1]):
    cv.rectangle(map_img, pt, (pt[0] + poring_largura, pt[1] + poring_altura), color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

cv.imshow('Resultado', map_img)
cv.waitKey()
