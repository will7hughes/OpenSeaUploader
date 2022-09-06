import tkinter

class InputEntry(tkinter.Entry):
    def __init__(self, parent, input_type, **kwargs):
        self.input_type = input_type
        super().__init__(parent, **kwargs)

    # Override the get
    # Used for our custom type checking system in InputField.input_field, validate, on_invalid
    # Tries to cast the value based on the input_type
    # If it fails to cast, then it just returns the value without casting
    # This way we can prompt the user that the Type is wrong without getting a bunch of ugly errors
    def get(self):
        try:
            input_value = self.input_type(super().get())
        except:
            input_value = super().get()
        return input_value