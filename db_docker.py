import docker
from neo4j_db_api import Neo4jDB

class Neo4jDockerDB(Neo4jDB):
    #TODO child class for launch docker DB
    # set up ports and driver from super() ?

    def start(self):
        #TODO start docker container
        # run with kwargs
        pass

    def stop(self):
        #TODO docker stop container
        pass

    def __del__(self):
        #TODO handle kill to stop container
        pass



