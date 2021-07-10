from neo4j import GraphDatabase, basic_auth


class Neo4jDB:
    def __init__(self, kwargs={}):
        #TODO set up ports and driver

        self.driver = GraphDatabase.driver(
            "bolt://%s:%s/" % (self.host, self.bolt_port),
            auth=basic_auth("neo4j", self.pw))

    def check_response(self):
        #TODO curl server to check response
        pass

    def run_query(self, cmd):
        # TODO execute command
        with self.driver.session() as session:
            tx = session.begin_transaction()
            try:
                session.run(cmd)
                tx.commit()
            except Exception as ex:
                print(f"Query failed: {cmd}")
                print("Exception: ", type(ex).__name__, ex.args)
                # attempt a rollback, if possible
                try:
                    # database in possibly corrupt state, rollback
                    tx.rollback()
                except:
                    pass


    def create_node(self, label, properties):
        # TODO create new node, return id
        pass

    def create_relationship_by_id(self, source_id, destination_id, rel):
        # TODO create relationship between two nodes with matching ID's
        pass

    def get_node_by_name(self, name):
        # TODO run query matching name, return ID
        pass

    def create_node_with_rel_to_id(self, label, properties, relationship, id):
        # TODO create new node with relationship to node with ID
        pass



