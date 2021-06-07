#/usr/bin/python3

import csv
import os
import traceback

from textwrap import wrap

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
    link_list = [tuple(item.split('-- ')) for item in links.split('; ')]
    newline = "\n\t"
    # This did not work with the accession link, most likely because it also has parentheses, so not just
    # a link. Need to fix that, possibly?
    return f"{newline.join(f'[color(32)][link={item[1]}]{item[0]}[/link][/color(32)]' for item in link_list if item[0] != '')}"

def format_entry(row, choice_num):
    return f"""
    [color(79)][underline]Name #{choice_num}[/underline][/color(79)]:

    [color(5)]Matched name[/color(5)]: [color(11)]{row[2]}[/color(11)]
    [color(5)]Full name[/color(5)]: [color(11)]{row[3]}[/color(11)]
    [color(5)]Life dates[/color(5)]: [color(11)]{row[4]}[/color(11)]
    [color(5)]Library of Congress ID[/color(5)]: [color(32)]{row[7]}[/color(32)]
    [color(5)]Archives at Yale URL[/color(5)]: [color(32)]{row[1]}[/color(32)]
    [color(5)]Collection links[/color(5)]: 
        {format_links(row[11])}
    [color(5)]Component links[/color(5)]: 
        {format_links(row[12])}
    [color(5)]Accession titles (no links)[/color(5)]:
        {format_links(row[13])}
    """

def question(row, index):
    similarity = row[2]
    left_compare = row[5:22]
    right_compare = row[24:41]
    # Fix to calculate number of rows
    return f"""
    [bold]Entry number: [color(79)]{index}[/color(79)]/[color(79)]2280[/color(79)][/bold]
    [bold]Similarity score: [color(79)]{similarity}[/color(79)]/[color(79)]1[/color(79)][/bold]
    {format_entry(left_compare, 1)}
    {format_entry(right_compare, 2)}
    """

def answer(row):
    answ = Prompt.ask("[bold][color(11)]Are these the same person?[/color(11)][/bold]", choices=["Y", "N", "M"])
    if answ in ('Y', 'N', 'M'):
        row.append(answ)
    return answ, row

def existing_data(outputfile):
    # gets the length of the existing output file, then starts at that row in the data file
    with open(outputfile) as ofile:
        lines = ofile.readlines()
        return len(lines[1:])

def main():
    welcome()
    csvpath = Prompt.ask("[color(11)]Please enter path to data source[/color(11)]")
    os.system('cls||clear')
    outputpath = f"{csvpath.replace('.csv', '')}_output.csv"
    with open(csvpath, 'r', encoding='utf-8') as csvfile:
        with open(outputpath, 'a', encoding='utf-8') as csvoutfile:
            existing_data_length = existing_data(outputpath)
            csvreader = csv.DictReader(csvfile)
            csvwriter = csv.writer(csvoutfile)
            header_row = csvreader.fieldnames
            if existing_data_length == 0:
                csvwriter.writerow(header_row + ['decision'])
            for i, row in enumerate(csvreader, 1):
                if i > existing_data_length:
                    try:
                        welcome()
                        quest = Panel(question(row, i))
                        console.print(quest)
                        ans, row = answer(row)
                        csvwriter.writerow(row)
                    except Exception:
                        # console.print(row)
                        row.append('ERROR')
                        csvwriter.writerow(row)
                        console.print_exception()
                    os.system('cls||clear')

if __name__ == "__main__":
    main()