# import library
import numpy as np # import library numpy dipanggil dengan np
import cv2 # sudah jelas
import matplotlib.pyplot as plt # import library matplotlib dengan panggilan plt

# mebaca Gambar
kucingturu = cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\mengantuk.jpg")# read file dari direktori file 
img_height = kucingturu.shape[0] # insialisasi variabel berisi tinggi gambar 
img_width = kucingturu.shape[1]  # inisialisasi variabel berisi lebar gambar
img_channel = kucingturu.shape[2] # inisialisasi variabel berisi chanel warna

# merubah gambar menjadi grayscale
img_grayscale = np.zeros(kucingturu.shape, dtype=np.uint8)# membuat variabel grayscale dengan mengisi mengisi array citra dengan nilai 0 
for y in range(0, img_height):# loop untuk variabel y dimulai dari 0 sampai img_height
    for x in range(0, img_width): #loop untuk variabel x dimulai dari 0 sampai img_width
        red = kucingturu[y][x][0] # untuk variabel red pada chanel menjdai 0
        green = kucingturu[y][x][1] # untuk variabel green pada chanel menajdi 1
        blue = kucingturu[y][x][2] # untuk variabel blue pada chanel menjadi 2
        gray = (int(red) + int(green) + int(blue)) / 3 #setiap int pada chanel dibagi 3 untuk menghasilkan 1 cahnel grayscael
        img_grayscale[y][x] = (gray, gray, gray) # mengubah bentuk y dan y menjadi grayscale pada masing masing chanel RGBnya
        
plt.imshow(img_grayscale)# tampilkan grayscale
plt.title("Grayscale")# buat tittle grayscale
#==========================================================================================================================================
#Menampilkan Histogram Gambar Grayscale
#Membuat variabel untuk menyimpan data gambar
hg = np.zeros((256))# array numpy hg dengan ukuran 256 dan diisi dengan nilai nol.

#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): # loop untuk x  dari range 0 sampai 256
    hg[x] = 0 # hg x = 0

#Menghitung nilai dari gambar
for y in range(0, img_height): # loop untuk y dalam range 0 sampai img height
    for x in range(0, img_width): # loop untuk x dalam range 0 sampai img width
        gray = img_grayscale[y][x][0]# channel grayscale = gray
        hg[gray] += 1 #increment pada index gray, dan setiap nilai piksel yang sama intensitasnya pada gray dan hg mengalami decrement 1

#Menampilkan Histogram
plt.figure(figsize=(20, 6))# buat figur dengan size 20 banding 6
plt.plot(hg, color="black", linewidth=2.0)# plot hg dengan warna hitam dan lebar garis 2.0
bins = np.linspace(0, 256, 100) # menentukan jumlah variabel bins yang disikan 0 pada rentang 256, sampai 100
plt.hist(hg, bins, color="black", alpha=0.5) # buat histogram hg dengan aturan bins warna hitam dan transparansi 0.5
plt.title("Histogram")# buat tittle dengan histogram
plt.show()# tampilkan
#==========================================================================================================================================
#Menampilkan Histogram Gambar RGB
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256)) # Membuat array hgr dengan 256 nilai 0 untuk menampung histogram warna merah (red)
hgg = np.zeros((256)) # Membuat array hgg dengan 256 nilai 0 untuk menampung histogram warna hijau (green)
hgb = np.zeros((256)) # Membuat array hgb dengan 256 nilai 0 untuk menampung histogram warna biru (blue)
hgrgb = np.zeros((768)) # Membuat array hgrgb dengan 768 nilai 0 untuk menampung histogram gabungan RGB
#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): # lopp keadaan x pada kisaran 0 sampai 256
    hgr[x] = 0# untuk hgread maka 0
    hgg[x] = 0# untuk hggreen maka 0
    hgb[x] = 0# untuk hgblue maka 0
    
for x in range(0, 768): # loop untuk range x 0 sampai 768
    hgrgb[x] = 0# maka hgrgb =0
