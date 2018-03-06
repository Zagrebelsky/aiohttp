import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import json

# create table
engine = sa.create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()
conn = engine.connect()


class Build(Base):
    __tablename__ = 'build'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String(200), nullable=False)
    version = sa.Column(sa.Integer, nullable=False)
    url = sa.Column(sa.String(200), nullable=False)
    owner = sa.Column(sa.String(200), nullable=False)


Build.metadata.create_all(engine)

# create new connection to db
Session = sessionmaker(bind=engine)
session = Session()


# session = scoped_session(Session)


def select_all():
    res = conn.execute(sa.select([Build]))
    # return all rows as a JSON array of objects
    return [dict(r) for r in res]


def select_by_id(data):
    select_st = sa.select([Build]).where(Build.id == data)
    res = conn.execute(select_st)
    for _row in res:
        return [dict(_row)]


def insert(data):
    row = Build(name=data['name'], description=data['description'], version=data['version'], url=data['url'],
                owner=data['owner'])
    session.add(row)
    session.commit()


def update(data):
    # Needs to disassemble data as dict to val and key and replace
    row = session.query(Build).filter(Build.key == data).first()
    session.commit()

# write to base
# session.commit()
