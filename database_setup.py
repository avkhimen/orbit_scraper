from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class CoinsquareDogePricesVolumes(Base):
    __tablename__ = "coinsquare_doge_prices_volumes"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String(25))
    price_ask_15 = Column(String(20))
    volume_ask_15 = Column(String(20))
    price_ask_14 = Column(String(20))
    volume_ask_14 = Column(String(20))
    price_ask_13 = Column(String(20))
    volume_ask_13 = Column(String(20))
    price_ask_12 = Column(String(20))
    volume_ask_12= Column(String(20))
    price_ask_11 = Column(String(20))
    volume_ask_11 = Column(String(20))
    price_ask_10 = Column(String(20))
    volume_ask_10 = Column(String(20))
    price_ask_9 = Column(String(20))
    volume_ask_9 = Column(String(20))
    price_ask_8 = Column(String(20))
    volume_ask_8 = Column(String(20))
    price_ask_7 = Column(String(20))
    volume_ask_7 = Column(String(20))
    price_ask_6 = Column(String(20))
    volume_ask_6 = Column(String(20))
    price_ask_5 = Column(String(20))
    volume_ask_5 = Column(String(20))
    price_ask_4 = Column(String(20))
    volume_ask_4 = Column(String(20))
    price_ask_3 = Column(String(20))
    volume_ask_3 = Column(String(20))
    price_ask_2 = Column(String(20))
    volume_ask_2 = Column(String(20))
    price_ask_1 = Column(String(20))
    volume_ask_1 = Column(String(20))
    price_bid_1 = Column(String(20))
    volume_bid_1 = Column(String(20))
    price_bid_2 = Column(String(20))
    volume_bid_2 = Column(String(20))
    price_bid_3 = Column(String(20))
    volume_bid_3 = Column(String(20))
    price_bid_4 = Column(String(20))
    volume_bid_4 = Column(String(20))
    price_bid_5 = Column(String(20))
    volume_bid_5 = Column(String(20))
    price_bid_6 = Column(String(20))
    volume_bid_6 = Column(String(20))
    price_bid_7 = Column(String(20))
    volume_bid_7 = Column(String(20))
    price_bid_8 = Column(String(20))
    volume_bid_8 = Column(String(20))
    price_bid_9 = Column(String(20))
    volume_bid_9 = Column(String(20))
    price_bid_10 = Column(String(20))
    volume_bid_10 = Column(String(20))
    price_bid_11 = Column(String(20))
    volume_bid_11 = Column(String(20))
    price_bid_12 = Column(String(20))
    volume_bid_12 = Column(String(20))
    price_bid_13 = Column(String(20))
    volume_bid_13 = Column(String(20))
    price_bid_14 = Column(String(20))
    volume_bid_14 = Column(String(20))
    price_bid_15 = Column(String(20))
    volume_bid_15 = Column(String(20))
    compared = Column(String(4))

class BittrexDogePricesVolumes(Base):
    __tablename__ = "bittrex_doge_prices_volumes"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String(25))
    price_ask_15 = Column(String(20))
    volume_ask_15 = Column(String(20))
    price_ask_14 = Column(String(20))
    volume_ask_14 = Column(String(20))
    price_ask_13 = Column(String(20))
    volume_ask_13 = Column(String(20))
    price_ask_12 = Column(String(20))
    volume_ask_12= Column(String(20))
    price_ask_11 = Column(String(20))
    volume_ask_11 = Column(String(20))
    price_ask_10 = Column(String(20))
    volume_ask_10 = Column(String(20))
    price_ask_9 = Column(String(20))
    volume_ask_9 = Column(String(20))
    price_ask_8 = Column(String(20))
    volume_ask_8 = Column(String(20))
    price_ask_7 = Column(String(20))
    volume_ask_7 = Column(String(20))
    price_ask_6 = Column(String(20))
    volume_ask_6 = Column(String(20))
    price_ask_5 = Column(String(20))
    volume_ask_5 = Column(String(20))
    price_ask_4 = Column(String(20))
    volume_ask_4 = Column(String(20))
    price_ask_3 = Column(String(20))
    volume_ask_3 = Column(String(20))
    price_ask_2 = Column(String(20))
    volume_ask_2 = Column(String(20))
    price_ask_1 = Column(String(20))
    volume_ask_1 = Column(String(20))
    price_bid_1 = Column(String(20))
    volume_bid_1 = Column(String(20))
    price_bid_2 = Column(String(20))
    volume_bid_2 = Column(String(20))
    price_bid_3 = Column(String(20))
    volume_bid_3 = Column(String(20))
    price_bid_4 = Column(String(20))
    volume_bid_4 = Column(String(20))
    price_bid_5 = Column(String(20))
    volume_bid_5 = Column(String(20))
    price_bid_6 = Column(String(20))
    volume_bid_6 = Column(String(20))
    price_bid_7 = Column(String(20))
    volume_bid_7 = Column(String(20))
    price_bid_8 = Column(String(20))
    volume_bid_8 = Column(String(20))
    price_bid_9 = Column(String(20))
    volume_bid_9 = Column(String(20))
    price_bid_10 = Column(String(20))
    volume_bid_10 = Column(String(20))
    price_bid_11 = Column(String(20))
    volume_bid_11 = Column(String(20))
    price_bid_12 = Column(String(20))
    volume_bid_12 = Column(String(20))
    price_bid_13 = Column(String(20))
    volume_bid_13 = Column(String(20))
    price_bid_14 = Column(String(20))
    volume_bid_14 = Column(String(20))
    price_bid_15 = Column(String(20))
    volume_bid_15 = Column(String(20))
    compared = Column(String(4))

class BidAkPriceVolumeComparison(Base):
    __tablename__ = "bid_ask_price_volume_comparison"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String(25))

    coinsquare_price_ask_1 = Column(String(20))
    bittrex_price_ask_1 = Column(String(20))
    coinsquare_volume_ask_1 = Column(String(20))
    bittrex_volume_ask_1 = Column(String(20))

    coinsquare_price_bid_1 = Column(String(20))
    bittrex_price_bid_1 = Column(String(20))
    coinsquare_volume_bid_1 = Column(String(20))
    bittrex_volume_bid_1 = Column(String(20))

    message_sent = Column(String(5))



engine = create_engine('sqlite:///doge_prices_volumes.db')

Base.metadata.create_all(engine)