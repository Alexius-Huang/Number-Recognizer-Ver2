import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os.path as path
from main.models import ImageData, ImageSample
from main.helpers import image_processing as imgps
from main.helpers import utils
from PIL import Image
from sklearn import svm, metrics
from sklearn.externals import joblib
import json

# TARGETS = [ i for i in range(0, 10) ]

LEVEL = [8, 16, 32, 64, 128]
# def learn(img_dir, level):
  # NOTHING

# gray = imgps.imread_grayscale(img_dir)
# inv_gray = imgps.image_grayscale_invert(gray)
# data_array = imgps.one_dimensionalize(inv_gray)

samples = ImageSample.get_samples();

# data =
# target = 4
# for resolution_level in range(1, 6):
#   for grayscale_level in range(1, 6):
#     img_dir  = "./data/processed/level_%i/sample000016.jpg" % resolution_level
#     gray = imgps.imread_grayscale(img_dir)
#     inv_gray = imgps.image_grayscale_invert(gray)
#     data_array = imgps.one_dimensionalize(inv_gray)


# print gray
# print inv_gray

print samples