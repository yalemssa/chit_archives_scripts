#/usr/bin/python3

from collections import Counter
from tqdm import tqdm
from utilities import utilities as u

header_row, csvfile = u.opencsv()
fileobject, csvoutfile = u.opencsvout()

headers = header_row + ['count']

csvoutfile.writerow(headers)

record_links = [row for row in csvfile]
agent_uris = [row[2] for row in record_links]
agent_uri_count = Counter(agent_uris)

output = [row + [agent_uri_count[row[2]]] for row in tqdm(record_links) if row[2] in agent_uri_count]

csvoutfile.writerows(output)

fileobject.close()



