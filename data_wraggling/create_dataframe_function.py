import pandas as pd
import numpy as np
def create_dataframe():
    # Create a DataFrame
    data = {
        'household_id': [37, 37, 37, 241, 242, 155789, 155789, 155789],
        'person': [1, 2, 3, 1, 1, 1, 2, 3],
        'age': [20, 19, 19, 50, 29, 58, 61, 15],
        'income': [10000, 5300, 4700, 90000, 20000, 5000, 110000, np.nan],
        'female': [False, True, False, True, False, False, True, False]
    }
    #Turn Dictionary into DataFrame
    df = pd.DataFrame(data)
    return df