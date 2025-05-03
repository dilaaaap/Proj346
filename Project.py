import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from PIL import Image

#Supposedly using global variables is bad practice, but I don't know how to do it otherwise while still using buttons.
def image_flip_horiz(event):
    global img
    flip_m = np.flip(np.array(img),axis = 1)
    imgplot.set_data(flip_m)
    img = flip_m
    plt.draw()
def image_flip_vert(event):
    global img
    flip_m = np.flip(np.array(img),axis = 0)
    imgplot.set_data(flip_m)
    img = flip_m
    plt.draw()
def image_rotate(event):
    global img
    rotate_m = np.rot90(np.array(img), k=1)
    imgplot.set_data(rotate_m)
    img = rotate_m
    plt.axis('equal')  
    plt.draw()
def image_rotate_90(event):
    global img
    rotate_m = np.rot90(np.array(img), k=3)
    imgplot.set_data(rotate_m)
    img = rotate_m
    plt.axis('equal')   
    plt.draw()
def image_rotate_180(event):
    global img
    rotate_m = np.rot90(np.array(img), k=2)
    imgplot.set_data(rotate_m)
    img = rotate_m
    plt.axis('equal')    
    plt.draw()
def image_gray(event):
    global img
    gray_m = np.dot(np.array(img)[..., :3], [0.2989, 0.5870, 0.1140])
    imgplot.set_data(gray_m)
    img = gray_m
    plt.draw()
    
def image_red_filter(event):
    global img
    red_m = np.zeros_like(np.array(img))
    red_m[..., 0] = img[..., 0]
    imgplot.set_data(red_m)
    img = red_m
    plt.draw()
def image_green_filter(event):
    global img
    green_m = np.zeros_like(np.array(img))
    green_m[..., 1] = img[..., 1]
    imgplot.set_data(green_m)
    img = green_m
    plt.draw()
def image_blue_filter(event):
    global img
    blue_m = np.zeros_like(np.array(img))
    blue_m[..., 2] = img[..., 2]
    imgplot.set_data(blue_m)
    img = blue_m
    plt.draw()
def reset(event):
    global img
    img = np.asarray(Image.open('test.jpg'))
    imgplot.set_data(img)
    plt.draw()
#def image_compress(event):
    #global img
    
img = np.asarray(Image.open('test.jpg'))
#img = np.flip(img, axis=0)
#img = image_flip_horiz(img)
plt.figure(figsize=(10,10))
imgplot = plt.imshow(img)
axbhoriz = plt.axes([0.1, 0.1, 0.1, 0.075])
axbvert = plt.axes([0.2, 0.1, 0.1, 0.075])
axbrotate_90 = plt.axes([0.3, 0.1, 0.1, 0.075])
axbrotate_180 = plt.axes([0.4, 0.1, 0.1, 0.075])
axbSVDCompress = plt.axes([0.1, 0.01, 0.1, 0.075])
axbredfilter = plt.axes([0.2, 0.01, 0.1, 0.075])
axbgreenfilter = plt.axes([0.3, 0.01, 0.1, 0.075])
axbbluefilter = plt.axes([0.4, 0.01, 0.1, 0.075])     
axbreset = plt.axes([.8, 0.01, 0.1, 0.075])

bhoriz = Button(axbhoriz, 'Flip Horz')
bvert = Button(axbvert, 'Flip Vert')
brotate_90 = Button(axbrotate_90, 'Rotate 90')
brotate_180 = Button(axbrotate_180, 'Rotate 180')
breset = Button(axbreset, 'Reset')
bSVDCompress = Button(axbSVDCompress, 'SVD Compress')
bredfilter = Button(axbredfilter, 'Red Filter')
bgreenfilter = Button(axbgreenfilter, 'Green Filter')
bbluefilter = Button(axbbluefilter, 'Blue Filter')


bhoriz.on_clicked(image_flip_horiz)
bvert.on_clicked(image_flip_vert)
brotate_90.on_clicked(image_rotate_90)
brotate_180.on_clicked(image_rotate_180)
bSVDCompress.on_clicked(image_gray)
bredfilter.on_clicked(image_red_filter)
bgreenfilter.on_clicked(image_green_filter)
bbluefilter.on_clicked(image_blue_filter)

breset.on_clicked(reset)

print(img.shape)
img_gray = img.sum(2)/255**3

plt.show()