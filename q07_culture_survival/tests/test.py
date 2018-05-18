import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_culture_survival
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
from inspect import getfullargspec
import pandas as pd
from q07_culture_survival.build import q07_culture_survival

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

battle, character_pred = q01_feature_engineering(battles,character_predictions)
a = [q07_culture_survival(x) for x in character_predictions.culture.fillna("")]

class TestGame_of_thrones(TestCase):
    def test_GOT_args(self):
        arg = getfullargspec(q07_culture_survival).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

