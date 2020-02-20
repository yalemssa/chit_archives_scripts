#/usr/bin/python3


import itertools
import string

from fuzzywuzzy import fuzz
import unidecode

from utilities import utilities as u

'''Functions for identifying potential duplicate agent records'''


def strip_punc(title):
	'''Strips punctuation for matching. Good for exact string matches, less so for
	matches i.e. Gore, Al and Albert Gore'''
	title = row[0]
    no_punc = title.translate(str.maketrans({key: None for key in string.punctuation}))
    no_punc = no_punc.translate(str.maketrans('', '', string.whitespace))
    no_punc = no_punc.lower()
    no_punc = unidecode.unidecode(no_punc)
    row.append(no_punc)
    return row


def matcher(input_file):
	'''This is the basic fuzzy matching process - it compares every row in the
	input file with every other row, and 

	Assumes that name to compare is in first column. Not sure if I can use
	csvdict with combinations'''
	match_list = []
	#not sure if I can use enumerate() with combinations
	identifier = 0
	for a, b in itertools.combinations(input_file, 2):
		identifier+=1
		ratio = fuzz.ratio(a[0], b[0])
		if ratio > 98:
			#could also do a side by side comparison but this is easier to see
			matchlist.append([identifier, ratio] + a)
			matchlist.append([identifier, ratio] + b)
	return match_list
