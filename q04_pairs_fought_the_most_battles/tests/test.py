import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_pairs_fought_the_most_battles
from q01_feature_engineering.build import q01_feature_engineering
from inspect import getfullargspec
import pandas as pd


battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

battle, character_pred = q01_feature_engineering(battles,character_predictions)


lis = q04_pairs_fought_the_most_battles(battle)

class TestGame_of_thrones(TestCase):
    def test_GOT_args(self):
        arg = getfullargspec(q04_pairs_fought_the_most_battles).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_data_to_df_return_instance(self):
        self.assertIsInstance((lis), list,
                              "The Expected return type does not match with the given return type")
