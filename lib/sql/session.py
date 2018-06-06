from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib import config

class SessionManager:
    def __init__(self,engine):
        self.engine = engine
        self.session = None
    
    def __enter__(self):
        if self.session != None:
            raise Exception("Session already in use!")
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise
        finally:
            self.session.close()
            self.session = None

db_engine = create_engine(config.MYSQL_DBASE_URI,isolation_level="SERIALIZABLE")
def db_session():
    return SessionManager(db_engine)
