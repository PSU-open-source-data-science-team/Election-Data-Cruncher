# Election-Data-Cruncher

## Team Members
Daniel Foland - dafoland@pdx.edu

## Project Intent
This project is a backend framework for working with federal election data. The data retrieval, database creation, and import are automated to serve as both a simple and powerful resource for a frontend developer. The included API may be used to access the FEC information within the system.

## Project Scope
This project automates pulling and processing of the 2021 [FEC dataset](https://www.fec.gov/data/browse-data/?tab=bulk-data)

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
> pip3 install -r requirements.txt 

OPTIONALLY Run test file to verify functionality:
> python3 neo4j_db_api_test.py

Run the program:
> ./Election-Data-Cruncher -q

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

## Accolades
Without these technologies and the hard work by their respective authors, this project would not be possible
1. The Neo4j database and Python connector
1. Docker
1. [Ivan Vinogradov](https://stackoverflow.com/questions/56950987/download-file-from-url-and-save-it-in-a-folder-python)
1. The Federal Election Commission

## Example Run
Files downloading:
![image](https://user-images.githubusercontent.com/47869340/129457351-72d9669b-5a66-4ee6-8475-6e1fee56f1cc.png | width=300)
Output displayed with example queries:
![image](https://user-images.githubusercontent.com/47869340/129457369-7ea3f99f-4eeb-4bf9-809d-9ec44b0f3cfd.png | width=300)
Graph nodes viewable via the web interface (http://localhost:7474/browser/): 
![image](https://user-images.githubusercontent.com/47869340/129457374-d90a7c91-a221-4917-88f9-cc3a4e22f253.png | width=300)

