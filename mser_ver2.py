#!/usr/bin/env python
import numpy as np
import cv2
import cv
import video

import sys
mser = cv2.MSER()
img=cv.LoadImage('/home/ilya/src_open_cv/vsplesk.png',cv.CV_LOAD_IMAGE_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()
regions = mser.detect(gray, None)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (255, 0, 0))
cv2.imshow('img', vis)

cv2.waitKey(100)

cv2.destroyAllWindows()
