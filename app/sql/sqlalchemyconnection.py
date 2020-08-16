import sqlalchemy as db
import logging
class sqlconnection:
    logger = logging.getLogger()
    def __init__(self):
        self.engine = None
        self.sqlite_connection = None
        self.connect()

    def connect(self):
        # try:

        engine = db.create_engine('sqlite:///../covid.sqllite',echo=False)
        self.engine = engine
        self.sqlite_connection = engine.connect()
        # except Exception as e:
        # self.logger.error("Unable to connect to sql lite file please check file",exc_info=0)

    def disconnect():
        self.sqlite_connection.close()

    def getAlchemyConnection(self):
        return self.sqlite_connection, self.engine

    
