#!/usr/bin/python

import os
import sys
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(file_path, './../'))

import pytest
from card_deck.card_deck import Deck

def test_shuffle_deck():
    card_deck = Deck()
    card_deck.shuffle_deck()
    assert len(card_deck.cards) == 52

def test_deal_one_card():
    card_deck = Deck()
    card_deck.deal_one_card()
    assert len(card_deck.cards) == 51

def test_deal_all_card():
    card_deck = Deck()
    for i in range(0,52):
        card_deck.deal_one_card()
    assert len(card_deck.cards) == 0
