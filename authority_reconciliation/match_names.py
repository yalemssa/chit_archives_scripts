#/usr/bin/python3

import json
import pandas as pd
from string_grouper import match_strings

def filter_mirrors(dataset):
	dataset['combined_index'] = dataset[[dataset['left_index'], dataset['right_index']]]
	print(dataset['combined_index'])
	#dataset.values.tolist().apply(sorted)
	# dataset.combined_index.sort_values().apply(lambda x: sorted(x))
	#print(dataset['combined_index'])
	# dataset['combined_index'] = dataset.apply()
	dataset.drop_duplicates(subset='combined_index')
	return dataset

def regroup_data(dataset, subset):
	# need to match on both the left index and the right index
	right_set = subset.join(dataset, on='left_index', how='left')
	# left_set = subset.join(dataset, on='right_index', how='left')
	full_set = right_set.join(dataset, on='right_index', how='left', rsuffix='_right', lsuffix='_left')
	return full_set

def main():
	cfg = json.load(open('config.json', 'r', encoding='utf-8'))
	column_to_match = input("Enter name of column to match: ")
	dataset = pd.read_csv(cfg['input_csv'])
	matches = match_strings(dataset[column_to_match])
	# excludes matches with the same index, which are by definition the same.
	match_subset = matches[matches['left_index'] != matches['right_index']]
	match_subset.to_csv(cfg['output_csv'], index=False)
	joined_subset = regroup_data(dataset, match_subset)
	joined_subset.to_csv(cfg['output_csv_2'], index=False)
	dropped_dupes = filter_mirrors(joined_subset)
	dropped_dupes.to_csv(cfg['output_csv_3'], index=False)


if __name__ == "__main__":
	main()



'''
Questions:
- How to exclude matches that are just mirror images? 
For instance, one match where the right index is 50 and left index is 20, and 
another match where the right index is 20 and the left index is 50?

'''