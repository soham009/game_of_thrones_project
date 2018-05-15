# XGB Classifier

- Now its time to apply a machine learning algorithm, we have split the data for you.

## Write a function `q09_XGBoost` that :
- Will take the model and fit on X, Y and predict the probabilities of test data.
- return the Roc and AUC score along with the accuracy.

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| variable_1 | dataframe | compulsory |  | X data |
| variable_2 | dataframe | compulsory |  | Y data |
| variable_3 | dataframe | compulsory |  | Xtest data |
| variable_4 | dataframe | compulsory |  | Ytest data |
| variable_5 | dataframe | compulsory |  | model |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable_1 | float | Auc Roc score |
| variable_2 | float | Accuracy |
