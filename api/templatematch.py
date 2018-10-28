import numpy as np
import cv2
from matplotlib import pyplot as plt

def recogniseImage(images, template):
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    final_max = 0
    id_maxValue = {}

    for image in images:
        for meth in methods:
            method = eval(meth)

            res = cv2.matchTemplate(template,image,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            if max_val < 0.5:
                continue
            elif max_val > final_max:
                final_max = max_val
        id_maxValue[image.id] = image.value 
    return max(id_maxValue.iterkeys(), key=(lambda key: id_maxValue[key]));