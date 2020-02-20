#/usr/bin/python3

import bz2
import json
import pprint
import time
import traceback

import requests
from tqdm import tqdm

from utilities import utilities as u
from utilities import decorators as decs



#if 'P244' in claims:


class QueryWikiData():

	def __init__(self):
		#change
		self.cnfg = u.get_config(cfg='/Users/amd243/as_tools_config.yml')
		self.lcnaf_property = 'P244'
		self.ulan_prop = 'P245'
		self.headers= {'User-Agent': 'alicias-wikidata-request-script/0.0.1',
						'From': 'alicia.detelich@yale.edu'}
		self.header_row, self.csvfile = u.opencsv(self.cnfg['input_csv'])
		self.rowcount = row_count = sum(1 for line in open(self.cnfg['input_csv']).readlines()) - 1
		self.sesh = self.setup_session()

	def setup_session(self):
		session = requests.Session()
		session.headers.update(self.headers)
		print(session.headers)
		return session
	
	def read_wikidata_dump(self, fname):
		with bz2.open(fname, mode='rt') as f:
			print('reading data')
			f.read()
			print('data read')
			for line in f:
				try:
					yield json.loads(line.rstrip(',\n'))
				except json.decoder.JSONDecodeError:
					continue

	def print_wikidata_dump(self, fpath):
		for record in self.read_wikidata_dump(fpath):
			#if 'P244' in record['claims']
			print(record)


	def lookup_by_lcnaf_uri(self, authority_id, result=None):
		try:
			lcnaf_query = f"""SELECT ?s where {{?s wdtn:{self.lcnaf_property} <{authority_id}>}}"""
			req = requests.get(f"https://query.wikidata.org/sparql?query={lcnaf_query}&format=json", headers=self.headers)
			#print(req.text)
			json_result = json.loads(req.text)
			#pprint.pprint(json_result)
			if json_result['results']['bindings']:
				result = json_result['results']['bindings'][0]['s']['value']
		except Exception:
			print(authority_id)
			print(traceback.format_exc())
		return result

	def lookup_by_wikidata_entity(self, wikidata_entity):
		data = requests.get(f'https://www.wikidata.org/entity/{wikidata_entity}.json')

	def extract_ulan_uri(self, wikidata_uri, result=None):
		pass

	def loop_and_lookup(self, csvoutfile):
		with tqdm(total=self.rowcount) as pbar:
			for row in self.csvfile:
				try:
					pbar.update(1)
					authority_id = row[2]
					wikidata_uri = self.lookup_by_lcnaf_uri(authority_id)
					if wikidata_uri is not None:
						row.append(wikidata_uri)
					else:
						row.append('Could not retrieve Wikidata URI')
					csvoutfile.writerow(row)
			#return [lookup_by_lcnaf_uri(row[0]) for row in self.csvfile]
				except Exception:
					print(traceback.format_exc())

	def extract_wiki_data(self):
		'''This will extract data re: ULAN URIs and others from the results of the Wikidata URI query'''
		pass

@decs.time_it
def main():
	try:
		wikidated = QueryWikiData()
		#wikidated.print_wikidata_dump('/Users/amd243/Desktop/latest-all.json.bz2')
		fileobject, csvoutfile = u.opencsvout('/Users/amd243/Dropbox/git/chit_metadata_reconciliation/data/wikidata_uris_out.csv')
		csvoutfile.writerow(wikidated.header_row)
		wikidated.loop_and_lookup(csvoutfile)
	except Exception:
		print(traceback.format_exc())
	finally:
		#does this happen even when the script is aborted by CTRL-C/Z?
		#not Z but C
		fileobject.close()
		print('All Done!')

if __name__ == "__main__":
	main()



