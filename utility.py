import pandas as pd
import pickle
from IPython.display import display

class Utility():
	# View columns and first head_rows rows of dataset
	# This function is designed to be used within a jupyter notebook (therefore display() is used)
	def preview_dataframe(df, head_rows = 5):
		print('The dataset has {} rows and {} columns'.format(df.shape[0], df.shape[1]))
		display(df.dtypes)
		with pd.option_context('display.max_rows', None, 'display.max_colwidth', -1):
			display(df.head(head_rows))

    # Save file to pickle
	def save_pickle(obj, file_name):
		pickle.dump(obj, open(file_name, "wb"))

    # Load object from pickle
	def load_pickle(file_name):
		return pickle.load(open(file_name, "rb"))
	
	# Count number of NAs in each column of data and output verbose results
	def count_nan(df):
		for column in df.columns.tolist():
			print('"{}" has {} missing values'.format(column, df[column].isnull().sum()))
