import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os.path as path
from main.helpers import image_processing as imgps
from PIL import Image

img_dir = './data/calibrated/sample000013.jpg'
gray = imgps.imread_grayscale(img_dir)

LEVEL = [8, 16, 32, 64, 128]

def generate_processed_image(img_dir):
  for resolution_level, resolution in enumerate(LEVEL):
    save_directory = './data/processed/level_%i' % (resolution_level + 1)
    filename = path.join(save_directory, 'sample.jpg')

    img = Image.open(img_dir)
    img = img.resize((resolution, resolution), Image.ANTIALIAS)
    img.save(filename)

  # Get the size of the image
  # size = np.shape(gray)
  # height = size[0]
  # width  = size[1]

def generate_grayscale_level_array(imgID):

# img = Image.open(img_dir)
# img = img.resize((8, 8), Image.ANTIALIAS)
# img.save('test.jpg')

# gray = imgps.imread_grayscale('test.jpg')
# plt.imshow(gray, cmap='gray')
# plt.show()

# print(gray)