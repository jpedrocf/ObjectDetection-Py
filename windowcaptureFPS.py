import numpy as np
import cv2 as cv
from time import time
from windowcaptureClass import WindowCapture

win_cap = WindowCapture('Ragnagoats | Gepard Shield 3.0 (^-_-^)')

loop_time = time()

while(True):
    screenshot = win_cap.get_screenshot()

    cv.imshow('Window Capture FPS', screenshot)
    
    # Calculando o FPS (Frames por Segundo)
    # O FPS é determinado dividindo 1 segundo pelo tempo que levou para executar uma iteração do loop.
    # O tempo de uma iteração é dado por (time() - loop_time), ou seja, o tempo atual menos o tempo registrado no início da iteração anterior.

    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Finalizado.')
