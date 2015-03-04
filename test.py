def test():
    sf = "6C 7C 8C 9C TC".spilt() # Straight Flush
    fk = "9D 9H 9S 9C 7D".spilt() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fk3 = "TC TS TH 2C TD".split() # Four of a Kind
    f3 = "2C 4C 6C 7C 10C".split() # Flush
    s3 = "3C 4D 5H 6D 7H".split() # Straight
    assert poker([fk3, f3, s3]) == fk3
    assert poker([sf] + 20*[fk]) == sf
    assert poker([fk3 + 5*[f3]]) == fk3
    assert card_ranks(fk3) == [10, 10, 10, 10, 2]
    assert card_ranks(f3) == [10, 7, 6, 4, 2]
    assert hand_rank(fk3) == [7, 10, 2]
    assert hand_rank(f3) == [5 [10, 7, 6, 4, 2]]
    assert flush(card_rank(f3)) == True
    assert straight(card_rank(s3)) == True
    assert straight(card_rank(f3)) == False
    return "Easy life"

print test()
