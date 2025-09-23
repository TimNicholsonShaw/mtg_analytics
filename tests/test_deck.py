#!/usr/bin/env python

from mtg_analytics.deck import Deck, create_db
try:
    import tests.dummy_decks as dummy_decks
except:
    import dummy_decks as dummy_decks
from loguru import logger
from mtg_analytics.tools import begin_logging
import statistics

# initialize db
cards_db = create_db()
test_deck = Deck(cards_db, dummy_decks.w_life_gain)
empty_deck = Deck(cards_db)

def test_read_from_str(test_deck=test_deck):
    assert len(test_deck) == 60

def test_card_db(cards_db=cards_db):
    spaghetti_monster = cards_db.where_exactly(multiverse_ids=[456600])[0]
    assert spaghetti_monster.name.startswith("Emrakul, the Aeons Torn")

def test_deck_repr(test_deck=test_deck):
    assert not str(test_deck).startswith("No deck parsed")

def test_empty_deck(empty_deck=empty_deck):
    assert str(empty_deck).startswith("No deck parsed")
    assert len(empty_deck)==0

def test_model_land_openings(test_deck=test_deck, num_draws=1000):
    begin_logging("land_draws")

    draws = test_deck.model_land_openings(num_draws)
    average_lands = sum(draws)/len(draws)
    logger.info(f'average lands: {average_lands}')
    logger.info(f'median lands: {statistics.median(draws)}')

    assert len(draws) == num_draws
    assert average_lands > 1.8
    assert average_lands < 2.2
    assert statistics.median(draws) == 2.0

    logger.remove()


if __name__=="__main__":
    pass