#Menghitung nilai dari gambar
for x in range(0, 256): # untuk loop range x range 0 sampai 256 dan hasilnya:
    hgr[x] = 0 # untuk hgr = 0
    hgg[x] = 0 # untuk hgg = 0
    hgb[x] = 0 # untuk hgb = 0
    
for x in range(0, 768): # loop x pada range 0 sampai 768 berlaku:
    hgrgb[x] = 0 # hgrgb bernilai 0

# th = int(256/64)
temp = [0] # Membuat variabel temp dengan nilai awal berupa list kosong.
for y in range(0, kucingturu.shape[0]):# Melakukan loop pada setiap baris gambar dengan variabel y.
    for x in range(0, kucingturu.shape[1]):# melakukan loop pada setiao gambar variabel x
        red = int(kucingturu[y][x][0]) # Mengambil nilai warna merah dari piksel gambar pada posisi (y, x) dan mengkonversinya menjadi bilangan bulat.
        green = int(kucingturu[y][x][1])# Mengambil nilai warna hijau dari piksel gambar pada posisi (y, x) dan mengkonversinya menjadi bilangan bulat.
        blue = int(kucingturu[y][x][2])# Mengambil nilai warna biru dari piksel gambar pada posisi (y, x) dan mengkonversinya menjadi bilangan bulat.
        green = green + 256 #Menambahkan nilai 256 pada nilai warna hijau
        blue = blue + 512 # Menambahkan nilai 512 pada nilai warna biru. Hal ini dilakukan untuk membedakan antara nilai warna merah, hijau, dan biru pada histogram.
# temp.append(green)
        hgrgb[red] += 1 # menambahkan nilai histogram  untuk komponen warna merah (red) dalam array hgrgb.
        hgrgb[green] += 1 # menambahkan nilai histogram untuk komponen warna hijau (green) dalam array hgrgb.
        hgrgb[blue] += 1 # menambahkan nilai histogram untuk komponen warna biru (blue) dalam array hgrgb.

binsrgb = np.linspace(0, 768, 100) # diisi aray dengan nilai 100, pada range 0 dan 768
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5) #Membuat histogram menggunakan data dengan warna hitam dan transparansi sebesar 0.5.
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")# berikan judul
plt.show()# tampilkan
#=============================================================================================================================================
for y in range(0, img_height): # loop untuk y range 0 sampai height
    for x in range(0, img_width): # loop untuk x range 0 sampai width
        red = kucingturu[y][x][0] # untuk image  chhanel 0 = red
        green = kucingturu[y][x][1]# untuk imgae chhanel 1 = green
        blue = kucingturu[y][x][2]# untuk image chanel 2 = blue
        hgr[red] += 1 # menambahkan nilai histogram  untuk komponen warna merah (red)
        hgg[green] += 1 # menambahkan nilai histogram  untuk komponen warna green (hijau)
        hgb[blue] += 1 # menambahkan nilai histogram  untuk komponen warna blue (biru)
# menampilkan histogram seperti program sebelumnyha
bins = np.linspace(0, 256, 100)# diisi nilai 100 pada 0 sampai 256
plt.hist(hgr, bins, color="red", alpha=0.5)# menampilkan histogram merah
plt.title("Histogram Red")# beri tittle
plt.show()# tampilkan
plt.hist(hgg, bins, color="green", alpha=0.5)# menampilkan histogram hijau
plt.title("Histogram Green")# beri tittle
plt.show()# tampilkan
plt.hist(hgb, bins, color="blue", alpha=0.5)# menampilkan histogram biru
plt.title("Histogram Blue")# beri tittle
plt.show()# tampilkan
#===========================================================================================================================
hgk = np.zeros((256))#hgk dan c diinisialisasi sebagai array kosong dengan panjang 256 elemen.
c = np.zeros((256)) # Mengisi setiap nilai dalam array hgk dan c dengan 0 menggunakan loop for.

for x in range(0, 256):#Melakukan loop pada setiap piksel gambar, mengambil nilai grayscale pada setiap piksel, dan menyimpan jumlah kemunculan tiap nilai grayscale pada array hgk.
    hgk[x] = 0 # Menentukan nilai kumulatif dari setiap nilai grayscale menggunakan loop for.
    c[x] = 0 # nilai chhanel = 0

