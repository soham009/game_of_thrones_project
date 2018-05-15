import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q01_feature_engineering
from inspect import getfullargspec
import pandas as pd

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

battle, character_pred = q01_feature_engineering(battles,character_predictions)

class TestGame_of_thrones(TestCase):
    def test_GOT_args(self):
        arg = getfullargspec(q01_feature_engineering).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (2, len(arg)))
    def test_data_to_df_return_instance(self):
        self.assertIsInstance((battle), pd.DataFrame,
                              "The Expected return type does not match with the given return type")
    def test_read_csv_data_to_df_return_shape_1(self):
        self.assertEqual(battle.shape, (38, 28), "The Expected return shape does not match with the given return shape")
    def test_read_csv_data_to_df_return_shape_2(self):
        self.assertEqual(character_pred.shape, (1946, 34), "The Expected return shape does not match with the given return shape")