from os import path

def image_path():
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "/src/images"))
    return filepath