import pandas as pd

df = pd.read_csv("filename.csv")

df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'},
          inplace=True)

# filter by value
filtered_df = df.locp[df['column_name'] == 2020]

# filter by value in list
filtered_df = df.loc[df['column_name'].isin(['Sunday', 'Saturday'])]

# combining data filters: & --> and , | --> or
filtered_df = df[(df['column_name1']>2020) & (df['column_name2'] != "Sunday")]

# assign a new name to keep the original dataframe intact.
df_dropped = df.drop(columns=['column_name1', 'column_name2'])
