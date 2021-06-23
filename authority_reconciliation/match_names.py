#/usr/bin/python3

from collections import defaultdict
import json
import pandas as pd
from string_grouper import match_strings
import csv


def remove_subfields(dataset):
	new_dataset = dataset[dataset['sort_name_left'].str.contains('\$') == False]
	new_new_dataset = new_dataset[new_dataset['sort_name_right'].str.contains('\$') == False]
	return new_new_dataset

def filter_mirrors(dataset):
	dataset['combined_index'] = list(zip(dataset.left_index, dataset.right_index))
	dataset['sorted_index'] = dataset['combined_index'].apply(sorted)
	dataset['sorted_index'] = dataset['sorted_index'].apply(tuple)
	dataset.drop(columns='combined_index', inplace=True)
	dataset.drop_duplicates(subset='sorted_index', inplace=True)
	return dataset

def regroup_data(dataset, subset):
	# need to match on both the left index and the right index
	right_set = subset.join(dataset, on='left_index', how='left')
	# left_set = subset.join(dataset, on='right_index', how='left')
	full_set = right_set.join(dataset, on='right_index', how='left', rsuffix='_right', lsuffix='_left')
	return full_set

def merge_datasets(cfg):
	dataset_1 = pd.read_csv(cfg['input_csv'])
	dataset_2 = pd.read_csv(cfg['input_csv_1'])
	new_set = pd.merge(dataset_1, dataset_2, how='left', on='index')
	new_set.to_csv(cfg['output_csv'])


def dupes_from_as(cfg):
	column_to_match = 'name_concat'
	dataset = pd.read_csv(cfg['input_csv'])
	matches = match_strings(dataset[column_to_match])
	# excludes matches with the same index, which are by definition the same.
	match_subset = matches[matches['left_index'] != matches['right_index']]
	match_subset.to_csv(cfg['output_csv'], index=False)
	joined_subset = regroup_data(dataset, match_subset)
	joined_subset.to_csv(cfg['output_csv_2'], index=False)
	dropped_dupes = filter_mirrors(joined_subset)
	dropped_dupes.to_csv(cfg['output_csv_3'], index=False)
	dropped_subfields = remove_subfields(dropped_dupes)
	dropped_subfields.to_csv(cfg['output_csv_4'], index=False)

def dupes_from_wikidata(cfg):
	wikidata_sublist = prep_wikidata_sublist(cfg)
	for key, value in wikidata_sublist.items():
		master_match = pd.DataFrame([key], columns=['agent_uri', 'name_concat'])
		master_match.set_index('agent_uri', inplace=True)
		dupe_match = pd.DataFrame(value, columns=['index', 'num_matches', 'agent_uri', 'aay_url', 'name_concat', 'sort_name', 'dates', 'resources', 'archival_objects', 'accessions', 'authority_id', 'source', 'create_time', 'wikidata_uri', 'wikidata_name', 'wikidata_begin', 'wikidata_end'])
		dupe_match.set_index('index', inplace=True)
		matches = match_strings(master_match['name_concat'], dupe_match['wikidata_name'])
		matches.to_csv(cfg.get('output_csv'), mode='a', header=False, index=False)

def prep_wikidata_sublist(cfg):
	sublist = defaultdict(list)
	with open(cfg.get('input_csv'), 'r', encoding='utf8') as infile:
		csvfile = csv.reader(infile)
		for row in csvfile:
			# the key is a tuple with the URI and matched name
			sublist[(row[2], row[4])].append(row)
	return sublist


def main():
	cfg = json.load(open('config.json', 'r', encoding='utf-8'))
	merge_datasets(cfg)
	#dupes_from_wikidata(cfg)





if __name__ == "__main__":
	main()


'''
Questions:
- How to exclude matches that are just mirror images? 
For instance, one match where the right index is 50 and left index is 20, and 
another match where the right index is 20 and the left index is 50?

'''