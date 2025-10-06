from fileIO import FileIO
import tkinter as tk
from tkinter import filedialog

load = filedialog.askdirectory(title="Select the folder containing the data files")
file = FileIO(load)
print(file)

