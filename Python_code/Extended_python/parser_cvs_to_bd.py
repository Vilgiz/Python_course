from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
from datetime import datetime

engine = create_engine(
    'postgresql+psycopg2://postgres:cf79db54Q@localhost:6969/test_db', echo=True)

con = engine.connect()
#print(con)

Base = declarative_base()



class Market(Base):
    __tablename__ = 'markets'

    FMID = Column(Integer, primary_key=True)
    MarketName = Column(String(255))
    Website = Column(String(255))
    Facebook = Column(String(255))
    Twitter = Column(String(255))
    Youtube = Column(String(255))
    OtherMedia = Column(String(255))
    street = Column(String(255))
    city = Column(String(255))
    County = Column(String(255))
    State = Column(String(100))
    zip = Column(String(10))
    Season1Date = Column(String(255))
    Season1Time = Column(String(255))
    Season2Date = Column(String(255))
    Season2Time = Column(String(255))
    Season3Date = Column(String(255))
    Season3Time = Column(String(255))
    Season4Date = Column(String(255))
    Season4Time = Column(String(255))
    x = Column(Float, nullable=True)
    y = Column(Float, nullable=True)
    Location = Column(String(255))
    Credit = Column(Boolean)
    WIC = Column(Boolean)
    WICcash = Column(Boolean)
    SFMNP = Column(Boolean)
    SNAP = Column(Boolean)
    Organic = Column(Boolean)
    Bakedgoods = Column(Boolean)
    Cheese = Column(Boolean)
    Crafts = Column(Boolean)
    Flowers = Column(Boolean)
    Eggs = Column(Boolean)
    Seafood = Column(Boolean)
    Herbs = Column(Boolean)
    Vegetables = Column(Boolean)
    Honey = Column(Boolean)
    Jams = Column(Boolean)
    Maple = Column(Boolean)
    Meat = Column(Boolean)
    Nursery = Column(Boolean)
    Nuts = Column(Boolean)
    Plants = Column(Boolean)
    Poultry = Column(Boolean)
    Prepared = Column(Boolean)
    Soap = Column(Boolean)
    Trees = Column(Boolean)
    Wine = Column(Boolean)
    Coffee = Column(Boolean)
    Beans = Column(Boolean)
    Fruits = Column(Boolean)
    Grains = Column(Boolean)
    Juices = Column(Boolean)
    Mushrooms = Column(Boolean)
    PetFood = Column(Boolean)
    Tofu = Column(Boolean)
    WildHarvested = Column(Boolean)
    updateTime = Column(DateTime)
# Base.metadata.create_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()

# with open('C:/Projects/Python_course/Python_code/Extended_python/Export.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         x = row['x']
#         y = row['y']
#         try:
#             float(x)
#             float(y)
#         except ValueError:
#             x = None
#             y = None
#         market = Market(
#             FMID=(row['FMID']),
#             MarketName=row['MarketName'],
#             Website=row['Website'],
#             Facebook=row['Facebook'],
#             Twitter=row['Twitter'],
#             Youtube=row['Youtube'],
#             OtherMedia=row['OtherMedia'],
#             street=row['street'],
#             city=row['city'],
#             County=row['County'],
#             State=row['State'],
#             zip=row['zip'],
#             Season1Date=row['Season1Date'],
#             Season1Time=row['Season1Time'],
#             Season2Date=row['Season2Date'],
#             Season2Time=row['Season2Time'],
#             Season3Date=row['Season3Date'],
#             Season3Time=row['Season3Time'],
#             Season4Date=row['Season4Date'],
#             Season4Time=row['Season4Time'],
#             x=x,
#             y=y,
#             Location=row['Location'],
#             Credit=row['Credit'] == 'Y',
#             WIC=row['WIC'] == 'Y',
#             WICcash=row['WICcash'] == 'Y',
#             SFMNP=row['SFMNP'] == 'Y',
#             SNAP=row['SNAP'] == 'Y',
#             Organic=row['Organic'] == 'Y',
#             Bakedgoods=row['Bakedgoods'] == 'Y',
#             Cheese=row['Cheese'] == 'Y',
#             Crafts=row['Crafts'] == 'Y',
#             Flowers=(row['Flowers'] == 'Y'),
#             Eggs=(row['Eggs'] == 'Y'),
#             Seafood=(row['Seafood'] == 'Y'),
#             Herbs=(row['Herbs'] == 'Y'),
#             Vegetables=(row['Vegetables'] == 'Y'),
#             Honey=(row['Honey'] == 'Y'),
#             Jams=(row['Jams'] == 'Y'),
#             Maple=(row['Maple'] == 'Y'),
#             Meat=(row['Meat'] == 'Y'),
#             Nursery=(row['Nursery'] == 'Y'),
#             Nuts=(row['Nuts'] == 'Y'),
#             Plants=(row['Plants'] == 'Y'),
#             Poultry=(row['Poultry'] == 'Y'),
#             Prepared=(row['Prepared'] == 'Y'),
#             Soap=(row['Soap'] == 'Y'),
#             Trees=(row['Trees'] == 'Y'),
#             Wine=(row['Wine'] == 'Y'),
#             Coffee=(row['Coffee'] == 'Y'),
#             Beans=(row['Beans'] == 'Y'),
#             Fruits=(row['Fruits'] == 'Y'),
#             Grains=(row['Grains'] == 'Y'),
#             Juices=(row['Juices'] == 'Y'),
#             Mushrooms=(row['Mushrooms'] == 'Y'),
#             PetFood=(row['PetFood'] == 'Y'),
#             Tofu=(row['Tofu'] == 'Y'),
#             WildHarvested=(row['WildHarvested'] == 'Y'),
#             updateTime=datetime.strptime(
#                 row['updateTime'], '%m/%d/%Y %I:%M:%S %p')
#         )
#         session.add(market)
#     session.commit()
