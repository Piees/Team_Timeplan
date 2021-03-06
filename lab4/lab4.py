# -*- coding: utf-8 -*-
# Gruppe: Team Timeplan
# Yngve Olsen Ranestad
# Steffen Sande
# Arild Høiland
# Even Nilsen
# Øistein Fongaard
# Håkon Gilje

import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

pranks = ["high card", "Pair", "Two Pair", "Three of a kind", "Straight", \
        "Flush", "Full house", "Four of a kind", "Straight flush"]

def deal(numhands, numcards=5, numdecks=1, deck=mydeck):
    """ Takes parameters: numbers of hands, number of cards(default = 5),
    number of decks(default = 1) used and type of deck(default = mydeck)
    """
    random.shuffle(deck)
    for s in range(numdecks - 1):
        deck = deck + mydeck
    return [deck[numcards*i:numcards*(i+1)] for i in range(numhands)]

def deal_udacity(numhands, n=5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    """ Shuffle deck and deal out numhands n-card hands """
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def poker(hands):
    """ Takes a two dimensional array and returns the winning hand. """
    try:
        print "The winning hand had: " + \
                pranks[hand_rank(allmax(hands,key=hand_rank)[0])[0]]
    except ValueError:
        print "The winning hand had: " + \
                pranks[hand_rank(allmax(hands,key=hand_rank))[0]]
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    """ Takes an iterable (ex. array of hands) and returns the highest ranked
    hand according to the key (ex. hand_rank) """
    result, maxcal = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    if len(result) == 1:
        result = result[0]
    return result

def hand_rank(hand):
    """ Takes an array of cards and returns a tuple with total hand rank """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    """ Takes an array of cards and returns the individual card ranks
    sorted from highest to lowest """
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    """ Returns true if the ordered ranks form a flush """
    checkflush = [s for r, s in hand]
    return checkflush.count(checkflush[1]) == 5

def flush_udacity(hand):
    """ Return True if all the cards have the same suit """
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """ Return True if the ordered ranks form a 5-card straight """
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """ Return the first rank that this hand has exactly n-of-a-kind of
        Return None if there is no n-of-a-kind in the hand """
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """ If there are two pair, return the two ranks as a
        tuple: (highest, lowest); otherwise return None """
    pairlist = ()
    for r in ranks:
        if ranks.count(r) == 2: pairlist = pairlist +(r, )
    set(pairlist)
    pairlist = tuple(set(pairlist))
    if len(pairlist) == 2:
        return pairlist
    else:
        return None

if __name__ == '__main__':
    import timeit
    print "flush()"
    print(timeit.timeit("flush(['6C', '7C', '8C', '9C', 'T2'])", setup="from __main__ import flush"))
    print "flush_udacity()"
    print(timeit.timeit("flush_udacity(['6C', '7C', '8C', '9C', 'T2'])", setup="from __main__ import flush_udacity"))
    print "deal()"
    print(timeit.timeit("deal(2)", setup="from __main__ import deal"))
    print "deal_udacity()"
    print(timeit.timeit("deal_udacity(2)", setup="from __main__ import deal_udacity"))

def test():
    """ Test cases for the functions in poker program """
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fk3 = "TC TS TH 2C TD".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fl = "AH KH JH 6H TH".split() # Flush
    st = "AH KC QD JD TS".split() # Straight
    tk = "2H 2C 2D AC TD".split() # Three of kind
    tp = "TD 9H TH 7C 9S".split() # Two Pair
    op = "TD TC AD KD QD".split() # One Pair
    hq = "2D 3D 4C 5H 7H".split() # High card
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    tp1 = "7H 7D 9C 3C 9S".split() #Two Pair
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    op1 = "KH 7C 5S KS 2S".split() # One pair
    tp2 = "TH 3S 2H 3D TC".split() # Two pair
    tk1 = "TH JD JH 8C JC".split() # Three of kind
    hq1 = "TH 9D 5C 3H 2C".split() # High card
    f3 = "2C 4C 6C 7C TC".split() # Flush
    s3 = "3C 4D 5H 6D 7H".split() # Straight
    assert poker([fk3, f3, s3]) == fk3 #gilje start
    assert poker([sf, 20*fk]) == sf
    assert poker([fk3, 5*f3]) == fk3
    assert card_ranks(fk3) == [10, 10, 10, 10, 2]
    assert card_ranks(f3) == [10, 7, 6, 4, 2]
    assert hand_rank(fk3) == (7, 10, 2)
    assert hand_rank(f3) == (5, [10, 7, 6, 4, 2])
    assert flush(f3) == True
    assert straight(card_ranks(s3)) == True
    assert straight(card_ranks(f3)) == False #gilje slutt
    assert poker([fh, tk, hq]) == fh #oistein start
    assert poker([fl, sf1, tk]) == sf1
    assert poker([op, al, fh]) == fh
    assert poker([st, fk, tp]) == fk
    assert poker([tk, tp, op]) == tk
    assert poker([hq, op, hq]) == op
    assert card_ranks(op1) == [13, 13, 7, 5, 2]
    assert card_ranks(tp2) == [10, 10, 3, 3, 2]
    assert card_ranks(tk1) == [11, 11, 11, 10, 8]
    assert card_ranks(hq1) == [10, 9, 5, 3, 2] #oistein slutt
    assert poker([hq, tp, op]) == tp#steffen start
    assert poker([al, st]) == st
    assert poker([al, st, fl]) == fl
    assert card_ranks(hq) == [7, 5, 4, 3, 2]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]#steffen slutt
    assert poker([sf2, tk, al]) == sf2#arild start
    assert poker([hq, st]) == st
    assert poker([al, st, fk]) == fk
    assert flush(fl) == True
    assert straight(card_ranks(tp)) == False
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(hq) == [7, 5, 4, 3, 2]
    assert hand_rank(tk) == (3, 2, [14, 10, 2, 2, 2])
    assert hand_rank(st) == (4, 14)
    assert kind(5, tpranks) == None#arild slutt
    assert poker([tp, op]) == tp #Even start
    assert poker([hq, tk]) == tk
    assert poker([sf1] + 50*[fl]) == sf1
    assert card_ranks(sf1) == [10, 9, 8, 7, 6]
    assert card_ranks(tk) == [14, 10, 2, 2, 2]
    assert card_ranks(st) == [14, 13, 12, 11, 10]
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, tpranks) == 10
    assert kind(1, fkranks) == 7 #Even slutt
    assert poker([sf1, fk, fh]) == sf1
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf1]) == sf1
    assert poker([sf1] + 99*[fh]) == sf1
    assert hand_rank(sf1) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert straight(card_ranks(al)) == True
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'You did good, and you should feel good about yourself :)'
