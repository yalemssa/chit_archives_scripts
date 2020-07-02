#/usr/bin/python3

from ast import literal_eval
import traceback
import requests
import json
from tqdm import tqdm
from utilities import utilities as u


def get_dates_from_ulan(ulan_json):
	if (results := ulan_json['results']['bindings']):
		for item in results:
			if item['Predicate']['value'] == 'http://vocab.getty.edu/ontology#estStart':
				print(item['Object']['value'])
			if item['Predicate']['value'] == 'http://vocab.getty.edu/ontology#estEnd':
				print(item['Object']['value'])

def ulan_json(ulan_uri):
	'''Downloads ULAN JSON files'''
	ulan_agent_data = requests.get(ulan_uri).json()
	return ulan_agent_data

def lcnaf_links(row, csvoutfile):
	'''Retrieves external URIs from LCNAF records'''
	suffix = '.skos.json'
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
		print(lcnaf_uri)
		print(traceback.format_exc())
	finally:
		print(row)
		csvoutfile.writerow(row)

def viaf_links(row, csvoutfile):
	'''Retrieves external URIs from VIAF records'''
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
	finally:
		print(row)
		csvoutfile.writerow(row)

def main():
	ex_ids = {'lcnaf_id': 'n79060481', 'ulan_id': '500001609', 'viaf_id': '112793769'}
	lcnaf_uri = f"http://id.loc.gov/authorities/names/{ex_ids.get('lcnaf_id')}"
	ulan_uri = f"http://vocab.getty.edu/ulan/{ex_ids.get('ulan_id')}.json"
	viaf_uri = f"http://viaf.org/viaf/{ex_ids.get('viaf_id')}.json"
	ulan_agent_data = ulan_json(ulan_uri)
	get_dates_from_ulan(ulan_agent_data)

if __name__ == "__main__":
	main()