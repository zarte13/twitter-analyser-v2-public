from operator import index
from unittest.mock import sentinel
import pandas as pd
import numpy as np
import csv
import os, os.path



DIR = './daytweetsoutput'
nfiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

for number in range(nfiles):
    df = pd.read_csv(f'daytweetsoutput/v3tweetsentiment-{number}.csv')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    
    mean = df[['sentiment']].mean(axis=0, numeric_only = True)
    print(mean)

