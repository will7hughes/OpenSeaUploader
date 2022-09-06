import tkinter
import pickle
from tkinter import filedialog
from functions.save_file_path import save_file_path

class JsonPath:
    def __init__(self, text, root):
        # Upload Folder Input Button
        self.path = property(self.get_path, self.set_path)
        self.upload_folder_input_button = tkinter.Button(root, width=50, height=1,  text=text, command=self.prompt_path)
        self.upload_folder_input_button.grid(row=21, column=0, columnspan=2, padx=2)
        try:
            with open(save_file_path(), "rb") as infile:
                new_dict = pickle.load(infile)
                self.set_path(new_dict[0])
        except FileNotFoundError:
            pass
    
    def get_path(self):
        return self.path

    # ask for directory on clicking button, changes button name.
    def prompt_path(self):
        self.set_path(filedialog.askdirectory())

    def set_path(self, path):
        self.path = path
        self.upload_folder_input_button["text"] = path

    def get_end(self):
        f_end_len = len("/src")
        f_end = self.path[-f_end_len:]
        return f_end

    