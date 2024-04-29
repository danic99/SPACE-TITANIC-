import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
import re
from sklearn.preprocessing import StandardScaler



def boleano(x):
    if x == 'True':
        return 1
    elif x == 'False':
        return 0
    




def cabina(x):
    deck = x.split("/")[0]
    ##number = int(x.split("/")[1])
    side =  x.split("/")[1]
    if side == 'P' and deck == 'A':
                     return 'grupo 1 babor'
    elif  side == 'S' and deck == 'A':
                     return 'grupo 1 Estribor'
    elif side == 'P' and deck == 'B':
                     return 'grupo 2 babor'
    elif  side == 'S' and deck == 'B':
                     return 'grupo 2 Estribor'
    
    elif side == 'P' and deck == 'C':
                     return 'grupo 3 babor'
    elif  side == 'S' and deck == 'C':
                     return 'grupo 3 Estribor'
    
    elif side == 'P' and deck == 'D':
                     return 'grupo 4 babor'
    elif  side == 'S' and deck == 'D':
                     return 'grupo 4 Estribor'
    
    elif side == 'P' and deck == 'E':
                     return 'grupo 5 babor'
    elif  side == 'S' and deck == 'E':
                     return 'grupo 5 Estribor'
    
    elif side == 'P' and deck == 'F':
                     return 'grupo 6 babor'
    elif  side == 'S' and deck == 'F':
                     return 'grupo 6 Estribor'
    

    elif side == 'P' and deck == 'G':
                     return 'grupo 7 babor'
    elif  side == 'S' and deck == 'G':
                     return 'grupo 7 Estribor'
    
    elif side == 'P' and deck == 'T':
                     return 'grupo 8 babor'
    elif  side == 'S' and deck == 'T':
                     return 'grupo 8 Estribor'
    


