#!/usr/bin/env python

import unittest
import neobolt
import warnings
from db_docker import Neo4jDockerDB
from neo4j_db_api import Neo4jAPIException
from neobolt import exceptions

# ignore warnings during import time or it won't work
warnings.filterwarnings("ignore", message="can't resolve package \
    from __spec__ or __package__")
warnings.filterwarnings("ignore", message="ResourceWarning: unclosed")

class TestDatabase(unittest.TestCase):
    # test functions exectuted in alphabetical order
    def test_1_do_stuff(self):
        # create and start neo4j container
        neo4j_docker_db = Neo4jDockerDB()
        neo4j_docker_db.start()