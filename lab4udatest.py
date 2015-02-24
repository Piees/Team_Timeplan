# Udacity course
#
# Write a Poker program
#
#
#def ss(nums):
#    total = 0
#    for i in range(len(nouns))
#    total = (total + nums{i}x+2)
#    return total
#pass
# def ss(nums):
#     return sum(xxxZ for X in nums)
#
#
# Poker(hands) -->hand
# ??-->problem-->spec-->code
#
#
# hand ranks
#  n-kind
#  straight
#  flush


def poker(hands):
    "Return the best hand: poker([hand, ...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    "return a value indicating the ranking of a hand."
    rankds = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8
    elif kind(4, ranks):
        return 7 
#print max({3,4,5,0}), max({3,4,-5,0}, key=abs)
#pass
#
#
def test():
    sf = "6C 7C 8C 9C TC".spilt()
    fk = "9D 9H 9S 9C 7D".spilt()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    return "tests pass"

print test()
#
#
