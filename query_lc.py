#/usr/bin/python3


import json
import pprint
import requests
import traceback
from tqdm import tqdm
from utilities import utilities as u


def query_lc(csvfile, csvoutfile):
	suffix = '.skos.json'
	for row in csvfile:
		try:
			lcnaf_uri = row[2]
			request_uri = f'{lcnaf_uri}{suffix}'
			send_requests = requests.get(request_uri).json()
			for item in send_requests:
				if "@id" in item:
					if item["@id"] == lcnaf_uri:
						if 'http://www.w3.org/2004/02/skos/core#exactMatch' in item:
							exact_matches = [ex['@id'] for ex in item.get('http://www.w3.org/2004/02/skos/core#exactMatch')]
						else:
							exact_matches = []
						if 'http://www.w3.org/2004/02/skos/core#closeMatch' in item:
							close_matches = [close['@id'] for close in item.get('http://www.w3.org/2004/02/skos/core#closeMatch')]
						else:
							close_matches = []
						row.extend([exact_matches, close_matches])
		except Exception:
			print(traceback.format_exc())
		finally:
			print(row)
			csvoutfile.writerow(row)


def main():
	try:
		header_row, csvfile = u.opencsv('/Users/aliciadetelich/Dropbox/git/chit_archives_scripts/data/all_lc_agent_uris.csv')
		fileobject, csvoutfile = u.opencsvout('/Users/aliciadetelich/Dropbox/git/chit_archives_scripts/data/lc_data.csv')
		csvoutfile.writerow(header_row)
		query_lc(csvfile, csvoutfile)
	except Exception:
		print(traceback.format_exc())
	finally:
		fileobject.close()

if __name__ == "__main__":
	main()