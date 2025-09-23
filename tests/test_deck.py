#!/usr/bin/env python

from mtg_analytics.deck import Deck, create_db



def test_read_from_str():
    pass

def test_card_db():
    cards_db = create_db()
    spaghetti_monster = cards_db.where_exactly(multiverse_ids=[456600])[0]
    assert spaghetti_monster.name.startswith("Emrakul, the Aeons Torn")

