from fileIO import FileIO
import tkinter as tk
from tkinter import filedialog

load = filedialog.askdirectory(title="Select the folder containing the data files")
file = FileIO(load)
file_list = file.read_multiple()


select = input("\n\nSelect the type of analysis you want to perform: \n1. ESR-C\n2. SelfD\n")

if select=="SelfD":
    print("At the moment the feature is not available")
else:
    print("Data Analysis Started")

