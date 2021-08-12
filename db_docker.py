import docker
from neo4j_db_api import Neo4jDB, Neo4jAPIException
import os
import time
from requests import exceptions


class Neo4jDockerDB(Neo4jDB):
    '''
    This child class is used to create a neo4j container and make its resources
    available to the api class
    '''
    def __init__(self):
        '''
        Initialize and automatically start docker db
        '''
        # keep container alive when script is completed
        self.persist = True
        self.client = docker.from_env()
        self.container = self.get_container()
        if not self.container:
            print("Starting neo4j container...")
            self.start()
        maxtime = 20
        while not self.curl_db("127.0.0.1", 7474) and maxtime >= 0:
            time.sleep(1)
            maxtime -= 1
        # container is setup, establish API to localhost
        super().__init__()

    def start(self, kwargs={}):
        '''
        Start container and keep reference
        :param kwargs: bash arguments to start container
        :return:
        '''
        # set default parameters for container unless defined
        if not kwargs:
            kwargs = {"name": "fec_neo4j",
                      "ports": {"7687/tcp": "7687", "7474/tcp": "7474"},
                      "environment": ["NEO4J_AUTH=neo4j/test"],
                      "remove": True,
                      "image": "neo4j:3.5.17"}
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
        while self.curl_db() and maxtime >= 0:
            time.sleep(1)
            maxtime -= 1
        self.client.close()

    def get_container(self):
        '''
        fetch the existing container info if it already exists, or just
        return the reference to the container created
        :return: container object reference
        '''
        if hasattr(self, 'container'):
            return self.container
        else:
            # use possible existing container
            try:
                container = self.client.containers.get('fec_neo4j')
            except exceptions.HTTPError:
                return None
            if container.attrs['State']['Running']:
                self.container = container
                return self.container

    def __del__(self):
        '''
        Automatically stop container with destructor
        :return:
        '''
        if not self.persist:
            self.stop()
