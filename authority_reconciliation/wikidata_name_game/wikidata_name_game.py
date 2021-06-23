#/usr/bin/python3

from collections import defaultdict
import csv
from operator import itemgetter
import os
import pprint
import sys

from rich import print
from rich.layout import Layout
from rich.padding import Padding
from rich.prompt import Prompt
from rich.panel import Panel
from constants import console


def welcome():
    console.rule()
    console.rule()
    console.rule("[color(11)]Wikidata Match Game[/color(11)]")
    console.rule()

def format_links(links):
    # This will remain the same
    link_list = [tuple(item.split('-- ')) for item in links.split('; ')]
    newline = "\n\t"
    return f"{newline.join(f'[color(32)][link={item[1]}]{item[0]}[/link][/color(32)]' for item in link_list if item[0] != '')}"

def format_entry(row, num_matches):
    entry_store = f"""
    [color(79)][underline]Wikidata matches:[/color(79)][/underline]"""
    for i, value in enumerate(row, 1):
        entry_store = f"""{entry_store}

    [bold]Match [color(79)]{i}/{num_matches}[/color(79)][/bold]:
    [bold]Similarity score: [color(79)]{value['similarity']}[/color(79)][/bold]

    [color(5)]Wikidata name[/color(5)]: [color(11)]{value['wikidata_name']}[/color(11)]
    [color(5)]Wikidata URI[/color(5)]: [color(11)]{value['wikidata_uri']}[/color(11)]
    [color(5)]Wikidata dates[/color(5)]: [color(11)]{value['wikidata_begin']}-{value['wikidata_end']}[/color(11)]
    """
    return entry_store



def format_base_agent(valuedict):
    return f"""
    [color(79)][underline]Source name[/underline]:[/color(79)] [bold][color(11)]{valuedict['name_concat']}[/color(11)][/bold]

    [color(5)]Full name[/color(5)]: [color(11)]{valuedict['sort_name']}[/color(11)]
    [color(5)]Life dates[/color(5)]: [color(11)]{valuedict['dates']}[/color(11)]
    [color(5)]Archives at Yale URL[/color(5)]: [color(32)]{valuedict['aay_url']}[/color(32)]
    [color(5)]ArchivesSpace Staff URL[/color(5)]: 
        [color(32)]{valuedict['aay_url'].replace('archives.yale.edu/agents/people/', 'archivesspace.library.yale.edu/agents/agent_person/')}[/color(32)]
    [color(5)]Collection links[/color(5)]: 
        {format_links(valuedict['resources'])}
    [color(5)]Component links[/color(5)]: 
        {format_links(valuedict['archival_objects'])}
    [color(5)]Accession titles (no links)[/color(5)]:
        {format_links(valuedict['accessions'])}
    """

def gendict(header_row, value):
    zipdict = dict(zip(header_row, value))
    return zipdict

def question(values, header_row, number_of_matches):
    valuedicts = [gendict(header_row, value) for value in values]
    source_entry = format_base_agent(valuedicts[0])
    wiki_entries = format_entry(valuedicts, number_of_matches)
    combined = f"""
        {source_entry} 
        {wiki_entries}"""
    return combined

def answer(values, key):
    # console.print("[bold][color(168)]Enter the number of the[/bold][/color(168)]")
    answ = Prompt.ask("[bold][color(11)]Enter the number of the Wikidata name which matches the source name. Enter 0 if there is no match. Enter M if unsure. Enter Q to quit[/color(11)][/bold]", choices=['0', '1', '2', '3', '4', '5', 'Q'])
    if answ == '0':
        return [key, 'NO MATCH']
    if answ == 'M':
        return [key, 'REVIEW']
    if answ in ('1', '2', '3', '4', '5'):
        selection = values[int(answ) - 1]
        return selection
    if answ == "Q":
        sys.exit()
    
def existing_data(outputfile):
    # gets the length of the existing output file, then starts at that row in the data file
    with open(outputfile) as ofile:
        reader = csv.reader(ofile)
        length = len(list(reader))
        # this accounts for the header row
        if length > 1:
            length = length - 1
        return length

def prep_data(fp):
    def_dict = defaultdict(list)
    with open(fp, 'r', encoding='utf-8') as infile:
        csvreader = csv.reader(infile)
        header_row = next(csvreader)
        for row in csvreader:
            uri = row[7]
            def_dict[uri].append(row)
    sub_dict = {key: value for key, value in def_dict.items() if len(value) < 6}
    return header_row, sub_dict

def main():
    welcome()
    csvpath = Prompt.ask("[color(11)]Please enter path to data source[/color(11)]")
    os.system('cls||clear')
    outputpath = f"{csvpath.replace('.csv', '')}_output.csv"
    header_row, dataset = prep_data(csvpath)
    data_length = len(dataset)
    with open(outputpath, 'a', encoding='utf-8') as csvoutfile:
        existing_data_length = existing_data(outputpath)
        csvwriter = csv.writer(csvoutfile)
        if existing_data_length == 0:
            csvwriter.writerow(header_row)
        counter = 0
        for key, values in dataset.items():
            counter +=1
            if counter > existing_data_length:
                try:
                    welcome()
                    number_of_matches = len(values)
                    values.sort(key=itemgetter(1))
                    console.print(f"{counter}/{data_length}", justify='center')
                    quest = Panel(question(values, header_row, number_of_matches))
                    console.print(quest)
                    row = answer(values, key)
                    csvwriter.writerow(row)
                except Exception:
                    csvwriter.writerow([key, 'ERROR'])
                    console.print_exception()
                os.system('cls||clear')


if __name__ == "__main__":
    main()