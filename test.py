def test():
    sf = "6C 7C 8C 9C TC".spilt()
    fk = "9D 9H 9S 9C 7D".spilt()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    ----------------------------------
    assert poker([sf] + 50*[fk]) == sf
    assert
    assert
    assert
    assert
    assert
    assert
    assert
    assert
    assert
    assert
    return "tests pass"

print test()
