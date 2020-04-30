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


'''
Next steps:
Write a similar script which queries SNAC and LC; maybe also ULAN? 

Do I want to actually download authority data????
What about downloading authority data for things created after the ingest




'''


'''
        self.lcnaf_property = 'P244'
        self.ulan_prop = 'P245'
        self.viaf_prop = 'P214'
        self.snac_prop = 'P3430'
'''

'''SELECT ?s ?value ?propertyLabel WHERE { ?s wdtn:P244 <http://id.loc.gov/authorities/names/n78085480> .
  ?property wikibase:propertyType wikibase:ExternalId .
  ?property wikibase:directClaim ?propertyclaim .
  ?s ?propertyclaim ?value
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }        
}'''

#different version that only gets VIAF, SNAC, ULAN, LC stuff - I think the other one is better
'''f"""SELECT ?s ?id WHERE {{{{?s wdtn:P244 <{authority_id}>
                {{?s wdt:P3430 ?id}} 
                UNION {{?s wdt:P244 ?id}}
                UNION {{?s wdt:P245 ?id}} 
                UNION {{?s wdt:P214 ?id}}}}}}"""'''

class QueryWikiData():

    def __init__(self):
        #change
        self.cnfg = u.get_config(cfg='/Users/aliciadetelich/as_tools_config.yml')
        self.headers= {'User-Agent': 'alicias-wikidata-request-script/0.0.1',
                        'From': 'alicia.detelich@yale.edu'}
        self.header_row, self.csvfile = u.opencsv(self.cnfg['input_csv'])
        self.rowcount = row_count = sum(1 for line in open(self.cnfg['input_csv']).readlines()) - 1
        self.sesh = self.setup_session()

    
    def lcnaf_query(self, authority_id):
        return f'''SELECT ?s ?value ?propertyLabel WHERE {{ ?s wdtn:P244 <{authority_id}> .
            ?property wikibase:propertyType wikibase:ExternalId .
            ?property wikibase:directClaim ?propertyclaim .
            ?s ?propertyclaim ?value
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}}}'''

    def setup_session(self):
        session = requests.Session()
        session.headers.update(self.headers)
        print(session.headers)
        return session
    
    # def read_wikidata_dump(self, fname):
    #     with bz2.open(fname, mode='rt') as f:
    #         print('reading data')
    #         f.read()
    #         print('data read')
    #         for line in f:
    #             try:
    #                 yield json.loads(line.rstrip(',\n'))
    #             except json.decoder.JSONDecodeError:
    #                 continue

    # def print_wikidata_dump(self, fpath):
    #     for record in self.read_wikidata_dump(fpath):
    #         #if 'P244' in record['claims']
    #         print(record)


    def lookup_by_lcnaf_uri(self, authority_id, result=None):
        try:
            # lcnaf_query = f"""SELECT ?s where {{?s wdtn:{self.lcnaf_property} <{authority_id}>}}"""
            lcnaf_query_string = self.lcnaf_query(authority_id)
            #move this to init variable
            req = requests.get(f"https://query.wikidata.org/sparql?query={lcnaf_query_string}&format=json", headers=self.headers)
            #print(req.text)
            json_result = json.loads(req.text)
            #pprint.pprint(json_result)
            #double check what this does = try adding an else to see what it prints
            if json_result['results']['bindings']:
                result = {item.get('s').get('value'): [f"{item.get('propertyLabel').get('value')}: {item.get('value').get('value')}" for item in json_result['results']['bindings']] for item in json_result['results']['bindings']}
        except Exception:
            print(authority_id)
            print(traceback.format_exc())
        return result

    # def lookup_by_wikidata_entity(self, wikidata_entity):
    #     data = requests.get(f'https://www.wikidata.org/entity/{wikidata_entity}.json')

    # def extract_all_uris(self, wikidata_uri, result=None):
    #   '''This only works if we already know the wikidata URI'''

    # def extract_ulan_uri(self, wikidata_uri, result=None):
    #     prefix = 'http://vocab.getty.edu/page/ulan/'

    # def extract_viaf_uri(self, wikidata_uri, result=None):
    #     prefix = 'https://viaf.org/viaf/'

    # def extract_snac_uri(self, snac_uri, result=None):
    #     prefix = 'http://n2t.net/ark:/99166/'

    def q_wikidata(self, csvoutfile):
        with tqdm(total=self.rowcount) as pbar:
            for row in self.csvfile:
                try:
                    pbar.update(1)
                    authority_id = row[2]
                    wikidata_data = self.lookup_by_lcnaf_uri(authority_id)
                    if wikidata_data is not None:
                        row.extend([list(wikidata_data.keys())[0], list(wikidata_data.values())[0]])
                    else:
                        row.append('Could not retrieve Wikidata URI')
                    #print(row)
                    csvoutfile.writerow(row)
                except Exception:
                    print(traceback.format_exc())

    def extract_wiki_data(self):
        '''This will extract data re: ULAN URIs and others from the results of the Wikidata URI query'''
        pass

@decs.time_it
def main():
    try:
        wikidated = QueryWikiData()
        #move this into the class like the input CSV
        fileobject, csvoutfile = u.opencsvout('/Users/aliciadetelich/Dropbox/git/chit_archives_scripts/data/wikidata_uris_outfile.csv')
        csvoutfile.writerow(wikidated.header_row)
        #wikidated.print_wikidata_dump('/Users/amd243/Desktop/latest-all.json.bz2')
        #maybe move this to 
        wikidated.q_wikidata(csvoutfile)
    except Exception:
        print(traceback.format_exc())
    finally:
        #does this happen even when the script is aborted by CTRL-C/Z?
        #not Z but C
        fileobject.close()
        print('All Done!')

if __name__ == "__main__":
    main()



