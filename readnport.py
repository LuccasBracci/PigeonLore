'''
 Just imports dependancies in one package 
'''

import numpy as np
import pandas as pd
from google.colab import drive
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_selector, make_column_transformer
  
drive.mount('/content/drive')


def dfRead(filepath):
  global df 
  df = pd.read_csv(filepath)