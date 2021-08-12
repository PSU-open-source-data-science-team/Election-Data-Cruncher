#!/usr/bin/env python

import unittest
import neobolt
import warnings
from db_docker import Neo4jDockerDB
from neo4j_db_api import Neo4jAPIException
from neobolt import exceptions

# ignore warnings on ports
warnings.filterwarnings("ignore", message="can't resolve package \
    from __spec__ or __package__")
warnings.filterwarnings("ignore", message="ResourceWarning: unclosed")


class TestDatabase(unittest.TestCase):
    # test functions exectuted in alphabetical order
    def test_1_do_stuff(self):
        # create and start neo4j container
        neo4j_docker_db = Neo4jDockerDB()
        neo4j_docker_db.start()
        # teardown db when completed
        neo4j_docker_db.persist = False

        self.assertTrue(neo4j_docker_db.curl_db(),
                        "database HTTP response detected")

        result = neo4j_docker_db.run_query("MATCH (n) return n")
        self.assertEqual(result.data()['n'], "", "Executed query on empty db")

        # test create node
        id = neo4j_docker_db.create_node("Test", "val:5")

        self.assertTrue(id, "ID returned from create node")

        # try to get same id by property
        self.assertEqual(
            neo4j_docker_db.get_node_id_by_prop("val: 5", id,
                                                "Found node with matching "
                                                "properties"))

        # create another test node
        other_id = neo4j_docker_db.create_node("Test", "val : 10")

        # test the link call
        neo4j_docker_db.create_relationship_by_id(id, other_id, "LINK")

        # create another node and test that link
        neo4j_docker_db.create_node_with_rel_to_id("Test", "val:5", "LINK", id)

        # check nodes created and links formed
        self.assertEqual(
            neo4j_docker_db.run_query("MATCH (n) - [:LINK] - (p) "
                                      "WHERE ID(n) = %d "
                                      "return count(p)").data()['count(p)'],
            2,
            "Links created properly")
