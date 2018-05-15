# Which pairs fought the most battles?

We need to know Which pair of houses fought against each other. 

## Write a function `q04_pairs_fought_the_most_battles` that :
- Will take "attacker_king" and "defender_king" columns and Use Counter function to create a list of tuple
- Convert the list into pandas Dataframe and plot a bar graph.
- and return the list that got from the first step

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| variable_1 | dataframe | compulsory |  | Dataframe to be loaded |


### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable_1 | list | List of names of king on attacker side and on defender side |


Note-
- Your graph should look somewhat like this [Image](../images/q04_pairs_fought_the_most_battles.png)
Start step:
- eg. list(Counter([tuple(set(x)) for x in battles.dropna(subset=["attacker_king", "defender_king"])[
        ["attacker_king", "defender_king"]].values if len(set(x)) > 1]).items())
