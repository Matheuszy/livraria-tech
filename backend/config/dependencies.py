from sqlalchemy.orm import sessionmaker
from backend.config.database_config import engine
def get_session():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
    finally:
        session.close()