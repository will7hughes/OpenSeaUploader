from tkinter import Label
import pickle
from tkinter import filedialog
from functions.info import info
from functions.log import log
from functions.warn import warn
from functions.save_file_path import save_file_path
from classes.InputEntry import InputEntry

input_save_list = ["NFTs folder :", 0, 0, 0, 0, 0, 0, 0, 0, 0]

class InputField():
    def __init__(self, label, row_io, column_io, pos, min, max, input_type, master, invalid_message="Invalid Input Field", txt_width=60):
        super().__init__()

        self.master = master

        self.min = min
        self.max = max
        self.input_type = input_type        
        self.invalid_message = invalid_message

        # Valid/Invalid Commands
        valid_command = (self.master.register(self.validate), '%P')
        invalid_command = (self.master.register(self.on_invalid),)

        self.input_field = InputEntry(self.master, self.input_type, width=txt_width)
        self.input_field.config(validate='focusout', validatecommand=valid_command, invalidcommand=invalid_command)
        self.input_field.grid(ipady=3)
        self.input_field.label = Label(master, text=label, anchor="w", width=20, height=1 )
        self.input_field.label.grid(row=row_io, column=column_io, padx=12, pady=2)
        
        self.input_field.grid(row=row_io, column=column_io + 1, columnspan=2, padx=12, pady=2)

        try:
            with open(save_file_path(), "rb") as infile:
                new_dict = pickle.load(infile)
                self.insert_text(new_dict[pos])
        except FileNotFoundError:
            info("!Exception: File Not Found", "InputField class __init__ threw an exception")
            pass

    def insert_text(self, text):
        self.input_field.delete(0, "end")
        self.input_field.insert(0, text)

    def save_inputs(self, pos):
        input_save_list.insert(pos, self.input_field.get())
        with open(save_file_path(), "wb") as outfile:
            pickle.dump(input_save_list, outfile)
    
    def show_message(self, message='', color='black'):
        self.input_field['foreground'] = color

    # Input Validation
    def on_invalid(self):
        on_invalid_message = "Invalid Input [ " + str(self.input_field.get()) + " ] " + self.invalid_message

        if type(self.input_field.get()) != self.input_type:
            on_invalid_message = on_invalid_message + " \n\tType should be ( " + str(self.input_type) + " ) \n\tInstead it was ( " + str(type(self.input_field.get())) + " )"
        
        self.show_message(on_invalid_message, 'red')
        log(on_invalid_message)
        info(on_invalid_message)
        return False

    def validate(self, value):
        try:
            input_field_value = self.input_field.get()
        except:
            input_field_value = value

        input_field_type = type(input_field_value)
        if input_field_type is self.input_type:
            if input_field_type is str and (input_field_value == 0 or (input_field_value).isdigit() == True or len(input_field_value) > self.max or len(input_field_value) < self.min):
                return False
            elif input_field_type is int and (input_field_value > self.max or input_field_value < self.min):
                return False
            elif input_field_type is float and (input_field_value > self.max or input_field_value < self.min):
                return False
            else:
                # Resets the input text field to valid
                self.show_message()
                return True
        else:
            return False

