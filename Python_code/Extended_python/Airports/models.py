from sqlalchemy import Column, Float, ForeignKeyConstraint, Index, Integer, Table, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Airlines(Base):
    __tablename__ = 'airlines'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    alt_name = Column(Text)
    iata = Column(Text)
    icao = Column(Text)
    callsign = Column(Text)
    country = Column(Text)
    active = Column(Text)


class Airports(Base):
    __tablename__ = 'airports'

    id = Column(Integer, primary_key=True)
    airport = Column(Text)
    city = Column(Text)
    country = Column(Text)
    iata = Column(Text)
    icao = Column(Text)
    latitude = Column(Float(asdecimal=True))
    longitude = Column(Float(asdecimal=True))
    elevation = Column(Integer)
    utc = Column(Integer)
    dst = Column(Text)
    region = Column(Text)


t_routes = Table(
    'routes', metadata,
    Column('airline', Text),
    Column('airline_id', Integer),
    Column('src_airport', Text),
    Column('src_airport_id', Integer),
    Column('dst_airport', Text),
    Column('dst_airport_id', Integer),
    Column('codeshare', Text),
    Column('stops', Integer),
    Column('airplane', Text),
    Column('airlines_id', Integer, nullable=False),
    Column('airports_id', Integer, nullable=False),
    Column('airports_id1', Integer, nullable=False),
    Column('airports_id2', Integer, nullable=False),
    Column('airports_id3', Integer, nullable=False),
    ForeignKeyConstraint(['airlines_id'], ['airlines.id'],
                         name='fk_routes_airlines'),
    ForeignKeyConstraint(['airports_id2'], ['airports.id'],
                         name='fk_routes_airports1'),
    ForeignKeyConstraint(['airports_id3'], ['airports.id'],
                         name='fk_routes_airports2'),
    Index('fk_routes_airlines_idx', 'airlines_id'),
    Index('fk_routes_airports1_idx', 'airports_id2'),
    Index('fk_routes_airports2_idx', 'airports_id3')
)
