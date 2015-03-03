def flush(hand):
    checkflush = [s for r, s in hand]
    return checkflush.count(checkflush[1]) == 5

def kind(n, ranks):
    
