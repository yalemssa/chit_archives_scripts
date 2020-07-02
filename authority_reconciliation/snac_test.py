#/usr/bin/python3


import json
import pprint
import requests
import traceback
from tqdm import tqdm
from utilities import utilities as u

'''This is really similar to the query_wikidata class; maybe combine somehow?'''


class QuerySnac():

    def __init__(self):
        self.cnfg = u.get_config(cfg='/Users/aliciadetelich/as_tools_config.yml')
        self.header_row, self.csvfile = u.opencsv(self.cnfg['input_csv'])
        self.rowcount = row_count = sum(1 for line in open(self.cnfg['input_csv']).readlines()) - 1
        self.api_url = 'http://api.snaccooperative.org/'
        self.headers = {'Content-type': 'application/json','Accept': 'text/plain'}
        self.q = {'command': 'read','sameas': 'lcnaf_uri'}

    def q_snac(self, csvoutfile):
        with tqdm(total=self.rowcount) as pbar:
            for row in self.csvfile:
                try:
                    pbar.update(1)
                    self.q['sameas'] = row[2]
                    send_query = requests.put(self.api_url, data=json.dumps(self.q), headers=self.headers).json()
                    if 'constellation' in send_query:
                        ark = send_query.get('constellation').get('ark')
                        same_as = send_query.get('constellation').get('sameAsRelations')
                        uris = [item.get('uri') for item in same_as]
                        row.extend([ark, uris])
                        #print(row)
                        csvoutfile.writerow(row)
                except Exception:
                    print(row[2])
                    print(traceback.format_exc())

def main():
    try:
        snac_query = QuerySnac()
        fileobject, csvoutfile = u.opencsvout('/Users/aliciadetelich/Dropbox/git/chit_archives_scripts/data/snac_uris_outfile.csv')
        csvoutfile.writerow(snac_query.header_row)
        snac_query.q_snac(csvoutfile)
    except Exception:
        print(traceback.format_exc())
    finally:
        fileobject.close()
        print('All Done!')

if __name__ == "__main__":
    main()



'''
[

{'dataType': 'SameAs', 
'type': {'id': '28225', 'term': 'sameAs', 
'uri': 'http://socialarchive.iath.virginia.edu/control/term#sameAs', 'type': 'record_type'}, 
'text': 'Whittelsey, Chauncey, 1783-1834', 
'uri': 'http://viaf.org/viaf/68890090', 'id': '6149401', 'version': '888548'}, 

{'dataType': 'SameAs', 
'type': {'id': '28225', 'term': 'sameAs', 'uri': 'http://socialarchive.iath.virginia.edu/control/term#sameAs', 'type': 'record_type'}, 
'uri': 'http://www.worldcat.org/wcidentities/lccn-nr2006006487', 
'id': '6149402', 
'version': '888548'}, 

{'dataType': 'SameAs', 
'type': {'id': '28225', 'term': 'sameAs', 'uri': 'http://socialarchive.iath.virginia.edu/control/term#sameAs', 'type': 'record_type'}, 
'uri': 'http://id.loc.gov/authorities/names/nr2006006487', '
id': '6149403', 
'version': '888548'}]
'''