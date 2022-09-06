import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from classes.InputField import InputField
from classes.JsonPath import JsonPath

# Main Tkinter Panel
root = Tk()
root.geometry('750x850')
root.resizable(False, False)
root.title("NFT Uploader")

# Input Objects
collection_link_input = InputField("OpenSea Collection Link:", 2, 0, 1, 1, 200, str, root, 'Collection link required, check your format. Should start with https://opensea.io/collection/. Insert your collection name. Then should end in /assets/create. Example: https://opensea.io/collection/willow-away/assets/create')
description_credit_input = InputField("Description Credit:", 3, 0, 2, 0, 100000, str, root, "Description Credit is invalid")
description_footer_input = InputField("Description Footer:", 4, 0, 3, 0, 100000, str, root, "Description Footer is invalid")
start_num_input = InputField("Start Number:", 5, 0, 4, 1, 1000, int, root, "Start Number should be a number between 1 and 999")
end_num_input = InputField("End Number:", 6, 0, 5, 1, 3000, int, root, "End Number should be greater than Start Number and less than (Start Number) + 1000")
price = InputField("Default Price:", 7, 0, 6, 0.001, 100, float, root, "Price required")
file_format = InputField("NFT Image Format:", 8, 0, 7, 1, 100, str, root, "File format required - png, jpg, jpeg, gif")
external_link = InputField("External link:", 9, 0, 8, 0, 300, str, root, "External link is not formatted correctly")

json_path = JsonPath("Add NFTs Upload Folder", root)


    