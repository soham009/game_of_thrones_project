# A bit of preprocessing

We quickly convert non-numeric categorical features to numeric. Then we drop some columns and replace missing values with -1.


## Write a function `q08_preprocessing` that :
- Will take the dataset and apply the previous function to the culture column and factorize (using pandas factorize function) the title,culture,mother,father,house,heir and spouse columns.
- Drop the following columns as we dont need that "name", "alive", "pred", "plod", "isAlive", "dateOfBirth".
- And replace the "." and "_" with empty spaces to columns and fill NA in dataframe with -1 values.
 
### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| variable_1 | dataframe | compulsory |  | Data to be loaded |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable_1 | pandas.Dataframe | Dataframe with above operations inculcated |
