import numpy as np
import cv2 
import pandas as pd
from scipy.io.wavfile import write

img = cv2.imread("zebras.jpg")
height, width, depth = img.shape

#Converting Images to HSV 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      
#Extracting Hue channel from every pixel
i = 0
j = 0
hue_arr = []
for i in range(height):
    for j in range(width):
        hue = hsv[i][j][0]
        hue_arr.append(hue)

pixel_df = pd.DataFrame(hue_arr, columns = ['hue_arr'])

#Mapping Hue values to frequencies of a musical notes
frequency = [261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.0, 440.0, 466.2, 493.9]

def hue2freq(h,frequency):
    thresholds = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
    note = frequency[0]
    if (h <= thresholds[0]):
         note = frequency[0]
    elif (h > thresholds[0]) & (h <= thresholds[1]):
        note = frequency[1]
    elif (h > thresholds[1]) & (h <= thresholds[2]):
        note = frequency[2]
    elif (h > thresholds[2]) & (h <= thresholds[3]):
        note = frequency[3]
    elif (h > thresholds[3]) & (h <= thresholds[4]):    
        note = frequency[4]
    elif (h > thresholds[4]) & (h <= thresholds[5]):
        note = frequency[5]
    elif (h > thresholds[5]) & (h <= thresholds[6]):
        note = frequency[6]
    elif (h > thresholds[6]) & (h <= thresholds[7]):    
        note = frequency[7]
    elif (h > thresholds[7]) & (h <= thresholds[8]):
        note = frequency[8]
    elif (h > thresholds[8]) & (h <= thresholds[9]):
        note = frequency[9]
    elif (h > thresholds[9]) & (h <= thresholds[10]):    
        note = frequency[10]
    elif (h > thresholds[10]) & (h <= thresholds[11]):
        note = frequency[11]
    else:
        note = frequency[0]
    
    return note


pixel_df['notes'] = pixel_df.apply(lambda row : hue2freq(row['hue_arr'],frequency), axis = 1) 
print(pixel_df)

#Conversion of array to Audio

frequencies = pixel_df['notes'].to_numpy()

music = np.array([]) 
rate = 44100
T = 0.1  
t = np.linspace(0, T, int(T*rate), endpoint=False) 

nPixels = 500
for i in range(99200, 99200+nPixels):  
    val = frequencies[i]
    note  = 0.5*np.sin(2*np.pi*val*t) 
    music  = np.concatenate([music, note]) 

write("music.wav", rate, music)


