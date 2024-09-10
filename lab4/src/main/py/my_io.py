import os

def my_read( path):
    file_path = os.path.join(os.path.dirname(__file__), *path)
    return open(file_path, "r").read()

def my_write(path, writable):
    file_path = os.path.join(os.path.dirname(__file__), *path)
    return open(file_path, "w").write(writable)     
