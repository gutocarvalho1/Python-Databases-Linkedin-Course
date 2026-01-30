import os
import mysql.connector as mysql
from urllib import parse

from sqlalchemy import Engine, create_engine, Column, String, Integer, Boolean, ForeignKey, text, select
from sqlalchemy.orm import relationship, Session, DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv

load_dotenv()

db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_pass = parse.quote_plus(os.environ.get("DB_PASS"))
db_name = os.environ.get("DB_NAME")
db_port = os.environ.get("DB_PORT")

def mysql_connect(db_name):
    """Connect through mysql connector."""
    try:
        return mysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
        )
    except Exception as e:
        print(e)

engine = create_engine(
    url=f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}",
    echo=True)

class Base(DeclarativeBase):
    pass

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))

    def __repr__(self):
        return f"<Project(title='{self.title}', description='{self.description}')>"

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)
    description = Column(String(50))
    completed = Column(Boolean, nullable=False,default=False, server_default=text("0"))

    project = relationship('Project')

    def __repr__(self):
        return f"<Task(description='{self.description}', completed={self.completed})>"