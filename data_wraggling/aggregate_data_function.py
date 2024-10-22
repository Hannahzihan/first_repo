import pandas
import numpy
def aggregate_household_data(df):
    household_df = df.groupby('household_id').agg(
    size_hh=('person', 'count'),  
    mean_age=('age', 'mean'),     
    min_age=('age', 'min'),       
    max_age=('age', 'max'),       
    nr_children=('age', lambda x: (x < 18).sum()),
    nr_female=('female', 'sum'), 
    mean_income=('income', 'mean'),
    total_income=('income', 'sum')
    ).reset_index()
    return household_df
