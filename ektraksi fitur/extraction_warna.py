import cv2
import numpy as np

img_bgr = cv2.imread('apel.jpg') #gambar origin apel
img_hsv = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV) #to hsv color

a = img_hsv.shape[0] #ukuran pixcel x
b = img_hsv.shape[1] #ukuran pixcel b
h = [] #array h
s = [] #array s
v = [] #array v


for x in range(int(a/2)-10,int(a/2)+9): #looping nilai pixcel x
    for y in range(int(b/2)-10,int(b/2)+9):  #looping nilai pixcel y
        h.append(img_hsv[x,y][0]) #tambahkan ke variabel h nilai pixcel X&Y [0 nilai hue]
        s.append(img_hsv[x,y][1]) #tambahkan ke variabel s nilai pixcel X&Y [1 nilai saturation]
        v.append(img_hsv[x,y][2]) #tambahkan ke variabel v nilai pixcel X&Y [2 nilai value]

H = np.array(h) #array hue dari semua looping
S = np.array(s) #array saturation dari semua looping
V = np.array(v) #array value dari semua looping

h_min = np.min(H) #nilai min H
h_max = np.max(H) #nilai max H
s_min = np.min(S) #nilai min S
s_max = np.max(S) #nilai max S
v_min = np.min(V) #nilai min V
v_max = np.max(V) #nilai min max

print("H:",np.mean(h_min+h_max)) #cetak nilai H
print("S:",np.mean(s_min+s_max))  #cetak nilai S
print("V:",np.mean(v_min+v_max))  #cetak nilai V
