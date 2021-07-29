import docker
from neo4j_db_api import Neo4jDB
import os
import time


class Neo4jDockerDB(Neo4jDB):
    def start(self, kwargs={}):
        '''
        Start container and keep reference
        :param kwargs: bash arguments to start container
        :return:
        '''
        container = self.client.containers.run(**kwargs, detach=True)
        # store reference for destructor
        self.container = container

    def stop(self):
        '''
        Stop container and wait for it to be stopped before closing connection
        :return:
        '''
        self.container.stop()
        maxtime = 20
        # wait for container to stop
        while (self.curl_db() or maxtime <= 0):
            time.sleep(1)
            maxtime -= 1
        self.client.close()

    def __del__(self):
        '''
        Automatically stop container with destructor
        :return:
        '''
        self.stop()
