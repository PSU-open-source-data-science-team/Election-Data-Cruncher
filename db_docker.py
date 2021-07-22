import docker
from neo4j_db_api import Neo4jDB
import os
import time


class Neo4jDockerDB(Neo4jDB):
    #TODO child class for launch docker DB
    # set up ports and driver from super() ?

    def start(self):
        # run with bash command
        kwargs = {"name": "testneo4j",
                  "ports": {"7687/tcp": "7687", "7474/tcp": "7474"},
                  "environment": ["NEO4J_AUTH=neo4j/test"],
                  "remove": True,
                  "image": "neo4j:3.5.17"}

        container = self.client.containers.run(**kwargs, detach=True)
        # store reference for destructor
        self.container = container

    def stop(self):
        self.container.stop()
        maxtime = 20
        # wait for container to stop
        while (self.curl_db() or maxtime <= 0):
            time.sleep(1)
            maxtime -= 1
        self.client.close()

    def __del__(self):
        self.stop()

