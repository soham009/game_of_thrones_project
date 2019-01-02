# %load q02_eda_major_death/build.py
import pandas as pd
import numpy as np
import sys,os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

def q02_eda_major_death(battles):
    ax = battles[['major_death','major_capture']].plot(kind='bar',title ='', figsize=(15, 10), legend=True)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('No of Death/Capture Event', fontsize=12)
    plt.show()
    return


