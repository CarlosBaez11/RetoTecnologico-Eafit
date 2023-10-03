#!/usr/bin/env/ python3
import pandas as pd
class filter_dataset(pd.DataFrame):
    
    """filter_columns : Used to filter columns in the dataset, takes as input a list
        filter_values : used to filter columns based on specific values, passed as kwargs"""
    def __init__(self, path=None, *args, **kwargs):
        super().__init__()
        self.args=args
        self.data=pd.read_excel(path)
        
    def filter_columns(self, columns):
        self.data=self.data[columns]
        return self.data
    def filter_values(self, **kwargs):
        for i, j in kwargs.items():
            self.data=self.data[self.data[str(i)].isin(j)]
        return self.data

        
        