from fileIO import FileIO
import tkinter as tks
from tkinter import filedialog
import pandas as pd
import os
from operations import Operations


# Load the Folder with prompt
load = filedialog.askdirectory(title="Select the folder containing the data files")
# Call the constructor 
file = FileIO(load)
file_list = file.read_multiple()

select = input("\n\nSelect the type of analysis you want to perform: \n1. ESR-C\n2. Self-D\n--> ")

if select=="Self-D":
    print("At the moment the feature is not available")
else:
    print("Data Analysis Started")



for i in file_list:
    data = FileIO.load_data(file.file_path, i)
    math = Operations(data)
    print(f"Processing file: {i}")
    esr = math.esr()
    cap = math.capacitance()
    df_full = pd.DataFrame({"ESR (Ohm)" : esr, "Cap (F)" : cap})
    with pd.ExcelWriter("{}/ESR-C.xlsx".format(load), engine='openpyxl', mode='a') as writer:
        df_full.to_excel(writer, sheet_name="{}".format(i.split("_")[1]), index=True)

# print("Analisi completata per tutti i file e grafici creati.")

    # print(f"Processing file: {i} with {data.shape[0]} rows and {data.shape[1]} columns")

# for i in tqdm(range(100)):
    # time.sleep(1)

