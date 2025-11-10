from fileIO import FileIO
from tkinter import filedialog
import pandas as pd, numpy as np
from operations import Operations


# Load the Folder with prompt
load = filedialog.askdirectory(title="Select the folder containing the data files")
# Call the constructor 
file = FileIO(load)
file_list = file.read_multiple() 

user = input("\nSelect the User name: \n1. Cristina\n2. Raffaele\n3. Valentina\n4. Batman\n5. IlSignoreOscuro\n\n--> ")


if user=="1":
    print("Hello Cristina, welcome back!\n")
    select = input("\nSelect the number of analysis you want to perform: \n1. ESR-C\n2. Self-D\n3. Cycling\n4. RP\n5. Floating\n\n--> ")

    if (select=="2"):
        print("At the moment the feature is not available")
        input("Press Enter to exit...")
        raise SystemExit
    else:
        print("Data Analysis Started...")


    if select=="1":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/ESR-C_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                esr = math.esr()
                cap = math.capacitance() 
                df_full = pd.DataFrame({"ESR (Ohm)" : esr, "Cap (F)" : cap})
                df_full.to_excel(writer, sheet_name="{}".format(i.split("_")[1]), index=True)

    elif select=="3":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/Cycling_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                cap = math.cycling()
                df_full = pd.DataFrame({'Cycle' : np.array(cap)[:,0], "Capacitance (F)" : np.array(cap)[:,1], 'ESR (Ohm)': np.array(cap)[:,2]})
                df_full.to_excel(writer, sheet_name="{}".format(i.split("_")[1]), index=True)

    elif select=="4":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/RP_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                rp_values = math.rp()
                df_full = pd.DataFrame({'Cycle' : np.array(rp_values)[:,0], "Capacitance (F)" : np.array(rp_values)[:,1], 'ESR (Ohm)': np.array(rp_values)[:,2]})
                df_full.to_excel(writer, sheet_name="{}".format(i.split("_")[1]), index=True)

    elif select=="5":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/Floating_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                rp_values = math.floating()
                df_full = pd.DataFrame({'Cycle' : np.array(rp_values)[:,0], "Capacitance (F)" : np.array(rp_values)[:,1], 'ESR (Ohm)': np.array(rp_values)[:,2]})
                df_full.to_excel(writer, sheet_name="{}".format(i.split("_")[1]), index=True)
                # df_full.to_excel(writer, sheet_name="{}".format(i), index=True)

    else:
        print("Invalid Selection. Exiting...")
        input("Press Enter to exit...")
        raise SystemExit


    input("Script Ended. Press Enter to exit...")





elif user=="2":
    print("Hello Raffaele, I hope you are doing well!\n")
    select = input("\nSelect the number of analysis you want to perform: \n1. ESR-C\n2. Self-D\n3. Cycling\n4. RP\n5. Floating\n\n--> ")

    if (select=="2"):
        print("At the moment the feature is not available")
        input("Press Enter to exit...")
        raise SystemExit
    else:
        print("Data Analysis Started...")


    if select=="1":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/ESR-C_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                esr = math.esr()
                cap = math.capacitance() 
                df_full = pd.DataFrame({"ESR (Ohm)" : esr, "Cap (F)" : cap})
                sheet_label = i.split("_")[1:3]
                sheet_name = "_".join(sheet_label)
                df_full.to_excel(writer, sheet_name="{}".format(sheet_name), index=True)

    elif select=="3":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/Cycling_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                cap = math.cycling()
                df_full = pd.DataFrame({'Cycle' : np.array(cap)[:,0], "Capacitance (F)" : np.array(cap)[:,1], 'ESR (Ohm)': np.array(cap)[:,2]})
                sheet_label = i.split("_")[1:3]
                sheet_name = "_".join(sheet_label)
                df_full.to_excel(writer, sheet_name="{}".format(sheet_name), index=True)

    elif select=="4":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/RP_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                rp_values = math.rp()
                df_full = pd.DataFrame({'Cycle' : np.array(rp_values)[:,0], "Capacitance (F)" : np.array(rp_values)[:,1], 'ESR (Ohm)': np.array(rp_values)[:,2]})
                sheet_label = i.split("_")[1:3]
                sheet_name = "_".join(sheet_label)
                df_full.to_excel(writer, sheet_name="{}".format(sheet_name), index=True)

    elif select=="5":
        # Create a Pandas Excel writer using openpyxl as the engine
        with pd.ExcelWriter("{}/Floating_new_v2.xlsx".format(load), engine='openpyxl', mode='w') as writer:
            for i in file_list:
                data = FileIO.load_data(file.file_path, i)
                math = Operations(data)
                print("Processing file: {}".format(i))
                rp_values = math.floating()
                df_full = pd.DataFrame({'Cycle' : np.array(rp_values)[:,0], "Capacitance (F)" : np.array(rp_values)[:,1], 'ESR (Ohm)': np.array(rp_values)[:,2]})
                sheet_label = i.split("_")[1:3]
                sheet_name = "_".join(sheet_label)
                df_full.to_excel(writer, sheet_name="{}".format(sheet_name), index=True)
                # df_full.to_excel(writer, sheet_name="{}".format(i), index=True)

    else:
        print("Invalid Selection. Exiting...")
        input("Press Enter to exit...")
        raise SystemExit


    input("Script Ended. Press Enter to exit...")   


elif user in ["3", "4", "5"]:
    print("Hello User {}, this application is currently under development for you. Please contact Cristina for more information.".format(user))
    input("Press Enter to exit...")
    raise SystemExit
