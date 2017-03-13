from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import ImageData, ImageSample
from .helpers import image_processing as imgps
from .helpers import machine_learning as ml
from .helpers import utils

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os.path as path
import json

SAMPLE_DIR = './data/samples/'
CALIBRATE_DIR = './data/calibrated/'
PROCESS_DIR = './data/processed/'
LEVEL_ARR = [ 2 ** (2 + i) for i in range(1, 6) ]

def index(request):
  view = {'test': 'Hello World1'}
  return render(request, 'main/index.html', view)

def feed(request):
  post = request.POST
  imgData = post['imgURL']
  serial = ImageSample.objects.count() + 1
  imgID = str(serial).zfill(6)
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
    sample = ImageSample(
      serial = serial,
      number = post['number'],
      created_at = timezone.now(),
      updated_at = timezone.now()
    )
    sample.save()

    return JsonResponse(dict(message = "success"))
  
  else:
    return JsonResponse(dict(message = "error"))

def generate_data(request):
  post = request.POST
  if post['ajax'] == 'true':
    try:
      samples = ImageSample.objects.filter(processed = False)
    except (KeyError, ImageSample.DoesNotExist):
      return JsonResponse(dict(message = "no data"))
    else:
      if len(samples) == 0:
        return JsonResponse(dict(message = "no data"))

      # Generating the data of the sample
      result = []
      for sample in samples:
        sampleID = sample.id
        serial = str(sample.serial).zfill(6)
        target = sample.number

        for resolution_level in range(1, 6):
          for grayscale_level in range(1, 6):
            img_dir = "./data/processed/level_%i/sample%s.jpg" % (resolution_level, serial)
            gray = imgps.imread_grayscale(img_dir)
            inv_gray = imgps.image_grayscale_invert(gray)
            data_arr = imgps.one_dimensionalize(inv_gray)

            for index, grayscale in enumerate(data_arr):
              data_arr[index] = int(np.round(grayscale / 255.0 * LEVEL_ARR[grayscale_level - 1]))

            json_data = json.dumps(data_arr.tolist())

            create_data = ImageData(
              sample_id        = sample,
              json             = json_data,
              grayscale_level  = grayscale_level,
              resolution_level = resolution_level,
              status           = 0,
              created_at       = timezone.now(),
              updated_at       = timezone.now()
            )
            create_data.save()

            sample.processed  = True
            sample.updated_at = timezone.now()
            sample.save()
      
      return JsonResponse(dict(message = 'success'))