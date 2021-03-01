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