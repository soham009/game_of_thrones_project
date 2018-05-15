import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_eda_major_houses_on_attacking_side
from q01_feature_engineering.build import q01_feature_engineering
from inspect import getfullargspec
import pandas as pd


battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

battle, character_pred = q01_feature_engineering(battles,character_predictions)


class TestGame_of_thrones(TestCase):
    def test_GOT_args(self):
        arg = getfullargspec(q03_eda_major_houses_on_attacking_side).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))
