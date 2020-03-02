#/usr/bin/python3


import itertools
import string

from fuzzywuzzy import fuzz
from tqdm import tqdm
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


def matcher(input_file, output_file):
    '''This is the basic fuzzy matching process - it compares every row in the
    input file with every other row, and 

    Assumes that name to compare is in first column. Not sure if I can use
    csvdict with combinations'''
    #match_list = []
    #not sure if I can use enumerate() with combinations
    identifier = 0
    #for a, b in tqdm(itertools.combinations(input_file, 2)):
    for a, b in tqdm(itertools.combinations(input_file, 2)):
        ratio = fuzz.ratio(a[2], b[2])
        if ratio > 98:
            identifier+=1
            #could also do a side by side comparison but this is easier to see
            output_file.writerow([identifier, ratio] + a)
            output_file.writerow([identifier, ratio] + b)
            #print([identifier, ratio] + a)
            #print([identifier, ratio] + b)
        #return match_list

def main():
    try:
        header_row, csvfile = u.opencsv()
        fileobject, csvoutfile = u.opencsvout()
        matcher(csvfile, csvoutfile)
    finally:
        fileobject.close()


if __name__ == "__main__":
    main()
