#!/bin/sh

echo "Removing Neo4j container..."
docker stop fec_neo4j
echo "Removing downloaded files..."
rm -rf ./FEC_Election_Data