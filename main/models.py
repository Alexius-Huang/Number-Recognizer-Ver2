from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import json

"""
  json - The JSON data of the image
  gray_scale_level - The level of the gray scale
  resolution_level - Resolution density 64 * 64 / 32 * 32 / 16 * 16 / 8 * 8
  status - The status of the image data

  Resolution Level table
  1. 8 * 8
  2. 16 * 16
  3. 32 * 32
  4. 64 * 64
  5. 128 * 128

  Gray Scale Level Table
  1. 8 : 0
  2. 16 : 0
  3. 32 : 0
  4. 64 : 0
  5. 128 : 0

"""
class ImageData(models.Model):
  sample_id       = models.ForeignKey(
    'ImageSample',
    on_delete = models.CASCADE,
    null = True,
    blank = True
  )
  json             = models.TextField()
  gray_scale_level = models.SmallIntegerField()
  resolution_level = models.SmallIntegerField()
  status           = models.SmallIntegerField()
  created_at       = models.DateTimeField(auto_now_add = True)
  updated_at       = models.DateTimeField()

  def __str__(self):
    return "ImageData %i - Level %i with Resolution %i" % (self.id, self.level_type, self.resolution_type)

"""
  id - not only represent the uniqueness of the data but also the reference to image filename
  number - The representing number of the image
"""
class ImageSample(models.Model):
  number     = models.SmallIntegerField()
  processed  = models.BooleanField(default = False)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField()

  def __str__(self):
    return "ImageSample %i" % self.id

