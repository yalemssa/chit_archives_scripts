#/usr/bin/python3

from ast import literal_eval
import traceback
import requests
from utilities import utilities as u


header_row, csvfile = u.opencsv('/Users/aliciadetelich/Dropbox/git/chit_archives_scripts/data/wikidata_uris_outfile.csv')

for row in csvfile:
	wikidata_uri = row[4]
	external_ids = row[5]
	try:
		if wikidata_uri != "Could not retrieve Wikidata URI":
			external_id_list = literal_eval(external_ids)
			for i, item in enumerate(external_id_list):
				if 'VIAF ID' in item:
					viaf_id = item.replace('VIAF ID: ', '')
					request_url = f"http://viaf.org/viaf/{viaf_id}/justlinks.json"
					get_viaf_links = requests.get(request_url).json()
					print(f'{wikidata_uri}: {get_viaf_links}')
	except Exception:
		print(wikidata_uri)
		print(traceback.format_exc())




