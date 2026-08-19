from sqlalchemy.orm import sessionmaker
from database import engine
def get_session():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
    finally:
        session.close()