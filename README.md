# Election-Data-Visualizer

Team Members:
Daniel Foland - dafoland@pdx.edu
Lyle Hubbar - lhubbard@pdx.edu (tentative)

# Project Scope
This project automates pulling and processing of an FEC dataset: https://www.fec.gov/data/browse-data/?tab=bulk-data

It will use a scripted importer in Python that will download the FEC data, and access it from the local filesystem. 

Then the startup script load this information into a newly spawned neo4j database in a docker container. It'll also utilize a class-based Python API for efficiently accessing (via Cypher query language) and formatting the data in a usable manner.

A visualization program (tentative) will then display the output of a variety of pre-selected data processing algorithms. One of these may be the breakdown between individual and organizational donations for a specific candidates's campaign.

# Project Environment
Linux/OSX operating system with Python 3, Docker, and access to install python packages (neo4j, etc). Frontend technologies tentative.

# Project Schedule
Week 1 - Develop script to download FEC data, set up docker instance, basic neo4j API, research frontend solutions
Week 2 - Data importing, expand API to facilitate import, develop skeleton frontend
Week 3 - Demo skeleton project
Week 4 - Expand API for data retrieval to frontend, implement graph algorithms (apoc?)
Week 5 - Expand preselected data processing for users to make simple queries, debug, adapt frontend and expand any needed animations or query fields
Week 6 - MVP commit
Week 7 - Debug, polish, expand, document
Wwek 8 - Final commit

