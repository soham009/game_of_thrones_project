# Feature Engineering

We have already loaded the data for you, you have to start with the feature engineering part by creating new feature as follows:

- defender_count – Number of major houses on defending side
- attacker_count – Number of major houses on attacking side
- att_comm_count – Number of commanders on attacking side
- no_of_books – Number of books a character appeared in

## Write a function `q01_feature_engineering` that :
- Takes Dataframe then in a new column it will give the overall count for the defender, attacker, commanders and character appeared in number of books.
- Return the DataFrame

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| variable_1 | dataframe | compulsory |  | Dataframe to be loaded |
| variable_2 | dataframe | compulsory |  | Dataframe to be loaded |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable_1 | pandas.Dataframe | Dataframe with above operations inculcated |
| variable_2 | pandas.Dataframe | Dataframe with above operations inculcated |


Note- 
1. For this you need to subtract the number of columns with 4 (there are total 4 columns each) to obtain defender and attacker count.
2. For more reference click (here)[https://www.kaggle.com/mylesoneill/game-of-thrones]
