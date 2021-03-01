Mimin di beri gambar sama member tapi kok panjang bener :( Bisa bantu perbaiki gaaak

Downloads : https://mega.nz/#!shIzQILI!KjNEUTHRFkxOpbQQw5gEacpJ-qKcRNlI6mCM_LZxbD0

Referensi : https://stackoverflow.com/questions/53755910/how-can-i-split-a-large-image-into-small-pieces-in-python

Python Code:

```
import cv2
img = cv2.imread('panjangbet.png')

#split image per 350px
for r in range(0,img.shape[0],350):
    ke=1
    for c in range(0,img.shape[1],350):
        cv2.imwrite(f"{ke}.png",img[r:r+1, c:c+350,:])
        ke+=1

# join object img cv
all_image = []
for r in range(1,351):
    im = cv2.imread(f'{r}.png')
    all_image.append(im)

# merge semua gambar jadi 1
im_v = cv2.vconcat(all_image)
cv2.imwrite('hasil.png', im_v)
```

Flag:
```
CTFR{n0w_y0u_l34rn1n9_4b0ut_ch4n93_1m4g3_sc4l3}
```