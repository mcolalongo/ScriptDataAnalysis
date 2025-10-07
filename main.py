from fileIO import FileIO
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
import time, os
from math import Math


# Load the Folder with prompt
load = filedialog.askdirectory(title="Select the folder containing the data files")
# Call the constructor 
file = FileIO(load)
file_list = file.read_multiple()
print(file)

select = input("\n\nSelect the type of analysis you want to perform: \n1. ESR-C\n2. SelfD\n--> ")

if select=="SelfD":
    print("At the moment the feature is not available")
else:
    print("Data Analysis Started")


for i in file_list:
    data = FileIO.load_data(file.file_path, i)
    math = Math(data)
    math.ESR()

    # print(f"Processing file: {i} with {data.shape[0]} rows and {data.shape[1]} columns")

# for i in tqdm(range(100)):
    # time.sleep(1)

