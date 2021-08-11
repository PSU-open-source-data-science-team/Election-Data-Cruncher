# Election-Data-Cruncher

## Team Members
Daniel Foland - dafoland@pdx.edu

## Project Intent
This project is a backend framework for working with federal election data. The data retrieval, database creation, and import are automated to serve as both a simple and powerful resource for a frontend developer. The included API may be used to access the FEC information within the system.

## Project Scope
This project automates pulling and processing of an [FEC dataset](https://www.fec.gov/data/browse-data/?tab=bulk-data)

It will use a scripted importer in Python that will download the FEC data, and access it from the local filesystem. 

Then the startup script load this information into a newly spawned neo4j database in a docker container. It'll also utilize a class-based Python API for efficiently accessing (via Cypher query language) and formatting the data in a usable manner.

A text report will be generated and display the output of a variety of pre-selected data processing algorithms. One of these, for example, may be the breakdown between individual and organizational donations for a specific candidates's campaign.

## Project Environment
Linux/OSX operating system with Python 3, Docker, and access to install python packages (neo4j, etc).

## Project License
[GNU v3.0](https://github.com/PSU-open-source-data-science-team/Election-Data-Cruncher/blob/main/LICENSE)

## Installation
Dowload the repository:
> git clone https://github.com/PSU-open-source-data-science-team/Election-Data-Cruncher.git

Install require python packages:
> pip install -r requirements.txt 

OPTIONALLY Run test file to verify functionality:
> python neo4j_db_api_test.py

Run the program:
> ./Election-Data-Cruncher

Clean up the container and temp files:
> ./Election-Data-Cruncher --clean

## Usage
The script will automatically download FEC data, bring up the container, import the data, and run some example graph algorithims. 

## Project Schedule
Schedule by week:
1. Develop script to download FEC data, set up docker instance, basic neo4j API
1. Data importing, expand API to facilitate import
1. Demo skeleton project
1. Expand API for data retrieval, implement cypher graph algorithms
1. Expand preselected data processing for users to make simple queries, debug, adapt report generation
1. MVP commit
1. Debug, polish, expand, document
1. Final commit

