import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q09_XGBoost
from q01_feature_engineering.build import q01_feature_engineering
from q08_preprocessing.build import q08_preprocessing
from xgboost import XGBClassifier as XGBC
from inspect import getfullargspec
import pandas as pd
import numpy as np

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

battle, character_pred = q01_feature_engineering(battles,character_predictions)
death_preds = q08_preprocessing(character_pred)



X = death_preds[death_preds.actual == 0].sample(350, random_state = 62).append(death_preds[death_preds.actual == 1].sample(350, random_state = 62)).copy(deep = True).astype(np.float64)
Y = X.actual.values
tX = death_preds[~death_preds.index.isin(X.index)].copy(deep = True).astype(np.float64)
tY = tX.actual.values
X.drop(["SNo", "actual", "DateoFdeath"], 1, inplace = True)
tX.drop(["SNo", "actual", "DateoFdeath"], 1, inplace = True)

clf_xgb = XGBC(subsample=.8, colsample_bytree=.8, seed=14, max_depth=3)

auc_score, acc_score = q09_XGBoost(X,Y,tX,tY,clf_xgb)


class TestGame_of_thrones(TestCase):
    def test_GOT_args(self):
        arg = getfullargspec(q09_XGBoost).args
        self.assertEqual(len(arg), 5, "Expected argument(s) %d, Given %d" % (5, len(arg)))

    def test_read_csv_data_to_df_return_auc(self):
        self.assertGreaterEqual(np.round(auc_score,4), 0.8255, "The Expected return score does not match with the given return score")

    def test_read_csv_data_to_df_return_accuracy(self):
        self.assertGreaterEqual(np.round(acc_score,4), 0.7528, "The Expected return score does not match with the given return score")

