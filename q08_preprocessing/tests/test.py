import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q08_preprocessing
from q01_feature_engineering.build import q01_feature_engineering

from inspect import getfullargspec
import pandas as pd


battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

battle, character_pred = q01_feature_engineering(battles,character_predictions)
data = q08_preprocessing(character_pred)


class TestGame_of_thrones(TestCase):
    def test_GOT_args(self):
        arg = getfullargspec(q08_preprocessing).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_data_to_df_return_instance(self):
        self.assertIsInstance((data), pd.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape_1(self):
        self.assertEqual(data.shape, (1946, 28), "The Expected return shape does not match with the given return shape")

