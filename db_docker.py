import docker
from neo4j_db_api import Neo4jDB
import os


class Neo4jDockerDB(Neo4jDB):
    #TODO child class for launch docker DB
    # set up ports and driver from super() ?

    def start(self):
        #TODO start docker container
        # run with bash command
        cmd = "docker run --name neo4jdb " \
              "-p7474:7474 -p7687:7687 -d " \
              "--env NEO4J_AUTH=neo4j/test neo4j:3.5.17"
        os.system(cmd)



    def stop(self):
        try:
            self.container.stop()


    def __del__(self):
        #TODO handle kill to stop container
        pass



