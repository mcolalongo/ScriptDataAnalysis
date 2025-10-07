import pandas as pd
import numpy as np


class Operations:

    def __init__(self, data):
        '''
        Initialize the Math class. The Constructor stores the data to be processed.
        '''
        self.data = data # Most likely this is going to be a pandas dataframe because loaded with NewareNDA lib


    def ESR (self):
        print(self.data['Cycle'])