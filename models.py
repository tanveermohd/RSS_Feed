from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.orm import declarative_base

# Define the database connection URL with the newly created database
db_url_with_db = 'postgresql://postgres:ashulshona@localhost:5432/rss_feed_database'

# Create a new engine with the specified database name
engine_with_db = create_engine(db_url_with_db)

# Define the base class for ORM
Base = declarative_base()

# Define the Article model
class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    publication_date = Column(TIMESTAMP)
    source_url = Column(String)
    
    # Ensure each article is unique based on title and source URL
    __table_args__ = (
        UniqueConstraint('title', 'source_url', name='uq_title_source_url'),
    )

# Create the table in the database if it doesn't exist
Base.metadata.create_all(engine_with_db)