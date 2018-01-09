import pandas as pd

class Utility():
    # Define function to view columns and first 5 rows of dataset
    # This function is designed to be used within a jupyter notebook (therefore display() is used)
    def preview_dataframe(df, head_rows = 5):
        print('The dataset has {} rows and {} columns'.format(df.shape[0], df.shape[1]))
        display(df.dtypes)
        with pd.option_context('display.max_rows', None, 'display.max_colwidth', -1):
            display(df.head(head_rows))
