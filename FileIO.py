import NewareNDA
import numpy as np
import pandas as pd
import os

class FileIO:

    def __init__(self, file_path):
        '''
        Initialize the FileIO class with the path to the NDA file.
        :param file_path: Path to the NDAx folder files.
        '''
        self.file_path = file_path
        

    def read_multiple(self):
        '''
        Read multiple data sets from the NDA file using NewareNDA library.
        :return: List of data sets read from the NDA file.
        '''
        data_list = [] # Create an empty list to store all the NDAx files
        
        try:
            # Loop through all the files in the specified directory and selecto only NDAx
            for i in os.listdir(self.file_path):
                if i.endswith('.ndax'):
                    data_list.append(i)
            # Cool print to see all the NDAx files in the folder
            print(f"{bcolors.BOLD}Files in the folder:{bcolors.ENDC}")
            [print("{} File Name {} --> {}".format(bcolors.OKCYAN,bcolors.ENDC,data_list[i])) for i in range(len(data_list))]
            # Return the data list
            return data_list
        
        except:
            raise IOError(f"An error occurred while reading the files in the folder {self.file_path}")



    def load_data(self, single_path):
        '''
        Read single data from the NDA file using NewareNDA library.
        :return: Data read from the NDA file.
        '''
        try:
            # Read single data using NewareNDA library --> Specifically .ndax files
            data = NewareNDA.NewareNDAx.read_ndax("{}/{}".format(self,single_path))
            return data
        except:
            raise IOError(f"An error occurred while reading the file: {single_path}")

# Cool colors for printing in terminal
class bcolors:
    '''
    Class for terminal text colors
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'