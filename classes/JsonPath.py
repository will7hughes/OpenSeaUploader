import tkinter
import pickle
from tkinter import filedialog
from functions.save_file_path import save_file_path

class JsonPath:
    def __init__(self, text, root):
        # Upload Folder Input Button
        self.upload_folder_input_button = tkinter.Button(root, width=50, height=1,  text=text, command=self.prompt_path)
        self.upload_folder_input_button.grid(row=21, column=0, columnspan=2, padx=2)
        try:
            with open(save_file_path(), "rb") as infile:
                new_dict = pickle.load(infile)
                self.set_path(new_dict[0])
        except FileNotFoundError:
            pass
    
    def get_path(self):
        return self.__path

    # ask for directory on clicking button, changes button name.
    def prompt_path(self):
        self.__path = filedialog.askdirectory()
        self.set_path(self.__path)

    def set_path(self, path):
        self.__path = path
        self.upload_folder_input_button["text"] = path

    path = property(get_path, set_path)