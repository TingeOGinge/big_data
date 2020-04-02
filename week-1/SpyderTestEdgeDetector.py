import matplotlib.pyplot as plt
from skimage import feature, io, data
#please note that this programme does not work
'''check the error messages and comment out certain lines with # or ' '''
#ValueError: The parameter `image` must be a 2-dimensional array
#if you have any problem let me know it - Dalin

img1 = data.camera()
io.imshow(img1)
io.show()

img2 = data.astronaut()
io.imshow(img2)
io.show()

sig1=3
sig2=1

edges11 = feature.canny(img1)
edges12 = feature.canny(img1, sigma=sig1)

edges21 = feature.canny(img2[:,:,0])
edges22 = feature.canny(img2[:,:,0], sigma=sig2)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True)

ax1.imshow(img1, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges11, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges12, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()