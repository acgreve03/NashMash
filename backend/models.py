from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#declrative base creates a base class that all db tables will inherit from. Every tables defined in the future will inherit from base
Base = declarative_base()

#Creates a table model named "Song", and creates a structured table in which each row is a song 
class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    bpm = Column(String)
    key = Column(String)
    mode = Column(String)

    #Connect to the DB

    #Tells SQLAlchemy where to store the DB, sqlite will save data in a file called "songs.db"
DATABASE_URL = "sqlite:///songs.db"

    #connects sqlalchemy to the DB
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)



if __name__ == '__main__':
    init_db()