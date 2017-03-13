from django.core.management.base import BaseCommand, CommandError
from main.models import ImageSample, ImageData
from subprocess import call
import os

class Command(BaseCommand):
  help = 'Clearing all of the samples in data folder'

  # def add_arguments(self, parser):
    # NOTHING

  def handle(self, *args, **options):
    SAMPLE_DIR = './data/samples'
    CALIBRATED_DIR = './data/calibrated'
    PROCESSED_DIR = './data/processed'

    sample_filelist = [ os.path.join(SAMPLE_DIR, file) for file in os.listdir(SAMPLE_DIR) if file.endswith(".jpg") ]
    for file in sample_filelist:
      os.remove(file)

    calibrated_filelist = [ os.path.join(CALIBRATED_DIR, file) for file in os.listdir(CALIBRATED_DIR) if file.endswith(".jpg") ]
    for file in calibrated_filelist:
      os.remove(file)

    for i in range(1, 6):
      sub_dir = os.path.join(PROCESSED_DIR, "level_%i" % i)
      processed_filelist = [ os.path.join(sub_dir, file) for file in os.listdir(sub_dir) if file.endswith(".jpg") ]
      for file in processed_filelist:
        os.remove(file)

    # Refresh Database
    call(['python', 'manage.py', 'flush'])