import pandas as pd
import numpy as np
from tqdm import tqdm

class Operations:

    def __init__(self, data):
        '''
        Initialize the Math class. The Constructor stores the data to be processed.
        '''
        self.data = data # Most likely this is going to be a pandas dataframe because loaded with NewareNDA lib

    def esr_old (self):
        '''
        Method to calculate the Equivalent Series Resistance (ESR) from the data.
        In general, ESR is calculated as the difference between the voltage at the start of the discharge and the voltage
        Ask Pietro Agola or Alessandro Fabbri for the routine details
        This method is totally wrong because it uses the last rest of the cycle. We actually need the values from the 
        rest before the first discharge
        '''
        # look for the number of cycles
        ncycles = self.data['Cycle'].unique()
        print("{}ESR Calculations running...{}".format(bcolors.WARNING,bcolors.ENDC))
        self.esr = []
        # filter only rest values
        # rest_data = self.data.loc[self.data['Status'] == 'Rest']
        for i in tqdm(ncycles):
            # filter only discharge values at certain cycle
            # self.dsch_data = self.data.loc[(self.data['Status'] == 'CC_DChg') & (self.data['Cycle'] == i)]
            # A solid reference point is the column Step_index in the NDAX file. We could use that for referencing First Discharge Cycle and Rest            
            self.filter_cycle = self.data.loc[self.data['Cycle'] == i]
            # First Step Discharge Step Index
            self.first_dsch = self.filter_cycle.loc[self.filter_cycle['Step_Index'] == 4]             
            self.mid_rest = self.filter_cycle.loc[self.filter_cycle['Step_Index'] == 5]
            self.v_end_dsch = self.first_dsch['Voltage'].iloc[-1]
            self.v_end_rest = self.mid_rest['Voltage'].iloc[-1]
            self.current = abs(self.first_dsch['Current(mA)'].iloc[-1])
            self.esr_value = (self.v_end_rest - self.v_end_dsch)/(self.current/1000) # in Ohm 
            self.esr.append(self.esr_value)

        print("{}Success!!!{}".format(bcolors.OKGREEN, bcolors.ENDC))

        return self.esr
    
    def esr (self):
        '''
        Method to calculate the Equivalent Series Resistance (ESR) from the data.
        In general, ESR is calculated as the difference between the voltage at the start of the discharge and the voltage
        Ask Pietro Agola or Alessandro Fabbri for the routine details
        new esr --> this is the correct method. Ask Mattia Colalongo or Pietro Agola about this
        '''
        # look for the number of cycles
        ncycles = self.data['Cycle'].unique()
        print("{}ESR Calculations running...{}".format(bcolors.WARNING,bcolors.ENDC))
        self.esr = []
        # filter only rest values
        # rest_data = self.data.loc[self.data['Status'] == 'Rest']
        for i in tqdm(ncycles):
            # filter only discharge values at certain cycle
            # self.dsch_data = self.data.loc[(self.data['Status'] == 'CC_DChg') & (self.data['Cycle'] == i)]
            # A solid reference point is the column Step_index in the NDAX file. We could use that for referencing First Discharge Cycle and Rest            
            self.filter_cycle = self.data.loc[self.data['Cycle'] == i]
            # First Step Discharge Step Index
            self.first_dsch = self.filter_cycle.loc[self.filter_cycle['Step_Index'] == 4]             
            self.mid_rest = self.filter_cycle.loc[self.filter_cycle['Step_Index'] == 3]
            self.v_init_dsch = self.first_dsch['Voltage'].iloc[0]
            self.v_end_rest = self.mid_rest['Voltage'].iloc[-1]
            self.current = abs(self.first_dsch['Current(mA)'].iloc[0])
            self.esr_value = (self.v_end_rest - self.v_init_dsch)/(self.current/1000) # in Ohm 
            self.esr.append(self.esr_value)

        print("{}Success!!!{}".format(bcolors.OKGREEN, bcolors.ENDC))

        return self.esr

    def capacitance(self):
        '''
        Function that calculates the capacitance out of the ESR-C tests. Any question should be directed to 
        Pietro Agola or Alessandro Fabbri
        '''
        ncycles = self.data['Cycle'].unique()
        print("{} Capacitance Calculations Running...{}".format(bcolors.WARNING, bcolors.ENDC))
        self.cap = []
        # for i in tqdm(ncycles):
        for i in tqdm(ncycles):
            # filter only discharge values at certain cycle
            # self.dsch_data = self.data.loc[(self.data['Status'] == 'CC_DChg') & (self.data['Cycle'] == i)]
            # A solid reference point is the column Step_index in the NDAX file. We could use that for referencing First Discharge Cycle and Rest            
            self.filter_cycle = self.data.loc[self.data['Cycle'] == i] # filter per no. cycle
            self.first_dsch = self.filter_cycle.loc[self.filter_cycle['Step_Index'] == 4] # filter only first discharge
            self.v_init = self.first_dsch['Voltage'].iloc[0] # select the first voltage value
            self.v_end = self.first_dsch['Voltage'].iloc[-1] # select the last voltage value
            self.v_ic = 0.8 * self.v_init + 0.2 * self.v_end # v_init_computed is a new value a bit more down to the discharge
            self.close_v = abs(self.first_dsch['Voltage'] - self.v_ic) # we subtract the computed value to the voltage series --> we look for the closest values
            # as the v_ic does not exist in the series

            self.close_v_idx = np.argmin(self.close_v) # get the index value of the closest V value in the df from the computed one
            self.cap_id = self.first_dsch['Discharge_Capacity(mAh)'].iloc[self.close_v_idx] # new initial capacity close to v_ic
            self.v_id = self.first_dsch['Voltage'].iloc[self.close_v_idx] # new initial voltage close to v_ic (voltage computed)               
            self.cap_end = self.first_dsch['Discharge_Capacity(mAh)'].iloc[-1] # end capacity at the end of the discharge
            self.capacitance = 3600/1000 * (self.cap_end - self.cap_id)/(self.v_id - self.v_end) # C = Q/ΔV
            # above 3600 is s/h and 1000 is from mA to A. We could multiply for 3.6 and done
            self.cap.append(self.capacitance)
        print("{}Success!!!{}".format(bcolors.OKGREEN, bcolors.ENDC))
        
        return self.cap

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