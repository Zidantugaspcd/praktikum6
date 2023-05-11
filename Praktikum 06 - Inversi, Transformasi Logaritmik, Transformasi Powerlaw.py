 # Mengimport library yang digunakan
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load gambar dari local drive dengan cv2.imread
kucingturu = cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\mengantuk.jpg")# read file dari direktori file 

# Mendapatkan resolusi dan type dari gambar
kucingturu_height = kucingturu.shape[0]     # Mengambil tinggi gambar dalam piksel, dan menyimpannya dalam variabel
kucingturu_width = kucingturu.shape[1]      # Mengambil lebar gambar dalam piksel, dan menyimpannya dalam variabel
kucingturu_channel = kucingturu.shape[2]    # Mengambil jumlah channel warna dalam gambar, dan menyimpannya dalam variabel

# PERCOBAAN PERTAMA : INVERSI
# Membuat variabel kucingturu_inversi
kucingturu_inversi = np.zeros(kucingturu.shape, dtype=np.uint8)# buat variabel kosong dengan data type uit 8

# Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):# definisikan inversi graysacale
    for y in range(0, kucingturu_height):# untuk y range 0 sampai heigh
        for x in range(0, kucingturu_width):# untuk x range 0 sampai width
            red = kucingturu[y][x][0] # utuk definsi warna merah
            green = kucingturu[y][x][1]# untuk definisi warna hijau
            blue = kucingturu[y][x][2]# ntuk definisi warna biru
            gray = (int(red) + int(green) + int(blue)) / 3# image dibuat grayscale dengan membagi niali rgb
            gray = nilai - gray# nilai - gray
            kucingturu_inversi[y][x] = (gray, gray, gray)# output gray

# Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai): # definisi nilai inversi
    for y in range(0, kucingturu_height):# unutk loop 0 sampai height
        for x in range(0, kucingturu_width):# untuk loop dari 0 ssampai widdth
            red = kucingturu[y][x][0]# untuk red cahhanel
            red = nilai - red # mengurangi nilai chanel dengan red
            green = kucingturu[y][x][1]# untuk chanel hijau
            green = nilai - green# mengurangi nilai chanel dengan hijau
            blue = kucingturu[y][x][2]# untuk chanel dengan hijau
            blue = nilai - blue# mengurangi nilai chanel dengan biru
            kucingturu_inversi[y][x] = (red, green, blue)# menyamakan dimensi dengan warna RGB

# Menampilkan hasil inversi
inversi_grayscale(255)
plt.imshow(kucingturu_inversi)# tampilkan  inversi rgb
plt.title("Inversi Grayscale")# beri tiltle
plt.show()

inversi_rgb(255)
plt.imshow(kucingturu_inversi)# tampilkan inversi rgb
plt.title("Inversi RGB")# beri tiltle
plt.show()
 # PERCOBAAN KEDUA : TRANSFORMASI LOGARITMIK

# Membuat variabel kucingturu_log untuk menampung hasil
kucingturu_log = np.zeros(kucingturu.shape, dtype=np.uint8)# kosongkan variable

# Mendefinisikan fungsi untuk log
def log(c): # definisi log
    for y in range(0, kucingturu_height):# loop y range 0, sampai height
        for x in range(0, kucingturu_width):# loop x dengan range 0 sampai width
            red = kucingturu[y][x][0] # chanel red 
            green = kucingturu[y][x][1]# chanel green
            blue = kucingturu[y][x][2]# chanel blue
            gray = (int(red) + int(green) + int(blue)) / 3 # mebagi dimensi menjadi grayscale
            gray = int(c * np.log(gray + 1))# membuat fungsi gambar log
            if gray > 255:# bila gray lebih besar dari 255 maka 
                gray = 255# gray = 255
            if gray < 0:# bila 0
                gray = 0# maka gray = 0
            kucingturu_log[y][x] = (gray, gray, gray)

# Menampilkan hasil log
log(30)
plt.imshow(kucingturu_log)
plt.title("Log")# beri tiltle
plt.show()
# PERCOBAAN KETIGA : INVERSI DAN LOG

# Membuat variabel kucingturu_inlog untuk menampung hasil
kucingturu_inlog = np.zeros(kucingturu.shape, dtype=np.uint8)

# Mendefinisikan fungsi untuk inversi log
def inlog(c):
    for y in range(0, kucingturu_height):
        for x in range(0, kucingturu_width):
            red = kucingturu[y][x][0]
            green = kucingturu[y][x][1]
            blue = kucingturu[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(c * np.log(255 - gray + 1))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            kucingturu_inlog[y][x] = (gray, gray, gray)

# Menampilkan hasil inversi log
inlog(30)
plt.imshow(kucingturu_inlog)
plt.title("Inversi & Log")# beri tiltle
plt.show()
# PERCOBAAN KEEMPAT : NTH POWER

# Membuat variabel kucingturu_nthpower untuk menampung hasil
kucingturu_nthpower = np.zeros(kucingturu.shape, dtype=np.uint8)

# Mendefinisikan fungsi untuk nth power
def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, kucingturu_height):
        for x in range(0, kucingturu_width):
            red = kucingturu[y][x][0]
            green = kucingturu[y][x][1]
            blue = kucingturu[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            kucingturu_nthpower[y][x] = (gray, gray, gray)

# Menampilkan hasil
nthpower(50, 100)
plt.imshow(kucingturu_nthpower)
plt.title("Nth Power")# beri tiltle
plt.show()
# PERCOBAAN KELIMA : NTH ROOT POWER

# Membuat variabel kucingturu_nthrootpower
kucingturu_nthrootpower = np.zeros(kucingturu.shape, dtype=np.uint8)

# Membuat fungsi untuk nth root power
def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, kucingturu_height):
        for x in range(0, kucingturu_width):
            red = kucingturu[y][x][0]
            green = kucingturu[y][x][1]
            blue = kucingturu[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            kucingturu_nthpower[y][x] = (gray, gray, gray)

# Menampilkan hasil
nthrootpower(50, 100)
plt.imshow(kucingturu_nthrootpower)# tampilkan kucing nthrootpower
plt.title("Nth Root Power")# buat title
plt.show()# tampilkan