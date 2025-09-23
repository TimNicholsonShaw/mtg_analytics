#!/usr/bin/env python
import mtg_parser
from mtgtools.MtgDB import MtgDB
from mtgtools.PCardList import PCardList
import subprocess
from pathlib import Path



def create_db(db_name="card_db.fs", update=False):
    mtg_db = MtgDB(f'{Path(__file__).parent.parent.parent}/database/{db_name}')
    if len(mtg_db.root.scryfall_cards) == 0 or update==True:
        mtg_db.scryfall_bulk_update()
    return mtg_db.root.scryfall_cards


class Deck():

    def __init__(self, card_db):
        #load card db if it
        pass

    def __len__(self):
        pass



if __name__=="__main__":
    create_db()