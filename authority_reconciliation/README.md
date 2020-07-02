# authority_api_scripts

Scripts to query Wikidata and other authority files using URIs or strings as input.

__NOTE__: These scripts are still actively being updated and thus are subject to frequent, possibly breaking, changes.

## Requirements

* Python 3.8
* Third-party libraries: `requests`, `fuzzywuzzy`, `tqdm`, `unidecode`

## Setting up your environment

If you do not already have a preferred Python environment setup, it is strongly recommended that you use `conda`. A lightweight distribution of the `conda` environment, Miniconda, can be found [here](https://docs.conda.io/en/latest/miniconda.html). With `conda` it is simple to create multiple Python environments which run on different versions. A good overview of getting started with `conda` can be found [here](https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307)

Once you have installed `conda` and created/activated your project environment, open a Terminal window or Anaconda prompt and navigate to the main `chit_archives_scripts` directory. Install the required packages by entering `pip -r requirements.txt` into the Terminal or prompt.

## Configuring script settings

You can use the included `config.json` file to enter various configuration options, including paths to your input and output files, backup directory, and API credentials for the various authority files. 

__NOTE__: Wikidata requires a very basic level of authentication to run queries in bulk. The user agent field is required, but can be whatever value you want it to be as long as it is unique. The email field is also required, but it's unlikely that Wikidata does any verification.

## Preparing your data for `wikidata.py`

The scripts in this directory use CSV files as input. Some fields must be present, even if blank, for the scripts to run. It is possible, in the `wikidata.py` script, for other types of data to be passed into the `Agent` dataclass.

Required fields:

* `uri`: the local identifier for the agent (i.e. ArchivesSpace URI, Voyage Bib ID). This can be left blank if not applicable.
* `name_concat`: The name, in direct order, of the agent to search (i.e. John Smith)
* `authority_id`: An LCNAF or other external identifier for the agent. If there is not already a known authority ID for the agent leave this column blank.
* `dates`: Birth and/or death dates (YYYY-YYYY). Leave blank if not known
* `source`: This field is required if theere is already a known authority ID. Current accepted values are `LCNAF`, `VIAF`, `ULAN`, and `SNAC`.
* `wikidata_uri`: leave blank if not known.

## Running the scripts

Once your configuration settings are entered into `config.json`, you can start running the included scripts from the Terminal or Anaconda prompt by typing in `python <scriptname>.py `. For more flexibility running the individual functions, you can also import the scripts into an interactive Python interpreter.

## Searching by name string

The `wikidata.py` script allows you to search for a Wikidata entity by name or by an external identifier from another, non-Wikidata source (i.e. LCNAF). The name string query uses case-sensitive substring matching, which is not very sophisticated but works reasonably well. It only searches the Wikidata label fields for a substring match. This could potentially be extended to include date matching, or other methods for either narrowing or broadening the search.

Currently the query can only be used to search for people, not corporate entities or families. The query filters the results to entities which are instances of `human` in order to limit the number of false positives (i.e. scholarly articles that include people's names). Unfortunately there is no single `instanceOf` property that can be used to identify corporate entities.

Once the results are retrieved from Wikidata, the script uses the `fuzzywuzzy` library to compare the agent name to each result and assign a match score from 0 to 100. Currently only matches with a score of 95 or higher are included on the report. Any name which did not return any results, or any match with a score less than 95, is not included in the output of the name query. This could be changed so that these results are written to a separate file.

## Reviewing the data

It is necessary to manually review the results of the name search to identify potential matches and to remove false positives from the result set before running any additional queries on the dataset.

There is potential for using automated methods to do some of the review, for instance by comparing life dates where they exist.

## Retrieve external identifiers from other external identifiers

`wikidata.py` also includes a query which will retrieve external identifiers (i.e. ULAN, SNAC, VIAF) using another external identifier (i.e. LCNAF) as input.

## Retrieving external identifiers from name string results

Once you have a set of matching names, you can use that data to retrieve all associated external identifiers from Wikidata using a similar process to the process for retrieving external IDs from other external IDs. In this case, the external IDs are retrieved by searching on the Wikidata entity ID.

## How to use the external identifier results

Results from the external identifier queries can be used to retrieve additional data, or even additional external ID links, from other authority files (i.e. LCNAF, ULAN). 

The `snac_test.py` file is an early version of a script with similar functionality as the `wikidata.py` script.

The `queries.py` file contains a few (in-progress) functions which connect to the VIAF, LCNAF, and ULAN authority files. Some of the functions simply retrieve lists of external identiiers, but it is also possible to extend these functions to enable users to download or otherwise search the authorities.

For demonstration purposes, running the `queries.py` file from the Terminal or prompt will demonstrate the process for retrieving life dates from ULAN JSON records.

## Deduping name records

The `deduplication.py` file contains some basic functions for performing duplicate analysis on a set of names. Like the `wikidata.py` script it uses `fuzzywuzzy` to perform the matching, and a score is assigned to each comparison. 

This tool is good to use in conjunction with other OpenRefine duplicate analysis tools.

## SPARQL resources

This tutorial is meant to demonstrate how to run SPARQL queries against a large dataset - either name strings or external identifiers such as LCNAF. It is not a SPARQL tutorial. For more information on forming SPARQL queries in the context of Wikidata, consult the following resources:

* [Wikidata Query Service](https://query.wikidata.org/) - run individual queries to test outputs
* [Wikidata SPARQL Tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial)