#import library
import numpy as np # import library numpy
import cv2 # import library cv2
import matplotlib.pyplot as plt # import library matplotlib dari python

# read gambar dari path file
kucingturu = cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\mengantuk.jpg")
# mendapatkan resolusi dan data type dari gambar mulai dari tinggi, lebar, channel, dan type
img_height = kucingturu.shape[0] # insialisasi variabel berisi tinggi gambar 
img_width = kucingturu.shape[1]  # inisialisasi variabel berisi lebar gambar
img_channel = kucingturu.shape[2] # inisialisasi variabel berisi chanel warna
img_type = kucingturu.dtype # variabel untuk jenis data type

# membuat variabel dengan resolusi dan tipe yang disamakan dengan gamber
img_flip_horizontal = np.zeros(kucingturu.shape, img_type) # inisialisasi variabel berisi flip horizontal dengan mengisi aray sesuai ukuran image dikosongkan
img_flip_vertical = np.zeros(kucingturu.shape, img_type)# inisialisasi variabel berisi flip vertikal dengan mengisi aray sesuai ukuran image dikosongkan

# membalik gambar secara horizontal, dengan membalik posisi titik x dimana x adalah sumbu piksel horizontal
for y in range(0, img_height): # perulangan sumbu y untuk ukuran dari 0 sampai ke img_height(tinggi)
    for x in range(0, img_width): #  perulangan sumbu x utuk ukuran dari 0 sampai ke img_width(lebar)
        for c in range(0, img_channel): # perulangan c untuk ukuran dari 0 sampai ke img_channel(warna)
            img_flip_horizontal[y][x][c] = kucingturu[y][img_width-1-x][c] # untuk image flip horizontal digunakan perubahan nilai x dengan fungsi img_width-1-x (yang seharusnya aray x value di baca dari kiri ke kanan, menjadi terbalik)

# membalik gambar secara vertikal dengan membalik posisi sumbu y dimana sumbu y adalah sumbu vertikal dari sistem kordinat9 (array)
for y in range(0, img_height): # perulangan sumbu y untuk ukuran dari 0 dampai ke img_height(tinggi)
    for x in range(0, img_width): #  perulangan sumbu x utuk ukuran dari 0 sampai ke img_width(lebar)
        for c in range(0, img_channel): # perulangan c untuk ukuran dari 0 sampai ke img_channel(warna)
            img_flip_vertical[y][x][c] = kucingturu[img_height-1-y][x][c] # untuk image flip horizontal digunakan perubahan nilai y dengan fungsi img_width-1-y (yang seharusnya aray y value di baca dari atas ke bawah, menjadi terbaik)

# menampilkan figure dengan plot gambar berisi gambar asli, gambar flip horizontal, dan gambar flip vertikal nrow srandard yaitu 1 dan ncols berisi 3 jadi plot akan berisi gambar 3 menyamping
fig, axs = plt.subplots( ncols=3, figsize=(12,8))

axs[0].imshow(kucingturu) # tampilkan gambar ori
axs[0].set_title('image asli') # set tittle gambar ori
axs[0].axis('off') # ubah sumbu menjadi off agar tidak ada ukuran skala
axs[1].imshow(img_flip_horizontal) # tampilkan gambar  hasil flip horizontal
axs[1].set_title('Flip Horizontal') # set tittle denga flip horizontal
axs[1].axis('off') # ubah sumbu menjadi off agar tidak ada ukuran skala
axs[2].imshow(img_flip_vertical) # tampilkan gambar hasil flip vertical
axs[2].set_title('flip Vertical')# beri tittle flip vertical
axs[2].axis('off')# ubah sumbu menjadi off agar tidak ada ukuran skala
# tampilkan gambar
plt.show()
