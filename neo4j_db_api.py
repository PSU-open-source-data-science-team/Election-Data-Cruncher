from neo4j import GraphDatabase, basic_auth, CypherError
import subprocess
import os


class Neo4jAPIException(Exception):
    '''
    Generic Exception class for the Neo4jDB API class
    '''
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Neo4jAPIException, {0} '.format(self.message)
        else:
            return 'Neo4jAPIException has been raised.'


class Neo4jDB:
    '''
    This is the api class that contains the connector, db port info,
    login credentials, and query functions to pull information from
    the neo4j container (set up in the db_docker child class)
    '''
    def __init__(self, ip="127.0.0.1", bolt=7687, http=7475):
        # set to localhost
        self.ip = ip
        # set object to have default bolt port
        self.bolt = bolt
        # start database driver with default password
        pw = os.environ.get("NEO4J_PASSWORD") or "test"
        # set http port
        self.http = http
        # create db connector
        self.driver = GraphDatabase.driver(
            "bolt://%s:%d/" % (self.ip, self.bolt),
            auth=basic_auth("neo4j", pw))

    def curl_db(self):
        '''
        Check if the neo4j db is responds
        via the selected port in the container
        :return: True if curl got an OK response, False otherwise
        '''
        result = subprocess.getoutput('curl -s -I  %s:%d | grep "200 OK"'
                                      % (self.ip, self.http))
        # '200 OK' in curl result indicates success
        if "200 OK" in result:
            return True
        else:
            return False

    def run_query(self, cmd):
        '''
        Execute a single Cypher query
        :param cmd: Cypher query string to execute
        :return: server response from Cypher command
        '''
        with self.driver.session() as session:
            tx = session.begin_transaction()
            try:
                ret = session.run(cmd)
                tx.commit()
                return ret
            except CypherError as ex:
                print(f"Cypher command failed: {cmd}")
                raise Neo4jAPIException("Neo4j run_query failure.")
            except Exception as ex:
                print("Exception: ", type(ex).__name__, ex.args)
                # attempt a rollback, if possible
                try:
                    # database in possibly corrupt state, rollback
                    tx.rollback()
                except:
                    # unable to rollback, just continue
                    pass
                raise Neo4jAPIException("Neo4j run_query failure.")

    def create_node(self, label, properties):
        '''
        Create node with input properties and labels
        :param label: string of ':' delimited labels
        :param properties: Cypher compliant properties
        :return: neo4j ID of the node created
        '''
        command = "CREATE (n:%s {%s}) " \
                  "RETURN ID(n)" % (label, properties)
        ret = self.run_query(command)
        try:
            # return response data
            return ret.data()[0]['ID(n)']
        except Exception:
            raise Neo4jAPIException("Neo4j create_node failure: %s" % command)

    def create_relationship_by_id(self, source_id, destination_id, rel):
        # TODO create relationship between two nodes with matching ID's
        pass

    def get_node_by_name(self, name):
        # TODO run query matching name, return ID
        pass

    def create_node_with_rel_to_id(self, label, properties, relationship, id):
        # TODO create new node with relationship to node with ID
        pass



