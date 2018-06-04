import pandas as pd
from collections import Counter
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

def q04_pairs_fought_the_most_battles():
    "write your solution here"
    # Ignoring records where either attacker_king or defender_king is null. Also ignoring one record where both have the same value.

