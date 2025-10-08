from fileIO import FileIO
from tkinter import filedialog
import pandas as pd
from operations import Operations


# Load the Folder with prompt
load = filedialog.askdirectory(title="Select the folder containing the data files")
# Call the constructor 
file = FileIO(load)
file_list = file.read_multiple() 

select = input("\n\nSelect the number of analysis you want to perform: \n1. ESR-C\n2. Self-D\n3. Cycling\n\n--> ")

if (select=="2") or (select=="3"):
    print("At the moment the feature is not available")
    raise SystemExit
else:
    print("Data Analysis Started...")


with pd.ExcelWriter("{}/ESR-C_new.xlsx".format(load), engine='openpyxl', mode='w') as writer:
    for i in file_list:
        data = FileIO.load_data(file.file_path, i)
        math = Operations(data)
        print("Processing file: {}".format(i))
        esr = math.esr()
        cap = math.capacitance() 
        df_full = pd.DataFrame({"ESR (Ohm)" : esr, "Cap (F)" : cap})
        df_full.to_excel(writer, sheet_name="{}".format(i.split("_")[1]), index=True)

# print("Analisi completata per tutti i file e grafici creati.")

    # print(f"Processing file: {i} with {data.shape[0]} rows and {data.shape[1]} columns")

# for i in tqdm(range(100)):
    # time.sleep(1)