for y in range(0, img_height): # untuk y pada range 0 sampai haeigh
    for x in range(0, img_width):# untuk x para range 0 sampai width
        gray = img_grayscale[y][x][0] # gray chhanel 
        hgk[gray] += 1 # increment nilai hgk untuk gray
                
c[0] = hgk[0] # menyimpan nilai awal hgk pada nilai chanel 0
for x in range(1, 256): # Looping sebanyak 255 kali, dimulai dari index 1 hingga 255
     c[x] = c[x-1] + hgk[x] # Menghitung nilai histogram grayscale kumulatif untuk setiap nilai derajat keabuan, yaitu dengan menjumlahkan nilai histogram grayscale pada nilai derajat keabuan sebelumnya dengan nilai histogram grayscale pada nilai derajat keabuan saat ini.

hmaxk = c[255] # Menyimpan nilai maksimum histogram grayscale kumulatif pada variable hmaxk, yaitu nilai pada index 255 dari array c.

for x in range(0, 256): # Looping sebanyak 256 kali, dimulai dari index 0 hingga 255.
    c[x] = 190 * c[x] / hmaxk # Menghitung nilai histogram grayscale kumulatif ternormalisasi untuk setiap nilai derajat keabuan

plt.hist(c, bins, color="black", alpha=0.5) # membuat grafik dengan warna black transparansi 0.5
plt.title("Histogram Grayscale Kumulatif") # buat title  
plt.show()# tampilkan
#=========================================================================================================================
hgh = np.zeros((256)) # membuat aray kosong untuk menyimpan hgh
h = np.zeros((256)) # mebuat array  kosong untuk h 
c = np.zeros((256))# mambuat aray kosong untuk chanel c
# semua aray diisi  256

for x in range(0, 256): # for x untuk range 0 sampai 256
    hgh[x] = 0 # hgh untuk x
    h[x] = 0 # h utnuk x#
    c[x] = 0# chanel untuk x

for y in range(0, img_height): # untuk y pada range 0 sampai haight 
    for x in range(0, img_width): # untuk 
        gray = img_grayscale[y][x][0] # untuk gray scale chanel akan sama dengan gray
        hgh[gray] += 1 #hgh gray increment
                
h[0] = hgh[0] # mengisi nilai 0 pad hgh diinisialisasi dengan 0 pada h
for x in range(1, 256): #looping x pada range 1 sampai 256
     h[x] = h[x-1] + hgh[x] # nilai h sama dengan h x-1 ditambah hgh x

for x in range(0, 256): # untuk range 0 sampai 256 
     h[x] = h[x] / img_height / img_width # untuk x = hx dibahi tinggi image dan dibagi lagi dengan lebar image

for x in range(0, 256): # untuk loop x pada range 0 sampai 256
    hgh[x] = 0 # hgh x =0
    
for y in range(0, img_height): # loop y pada range 0 sampai image high
    for x in range(0, img_width): # loop x pada range 0 sampai image width
        gray = img_grayscale[y][x][0] # img grayscale untuk chhanel c = 0
        gray = h[gray] * 255 # nilai h gray dikali 255
        hgh[int(gray)] += 1# maka hgh int gra

c[0] = hgh[0] # c0 = hgh 0 
for x in range(1, 256): # untuk range 1 sampai 256 
     c[x] = c[x-1] + hgh[x] # cx = c  aray x-1 + hgh x

hmaxk = c[255] # hmax chanel 255

for x in range(0, 256): # loop x range 0 sampai 256
    c[x] = 190 * c[x] / hmaxk # cx = 190 dikali nilai chanel x dan dibagi nilai h max

plt.hist(c, bins, color="black", alpha=0.5) # buat histogram berwarna hitam dengan ketebalan transparansi 0.5
plt.title("Histogram Grayscale Hequalisasi")# buat tittle
plt.show() # tampilkan
#=======================================================================================================================================