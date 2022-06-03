import pandas as pd
from random import randint

def random_n_hashtags(hashtags, n=3):
	# select n random hashtags and return them in a list
	return [ hashtags[ randint(0, len(hashtags)-1) ] for i in range(n) ]


def setup():
	
	wanted_hashtags = [f'wanted_{i}' for i in range(3)]
	noise_hashtags = [f'garbage_{i}' for i in range(10)]

	all_ht = wanted_hashtags + noise_hashtags
	n_rows = 10
	
	hashtags_series = pd.Series([random_n_hashtags(all_ht) for i in range(n_rows)])
	
	column_1 = pd.Series([f'tweet: {i}' for i in range(n_rows)])
	column_2 = pd.Series([f'c2_r{i}' for i in range(n_rows)])
	df = pd.DataFrame({'ids': column_1, 
			   'hashtags': hashtags_series, 
			   'third_column': column_2})
	return df, wanted_hashtags


def solution(df, wanted_hashtags):
	wanted_set = set(wanted_hashtags)

	# This function finds the size of the intersection of 
	# the two sets. Here, `x` will be one entry in the `hashtags` pandas.Series.
	# It means 
	filter_wanted = lambda x: len(set(x).intersection(wanted_set)) 
	
	# pd.apply: applies the whole function to each element in the array.
	are_there_matches = df.hashtags.apply(filter_wanted)

	# boolean pair-wise operation: the `> 0` is applied to each element, 
	# returning an array of the same size.
	bool_matches = are_there_matches > 0
	# Use boolean array to select a subset of your DataFrame. 
	# This works because: df.shape[0] == bool_matches.size
	new_df = df[bool_matches]

	# we write the next line because
	# it stops the interpreter and allows you to 
	# inspect the variable objects which together make the solution.
	import idpb; ipdb.set_trace()

	# Returned the dataset without tweets that do not have at least
	# 1 "wanted" hashtag.
	return new_df
	

	

def main():
	df, matches = setup()
	df = solution(df, matches)

if __name__ == '__main__':
	main()
