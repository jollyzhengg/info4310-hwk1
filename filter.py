import pandas as pd

df = pd.read_csv('Street_Tree_List-2022-01-30_FILTERED.csv')
cols = ['TreeID', 'qSpecies', 'qLegalStatus', 'PlantDate', 'DBH', 'Latitude', 'Longitude']

updated_df = df.filter(cols)
updated_df = updated_df[updated_df['PlantDate'].isna()]

def alter_species_names(x):
  split_names = x.split('::')[-1]
  split_names = split_names.split(':')[-1]
  return split_names
updated_df['qSpecies'] = updated_df['qSpecies'].apply(alter_species_names)
updated_df.to_csv('updated_tree_list.csv', index=False)


df = pd.read_csv('updated_tree_list.csv')
species_count = df['qSpecies'].value_counts()
top_species = species_count.head(15).index
top_species_df = df[df['qSpecies'].isin(top_species)]

avg_dbh = top_species_df.groupby('qSpecies')['DBH'].mean().reset_index()
avg_dbh.to_csv('top_15_species_avg_dbh.csv', index=False)



