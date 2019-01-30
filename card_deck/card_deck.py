import itertools, random

class Deck(object):
    """
    Represents the deck of cards
    """
    def __init__(self):
        self.deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
        self.higher_cards = dict({11: "Jack", 12: "Queen", 13: "King"})

    def shuffle_deck(self):
        """
        Shuffles the card Deck
        """
        for i in range(0, 52):
            rnd_idx = (i + random.randint(0, 52)) % (52-i)
            tmp = self.deck[i]
            self.deck[i] = self.deck[rnd_idx]
            self.deck[rnd_idx] = tmp

    def deal_one_card(self):
        """
        Deals one card from the deck
        """
        return self.deck.pop(0)

    @property
    def cards(self):
        return self.deck

    @property
    def high_cards(self):
        return self.higher_cards


class Start(object):
    """
    A user can:
    1. Draw a card as many times as they wish, until the deck is depleted
    2. Shuffle the entire deck at any time
    3. See a list of the cards they've drawn so far
    4. Quit playing with the deck (Exit the program)
    """

    def start_game(self):
        """
        Starts the card game
        """
        new_deck = Deck()
        new_deck.shuffle_deck()

        while True:
            try:
                choice = input("\nWould you like to: \n* (S)huffle the deck \n* (D)raw a card \n* See Your (C)ards \n* (Q)uit? ")
                choice = str(choice.lower())
            except NameError as e:
                print "Please enter the option in quotes"
                exit()
            if choice == 's':
                new_deck.shuffle_deck()
                # for card in new_deck.deck:
                #     print(card)
                print "Okay, I shuffled the deck."
                continue
            elif choice == 'd':
                if len(new_deck.deck) >= 1:
                    mycard = new_deck.deal_one_card()
                    print "\nYou drew the {} of {}.".format(new_deck.high_cards.get(mycard[0], mycard[0]), mycard[1])
                    print "There are {} cards left in the deck.".format(len(new_deck.deck))
                    continue
                else:
                    print "Sorry, there are no more cards left!"
                    continue
            elif choice == 'c':
                print "\nSo far, you've drawn these cards:\n"
                for card in new_deck.cards:
                    print "{} of {}".format(new_deck.high_cards.get(card[0], card[0]), card[1])
                continue
            elif choice == 'q':
                print 'Thanks for playing!'
                break
            else:
                print "Sorry, that's not a valid choice"
                continue

if __name__ == '__main__':
    start = Start()
    start.start_game()
