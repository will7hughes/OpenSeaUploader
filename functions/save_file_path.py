import os
import sys
from os import path

def save_file_path():
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "Save_gui.cloud"))
    return filepath