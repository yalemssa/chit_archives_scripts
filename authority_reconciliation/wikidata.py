#/usr/bin/python3

import csv
from dataclasses import dataclass
import json
import traceback

from fuzzywuzzy import fuzz
import requests
from tqdm import tqdm

from utilities import utilities as u


@dataclass
class AgentData():
    '''Creates an agent object from a CSV row'''
    __slots__ = ['agent_uri', 'agent_aay_url', 'name_concat', 'authority_id', 'dates', 'source', 'resource_ids',
                    'archival_object_ids', 'accession_ids', 'digital_object_ids', 'event_ids', 'create_time', 'entity_id']
    agent_uri: str
    agent_aay_url: str
    name_concat: str
    authority_id: str
    dates: str
    source: str
    resource_ids: str
    archival_object_ids: str
    accession_ids: str
    digital_object_ids: str
    event_ids: str
    create_time: str
    entity_id: str

    def property_id(self):
        #this is supposed to get around the default values/slots issue, but not sure if it's good thing to do
        id_properties = {'LCNAF': 'P244', 'ULAN': 'P245', 'VIAF': 'P214', 'SNAC': 'P3430'}
        return id_properties.get(self.source)

    def label_query(self):
        '''This is just a substring match. Could potentially add other filters to narrow or broaden results'''
        return f"""SELECT ?item ?label ?dob ?dod
                    WHERE {{ SERVICE wikibase:mwapi
                    {{
                        bd:serviceParam wikibase:endpoint "www.wikidata.org";
                                        wikibase:api "Generator";
                                        mwapi:generator "search";
                                        mwapi:gsrsearch "inlabel:{self.name_concat}";
                                        mwapi:gsrlimit "max".
                        ?item wikibase:apiOutputItem mwapi:title.
                                                                    }}
                        
                        ?item wdt:P31 wd:Q5;
                          rdfs:label ?label;
                        OPTIONAL {{ ?item wdt:P569 ?dob .}}
                        OPTIONAL {{ ?item wdt:P570 ?dod .}}
                        FILTER(CONTAINS(?label, "{self.name_concat}")).
                        FILTER(LANG(?label) = "en").}}
                        """

    def identifier_query(self):
        '''Retrieves other external identifiers using an external ID - VIAF, LCNAF, ULAN, SNAC'''
        return f'''SELECT ?s ?value ?propertyLabel WHERE {{ ?s wdtn:{self.property_id()} <{self.authority_id}> .
            ?property wikibase:propertyType wikibase:ExternalId .
            ?property wikibase:directClaim ?propertyclaim .
            ?s ?propertyclaim ?value
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}}}'''

    def identifier_query_by_entity(self):
        '''Retrieves external identifiers using the wikidata entity ID '''
        return f'''SELECT DISTINCT ?value ?propertyLabel WHERE {{
            ?property wikibase:propertyType wikibase:ExternalId .
            ?property wikibase:directClaim ?propertyclaim .
            <{self.entity_id}> ?propertyclaim ?value
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}}}'''

@dataclass
class ConfigData():
    '''Creates a config object from a JSON file with assorted file methods'''
    __slots__ = ['snac_api_url', 'wikidata_user_agent', 'wikidata_user_agent_email', 'input_csv', 'output_csv', 'backup_directory']
    snac_api_url: str
    wikidata_user_agent: str
    wikidata_user_agent_email: str
    input_csv: str
    output_csv: str
    backup_directory: str

    def wikidata_headers(self):
        return {'User-Agent': self.wikidata_user_agent,
                        'From': self.wikidata_user_agent_email}

    def open_input_csv(self):
        '''This way you can't get fieldnames from the fieldnames function.'''
        with open(self.input_csv) as data:
            reader = csv.DictReader(data)
            for row in reader:
                yield row

    def open_output_csv(self):
        #this returns a fileobject (that you have to close manually) and the csvoutfile object
        fileob = open(self.output_csv, 'a', encoding='utf-8', newline='')
        csvout = csv.writer(fileob)
        return (fileob, csvout)

    def row_count(self):
        '''Returns a count of rows in a CSV file, minus the header row'''
        return len([row for row in u.opencsv(self.input_csv)[1]])

    def header_row(self):
        '''Returns the header row of the input CSV as a list'''
        with open(self.input_csv) as f:
            return f.readline().split(', ')

def setup_session(config_data):
    session = requests.Session()
    session.headers.update(config_data.wikidata_headers())
    return session

def generate_agents(cnfg):
    '''This returns a list of a bunch of data objects representing the agents in a CSV file'''
    return (AgentData(row['agent_uri'], row['agent_aay_url'], row['name_concat'], row['authority_id'], row['dates'], row['source'],
                        row['resource_ids'], row['archival_object_ids'], row['accession_ids'], row['digital_object_ids'], row['event_ids'], 
                        row['create_time'], row['entity_id'])
                    for row in cnfg.open_input_csv())

def get_query_string(agent_data, search_type):
    '''Used this inner function instead of using a series if if/else statements'''
    def get_query(search_type):
        return {'NAME': agent_data.label_query, 'ID': agent_data.identifier_query
                , 'ENTITY': agent_data.identifier_query_by_entity}.get(search_type)
    query_function = get_query(search_type)
    return query_function()

def run_query(wikidata_sesh, agent_data, search_type):
    query_string = get_query_string(agent_data, search_type)
    try:
        json_result = wikidata_sesh.get(f"https://query.wikidata.org/sparql?query={query_string}&format=json").json()
        if json_result['results']['bindings']:
            return json_result['results']['bindings']
        else:
            return 'NO RESULTS'
    #change this at some point
    except Exception:
        print(agent_data.name_concat)
        print(traceback.format_exc())
        return 'ERROR'

