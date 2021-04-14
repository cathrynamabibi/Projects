

import pandas as pd
import numpy as np
import os

class Kleanit:
    ''' This class is used to clean our Telco data set '''
    def __init__(self, df):
        ''' This is a Method to initailise our df (pandas) '''
        self.df = df
    
    def drop_duplicates(self):
        ''' This method drop duplicates from our data set '''
        self.df.drop_duplicates(inplace = True)
        
    def replace_empty_string(self):
        ''' This method replaces empty string with nan '''
        self.df['TotalCharges']= self.df['TotalCharges'].replace(' ', np.nan)
        
    def cast_object_to_float(self):
        ''' This method casts the dtype from object to float '''
        self.df['TotalCharges'] =  self.df['TotalCharges'].astype(float)
    
    