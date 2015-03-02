import random
'''numhands = 4
for c in range(1, numhands):
	c = [r+s for r in '2345789TJQKA' for s in 'SHDC']

for x in range(1, numhands):
	random.shuffle(x)
'''

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, numdecks=1, deck=mydeck):
	random.shuffle(deck)
	for s in range(numdecks - 1):
		deck = deck + mydeck
	#hands = []
	#for s in range(1, numhands):
		#for r in range(1, 5):
			#hands[s] = hands[s] + deck.pop()
			#hands[r].append(deck.pop())
	return [deck[n*i:n*(i+1)] for i in range(numhands)]
	#return [[deck.pop() for n in range(n)] for h in range(numhands)]
	#return hands
pranks = ["high card", "Pair", "Two Pair", "Three of a kind", "Straight", \
	"Flush", "Full house", "Four of a kind", "Straight flush"]

def poker(hands):
	"Return a list of winning hands: poker([hand,...]) => [hand,...]"
	#print "The winning hand had: " + \
	   #pranks[hand_rank(allmax(hands,key=hand_rank))[0]]
	#print hand_rank(allmax(hands,key=hand_rank))
	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	"Return a list of all items equal to the max of the iterable."
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

#def allmax(iterable, key=None):
#	iterable.sort(key=key,reverse=True)
#	result = [iterable[0]]
#	maxValue = key(iterable[0]) if key else iterable[0]
#	for value in iterable[1:]:
#		v = key(value) if key else value
#		if v == maxValue: result.append(value)
#		else: break
#	return result

#def allmax(iterable, key=None):
#	best_hands = []
#	max_hand = max(iterable, key=hand_rank)
#	for hand in iterable:
#		if hand_rank(hand) == hand_rank(max_hand):
#			best_hands.append(hand)
#	return best_hands
#/	ismax = max(iterable, key=hand_rank)
#/	return ismax


def hand_rank(hand):
	"Return a value indicating the ranking of a hand."
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
	"Return a list of the ranks, sorted with higher first."
	ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
	ranks.sort(reverse = True)
	return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

#def flush(hand):
#	"Return True if all the cards have the same suit."
#	suits = [s for r,s in hand]
#	return len(set(suits)) == 1

def flush(hand):
	checkflush = [s for r, s in hand]
	return checkflush.count(checkflush[1]) == 5

def straight(ranks):
	"Return True if the ordered ranks form a 5-card straight."
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
	"""Return the first rank that this hand has exactly n-of-a-kind of.
	Return None if there is no n-of-a-kind in the hand."""
	for r in ranks:
		if ranks.count(r) == n: return r
	return None

#def two_pair(ranks):
#    "If there are two pair here, return the two ranks of the two pairs, else None."
#    pair = kind(2, ranks)
#    lowpair = kind(2, list(reversed(ranks)))
#    if pair and lowpair != pair:
#        return (pair, lowpair)
#    else:
#        return None

def two_pair(ranks):
	"""If there are two pair, return the two ranks as a
	tuple: (highest, lowest); otherwise return None."""
	pairlist = ()
	for r in ranks:
		if ranks.count(r) == 2: pairlist = pairlist +(r, )
	set(pairlist)
	pairlist = tuple(set(pairlist))
	if len(pairlist) == 2:
		return pairlist
	else:
		return None

def test():
	"Test cases for the functions in poker program."
	sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
	sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	tp = "TD 9H TH 7C 3S".split() # Two Pair
	al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
	fkranks = card_ranks(fk)
	tpranks = card_ranks(tp)
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
