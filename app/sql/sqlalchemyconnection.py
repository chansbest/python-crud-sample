import sqlalchemy as db
import logging
class sqlconnection:
    logger = logging.getLogger()
    def __init__(self):
        self.engine = None
        self.sqlite_connection = None
        self.connect()

    def connect(self):
        """connect to sqlalchemy datbase and store connection object,
        this single connection object will be used throughout app lifecycle
        """
        try:
            engine = db.create_engine('sqlite:///../covid.sqllite',echo=False)
            self.engine = engine
            self.sqlite_connection = engine.connect()
        except Exception as e:
            self.logger.error("Unable to connect to sql lite file please check file",exc_info=0)

    def disconnect():
        """todo: will be called from a application shutdown hook which will close the connection
        """
        self.sqlite_connection.close()

    def getAlchemyConnection(self):
        """returns connection and engine objects to be used to run queries
        """
        return self.sqlite_connection, self.engine

    
