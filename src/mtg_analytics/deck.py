#!/usr/bin/env python
import mtg_parser
from mtgtools.MtgDB import MtgDB
from mtgtools.PCardList import PCardList
import subprocess
from pathlib import Path
from tqdm import tqdm
from random import shuffle



def create_db(db_name="card_db.fs", update=False):
    mtg_db = MtgDB(f'{Path(__file__).parent.parent.parent}/database/{db_name}')
    if len(mtg_db.root.scryfall_cards) == 0 or update==True:
        mtg_db.scryfall_bulk_update()
    return mtg_db.root.scryfall_cards


class Deck():

    def __init__(self, card_db, deck_string=""):
        if deck_string:
            self.cards = card_db.from_str(deck_string)
        else:
            self.cards=PCardList()


    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        if len(self.cards) == 0:
            return "No deck parsed"
        return self.cards.deck_str(add_set_codes=False)

    def model_land_openings(self, num_draws):
        out = []

        for _ in tqdm(range(num_draws)):
            shuffle(self.cards)
            out.append(len(self.cards[:6].lands()))

        return out



if __name__=="__main__":
    create_db()