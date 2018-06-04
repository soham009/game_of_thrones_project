import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style("white")

import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

def q06_battles_on_each_region():
    "write your solution here"

