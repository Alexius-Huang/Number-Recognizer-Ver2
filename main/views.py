from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import ImageData, ImageSample
from .helpers import image_processing as imgps
from .helpers import machine_learning as ml

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os.path as path

SAMPLE_DIR = './data/samples/'
CALIBRATE_DIR = './data/calibrated/'
PROCESS_DIR = './data/processed/'

def index(request):
  view = {'test': 'Hello World1'}
  return render(request, 'main/index.html', view)

def feed(request):
  post = request.POST
  imgData = post['imgURL']
  imgID = str(ImageSample.objects.count() + 1).zfill(6)
  filename = path.join(SAMPLE_DIR, "sample%s.jpg" % imgID)
  if imgData.startswith("data:image/jpeg;base64,"):
    imgData = imgData[len("data:image/jpeg;base64,"):]
    with open(filename, "wb") as fh:
      fh.write(imgData.decode('base64'))

    # Calibrate sample and save it
    c_filename = path.join(CALIBRATE_DIR, "sample%s.jpg" % imgID)
    gray = imgps.imread_grayscale(filename)
    c_img = imgps.calibrate_image_array(gray)
    imgps.save_image(c_img, 'gray', c_filename)

    # Processing the Image
    imgps.generate_processed_image(c_filename, "sample%s.jpg" % imgID)

    # Create ImageSample Record
    sample = ImageSample(number = post['number'], created_at = timezone.now(), updated_at = timezone.now())
    sample.save()

    return JsonResponse(dict(message = "success"))
  
  else:
    return JsonResponse(dict(message = "error"))

