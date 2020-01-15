from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

###########RIPPLE############################

class CoinsquareDogePricesVolumes(Base):
    __tablename__ = "coinsquare_doge_prices_volumes"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String(25))
    price_ask_10 = Column(String(20))
    volume_ask_10 = Column(String(20))

engine = create_engine('sqlite:///coin_database_test.db')

Base.metadata.create_all(engine)