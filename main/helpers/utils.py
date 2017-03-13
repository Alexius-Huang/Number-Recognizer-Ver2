import os

def get_filelist(dir, file_prefix = ""):
  return [ os.path.join(dir, file) for file in os.listdir(dir) if file.endswith(file_prefix) ]
