    id = Column(Integer, primary_key=True)
    timestamp = Column(String(25))
    price_ask_15 = entry['ask_15']['price']
    volume_ask_15 = entry['ask_15']['volume']
    price_ask_14 = entry['ask_14']['price']
    volume_ask_14 = entry['ask_14']['volume']
    price_ask_13 = entry['ask_13']['price']
    volume_ask_13 = entry['ask_13']['volume']
    price_ask_12 = entry['ask_12']['price']
    volume_ask_12= entry['ask_12']['volume']
    price_ask_11 = entry['ask_11']['price']
    volume_ask_11 = entry['ask_11']['volume']
    price_ask_10 = entry['ask_10']['price']
    volume_ask_10 = entry['ask_10']['volume']
    price_ask_9 = entry['ask_9']['price']
    volume_ask_9 = entry['ask_9']['volume']
    price_ask_8 = entry['ask_8']['price']
    volume_ask_8 = entry['ask_8']['volume']
    price_ask_7 = entry['ask_7']['price']
    volume_ask_7 = entry['ask_7']['volume']
    price_ask_6 = entry['ask_6']['price']
    volume_ask_6 = entry['ask_6']['volume']
    price_ask_5 = entry['ask_5']['price']
    volume_ask_5 = entry['ask_5']['volume']
    price_ask_4 = entry['ask_4']['price']
    volume_ask_4 = entry['ask_4']['volume']
    price_ask_3 = entry['ask_3']['price']
    volume_ask_3 = entry['ask_3']['volume']
    price_ask_2 = entry['ask_2']['price']
    volume_ask_2 = entry['ask_2']['volume']
    price_ask_1 = entry['ask_1']['price']
    volume_ask_1 = entry['ask_1']['volume']
    price_bid_1 = entry['bid_1']['price']
    volume_bid_1 = entry['bid_1']['volume']
    price_bid_2 = entry['bid_2']['price']
    volume_bid_2 = entry['bid_2']['volume']
    price_bid_3 = entry['bid_3']['price']
    volume_bid_3 = entry['bid_3']['volume']
    price_bid_4 = entry['bid_4']['price']
    volume_bid_4 = entry['bid_4']['volume']
    price_bid_5 = entry['bid_5']['price']
    volume_bid_5 = entry['bid_5']['volume']
    price_bid_6 = entry['bid_6']['price']
    volume_bid_6 = entry['bid_6']['volume']
    price_bid_7 = entry['bid_7']['price']
    volume_bid_7 = entry['bid_7']['volume']
    price_bid_8 = entry['bid_8']['price']
    volume_bid_8 = entry['bid_8']['volume']
    price_bid_9 = entry['bid_9']['price']
    volume_bid_9 = entry['bid_9']['volume']
    price_bid_10 = entry['bid_10']['price']
    volume_bid_10 = entry['bid_10']['volume']
    price_bid_11 = entry['bid_11']['price']
    volume_bid_11 = entry['bid_11']['volume']
    price_bid_12 = entry['bid_12']['price']
    volume_bid_12 = entry['bid_12']['volume']
    price_bid_13 = entry['bid_13']['price']
    volume_bid_13 = entry['bid_13']['volume']
    price_bid_14 = entry['bid_14']['price']
    volume_bid_14 = entry['bid_14']['volume']
    price_bid_15 = entry['bid_15']['price']
    volume_bid_15 = entry['bid_15']['volume']
    compared = Column(String(4))