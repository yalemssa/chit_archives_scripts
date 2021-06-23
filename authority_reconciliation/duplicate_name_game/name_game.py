#/usr/bin/python3

import csv
import os
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
    console.rule("[color(11)]ArchivesSpace Duplicate Name Game[/color(11)]")
    console.rule()

def format_links(links):
    #
    link_list = [tuple(item.split('-- ')) for item in links.split('; ')]
    print(link_list)
    newline = "\n\t"
    return f"{newline.join(f'[color(32)][link={item[1]}]{item[0]}[/link][/color(32)]' for item in link_list if item[0] != '')}"

def format_entry(row, choice_num):
    return f"""
    [color(79)][underline]Name #{choice_num}[/underline][/color(79)]:

    [color(5)]Matched name[/color(5)]: [color(11)]{row[0]}[/color(11)]
    [color(5)]Full name[/color(5)]: [color(11)]{row[1]}[/color(11)]
    [color(5)]Life dates[/color(5)]: [color(11)]{row[2]}[/color(11)]
    [color(5)]Library of Congress ID[/color(5)]: [color(32)]{row[3]}[/color(32)]
    [color(5)]Archives at Yale URL[/color(5)]: [color(32)]{row[4]}[/color(32)]
    [color(5)]Collection links[/color(5)]: 
        {format_links(row[5])}
    [color(5)]Component links[/color(5)]: 
        {format_links(row[6])}
    [color(5)]Accession titles (no links)[/color(5)]:
        {format_links(row[7])}
    """

def question(row, index):
    similarity = row['similarity']
    # left_compare = row[5:22]
    left_compare = [row['name_concat_left'], row['sort_name_left'], row['dates_left'], row['authority_id_left'], row['agent_aay_url_left'], row['resource_ids_left'], row['archival_object_ids_left'], row['accession_ids_left']]
    right_compare = [row['name_concat_right'], row['sort_name_right'], row['dates_right'], row['authority_id_right'], row['agent_aay_url_right'], row['resource_ids_right'], row['archival_object_ids_right'], row['accession_ids_right']]
    # right_compare = row[24:41]
    # Fix to calculate number of rows
    return f"""
    [bold]Entry number: [color(79)]{index}[/color(79)]/[color(79)]2275[/color(79)][/bold]
    [bold]Similarity score: [color(79)]{similarity}[/color(79)]/[color(79)]1[/color(79)][/bold]
    {format_entry(left_compare, 1)}
    {format_entry(right_compare, 2)}
    """

def answer(row):
    console.print("[bold][color(168)]Y: Match, N: No match, M: Possible match, Q: Quit[/bold][/color(168)]")
    answ = Prompt.ask("[bold][color(11)]Are these the same person?[/color(11)][/bold]", choices=["Y", "N", "M", "Q"])
    if answ in ('Y', 'N', 'M'):
        row['decision'] = answ
        return answ, row
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


def main():
    welcome()
    csvpath = Prompt.ask("[color(11)]Please enter path to data source[/color(11)]")
    os.system('cls||clear')
    outputpath = f"{csvpath.replace('.csv', '')}_output.csv"
    with open(csvpath, 'r', encoding='utf-8') as csvfile, open(outputpath, 'a', encoding='utf-8') as csvoutfile:
        existing_data_length = existing_data(outputpath)
        csvreader = csv.DictReader(csvfile)
        header_row = csvreader.fieldnames
        header_row.append('decision')
        csvwriter = csv.DictWriter(csvoutfile, fieldnames=header_row)
        if existing_data_length == 0:
            csvwriter.writeheader()
        for i, row in enumerate(csvreader, 1):
            if i > existing_data_length:
                try:
                    welcome()
                    quest = Panel(question(row, i))
                    console.print(quest)
                    ans, row = answer(row)
                    csvwriter.writerow(row)
                except Exception:
                    row['decision'] = 'ERROR'
                    csvwriter.writerow(row)
                    console.print_exception()
               # os.system('cls||clear')

if __name__ == "__main__":
    main()