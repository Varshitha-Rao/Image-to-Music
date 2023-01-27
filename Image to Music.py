import numpy as np
import cv2
from scipy.io.wavfile import write

img = cv2.imread("C:/Users/HP/OneDrive/Pictures/ash.jpg")
img_arr = np.array(img)
print(img_arr.size)
print(img_arr.shape)

rate = 44100
scaled = np.int16(img_arr/ np.max(np.abs(img_arr))*32767)
write("music.wav", rate, scaled)


