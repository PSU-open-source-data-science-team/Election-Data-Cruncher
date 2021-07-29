import docker
from neo4j_db_api import Neo4jDB
import os
import time


class Neo4jDockerDB(Neo4jDB):
    #TODO child class for launch docker DB
    # set up ports and driver from super() ?

    def start(self, kwargs={}):
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

