import pandas as pd

people_df = pd.read_excel('people.xlsx')
animals_df = pd.read_excel('animals.xlsx')

# result for 1
people_table = people_df.rename(columns={'ID': 'personid', 'Name': 'personname', 'Age': 'personage'})

# result for 2
animals_table = animals_df.rename(columns={'ID': 'animalsid', 'Name': 'animalsname', 'Age': 'animalsage'})

# result for 3
people_with_animals = people_table.merge(animals_table, left_on='personid', right_on='Owner_ID')

# result for 4
df4 = people_df

# used for 10
temp_df = people_table.merge(animals_table, left_on='personid', right_on='Owner_ID', how='left')
people_without_animals = temp_df[pd.isnull(temp_df['Owner_ID'])]

# result for 5
df5 = people_with_animals['personname'].unique()

# result for 6
df6 = people_with_animals.loc[people_with_animals['personname'] == 'Ido']['animalsid']

# result for 7
df7 = people_with_animals.loc[people_with_animals['personage'] >= 20]['personid'].unique()

# result for 8
df8 = people_with_animals.loc[people_with_animals['personage'] >= 30]['personid']

# result for 9
df9 = people_with_animals.loc[
    (people_with_animals['Gender'] == 'F') &
    ((people_with_animals['Type'] == 'dog') | (people_with_animals['Type'] == 'cat'))]['personname']

# result for 10
df10 = people_without_animals.loc[people_without_animals['Gender'] == 'M']

# result for 11
df11 = people_with_animals.loc[
    (people_with_animals['Gender'] == 'F') &
    (people_with_animals['Color'] == 'white')]['Birthdate']

# result for 12
df12 = people_with_animals.loc[people_with_animals['personage'] >= 21]['Color'].unique()

# result for 13
df13 = people_without_animals['personname']

# result for 14
df14 = people_with_animals.loc[
    (people_with_animals['Gender'] == 'F') &
    (people_with_animals['animalsage'] >= 3) &
    (people_with_animals['Color'] != 'black')]

# result for 15
df15 = people_with_animals.loc[
    people_with_animals['personname'] == people_with_animals['animalsname']
]

# result for 16
df16 = people_with_animals.loc[
    people_with_animals['personid'] == people_with_animals['animalsid']
]



# result for 21
df21 = animals_table.sort_values('animalsage', ascending=False)

# result for 22
df22 = animals_table.sort_values('animalsage', ascending=False).head()

# result for 29
df29 = people_with_animals.sort_values('animalsage', ascending=False).groupby('personid').head(1)

# result for 30
df30 = animals_table.groupby('Type')['animalsage'].mean()\
    .to_frame().rename(columns={'animalsage': 'average_animal_age'})\
    .sort_values('average_animal_age', ascending=False).head(1)