def process_external_id_results(json_result, agent_data, no_value):
    '''Processes the external results list into a dictionary'''
    return {item.get('s', no_value).get('value'): {item.get('propertyLabel', no_value).get('value'): item.get('value', no_value).get('value') 
                                            for item in json_result} 
                for item in json_result}

def process_name_results(json_result, agent_data, no_value):
    '''Processes the name results list into a dictionary'''
    return {agent_data.name_concat: {item.get('item', no_value).get('value'): 
                            [item.get('label').get('value'), item.get('dob', no_value).get('value')[:4], item.get('dod', no_value).get('value')[:4]] 
                                for item in json_result}}

def process_results(json_result, agent_data, search_type):
    if isinstance(json_result, list):
        no_value = {'value': 'NONE'}
        if search_type in ('ID', 'ENTITY'):
            return process_external_id_results(json_result, agent_data, no_value)
        elif search_type == 'NAME':
            return process_name_results(json_result, agent_data, no_value)
    else:
        return {agent_data.authority_id: {'NO_RESULT': [json_result]}}

def write_name_results(json_result, agent_data, csv_outfile):
    '''Make two spreadsheets - one for under 94 one for 95 and up'''
    new_rows = [[str(len(json_values.items())), 
                ratio_num,
                agent_data.agent_uri,
                agent_data.agent_aay_url,
                agent_data.name_concat, 
                agent_data.dates, 
                agent_data.resource_ids,
                agent_data.archival_object_ids,
                agent_data.accession_ids,
                agent_data.digital_object_ids,
                agent_data.event_ids,
                agent_data.create_time,
                key] + value
                for json_values in json_result.values()
                for key, value in json_values.items()
                if (ratio_num := fuzz.ratio(agent_data.name_concat, value[0])) > 94
                    ]
    csv_outfile.writerows(new_rows)

def filter_authorities(json_result, id_types):
    '''Takes the larger dictionary of authority identifiers and filters out for VIAF, LCNAF, SNAC, and ULAN'''
    #returns [('VIAF ID', '54011237'), ('Library of Congress authority ID', 'nr92016389'), ('SNAC Ark ID', 'w6dz0vgt')]
    filtered_dict = {id_type: id_value for auth_id, identifiers in json_result.items()
                        for id_type, id_value in identifiers.items() if id_type in id_types}
    return [list(json_result.keys())[0], filtered_dict.get('VIAF ID', 'NONE'), filtered_dict.get('Library of Congress authority ID', 'NONE'),
                     filtered_dict.get('SNAC Ark ID', 'NONE'), filtered_dict.get('ULAN ID', 'NONE')]

def write_external_id_results(json_result, agent_data, csv_outfile):
    '''Writes external identifiers to a CSV file'''
    '''Make these configurable, remove from code'''
    id_types = ['Library of Congress authority ID', 'VIAF ID', 'SNAC Ark ID', 'ULAN ID']
    filtered_authorities = filter_authorities(json_result, id_types)
    #add full URI?
    new_row = [agent_data.agent_uri, agent_data.name_concat, agent_data.dates] + filtered_authorities
    csv_outfile.writerow(new_row)

def write_to_file(json_result, agent_data, search_type, csv_outfile):
    '''Retrieves the correct writer function and executes it'''
    def get_writer(search_type):
        '''Retrieves the correct writer function, depending on the selected search type'''
        return {'NAME': write_name_results, 'ID': write_external_id_results,
                'ENTITY': write_external_id_results}.get(search_type)
    if json_result is not None:
        result_writer = get_writer(search_type)
        result_writer(json_result, agent_data, csv_outfile)

def lookup_agents(row_total, session_data, agent_data, csv_outfile):
    search_type = input('Enter NAME, ID, or ENTITY to select your query: ')
    csv_outfile.writerow(get_csv_headers(search_type))
    with tqdm(total=row_total) as prog_bar:
        for agent in agent_data:
            prog_bar.update(1)
            query_results = run_query(session_data, agent, search_type)
            processed_results = process_results(query_results, agent, search_type)
            write_to_file(processed_results, agent, search_type, csv_outfile)

def get_csv_headers(search_type):
    if search_type in ('ENTITY', 'ID'):
        return ['agent_uri', 'name_concat', 'dates', 'wikidata_uri', 'viaf_id', 'lcnaf_id', 'snac_id', 'ulan_id']
    elif search_type == 'NAME':
        return ['num_matches', 'match_score', 'agent_uri', 'aay_url', 'name_concat', 'dates', 'wikidata_uri', 'wikidata_label', 'wikidata_dob', 'wikidata_dod', 'authority_id', 'source']

def main():
    try:
        cfg_json = json.load(open('config.json', 'r', encoding='utf-8'))
        config_data = ConfigData(cfg_json['snac_api_url'], cfg_json['wikidata_user_agent'], 
                                cfg_json['wikidata_user_agent_email'], cfg_json['input_csv'], 
                                cfg_json['output_csv'], cfg_json['backup_directory'])
        file_object, csv_outfile = config_data.open_output_csv()
        wikidata_sesh = setup_session(config_data)
        agent_data = generate_agents(config_data)
        lookup_agents(config_data.row_count(), wikidata_sesh, agent_data, csv_outfile)
    except Exception:
        print(traceback.format_exc())
    finally:
        #this will break if it doesn't get to the opening of the file object
        file_object.close()


if __name__ == "__main__":
    main()
