import NewareNDA
import numpy as np
import pandas as pd
import os

class FileIO:

    def __init__(self, file_path):
        '''
        Initialize the FileIO class with the path to the NDA file.
        :param file_path: Path to the NDA file.
        '''
        self.file_path = file_path

    def read_data(self):
        '''
        Read single data from the NDA file using NewareNDA library.
        :return: Data read from the NDA file.
        '''
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")        
        try:
            # Read single data using NewareNDA library --> Specifically .ndax files
            data = NewareNDA.NewareNDAx.read_ndax(self.file_path)
            return data
        except Exception as e:
            raise IOError(f"An error occurred while reading the file: {e}")
        
    def read_multiple(self):
        '''
        Read multiple data sets from the NDA file using NewareNDA library.
        :return: List of data sets read from the NDA file.
        '''
        data_list = []
        try:
            for i in data_list:
                data_list.append(i)
            # Read multiple data sets using NewareNDA library --> Specifically .ndax files
            return data_list
        except Exception as e:
            raise IOError(f"An error occurred while reading the files in the folder: {e}")
        

    # def save_to_csv(self, data, output_path):
    #     try:
    #         df = pd.DataFrame(data)
    #         df.to_csv(output_path, index=False)
    #         print(f"Data successfully saved to {output_path}")
    #     except Exception as e:
    #         raise IOError(f"An error occurred while saving to CSV: {e}")