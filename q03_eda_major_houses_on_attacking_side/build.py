import pandas as pd
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
plt.switch_backend('agg') 

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

def q03_eda_major_houses_on_attacking_side():
    "write your solution here"


