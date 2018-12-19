def poker(hands):
    "return best hand"
    return max(hands, key=hand_rank)
    pass


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return  # your code here
    elif flush(hand):                              # flush
        return  # your code here
    elif straight(ranks):                          # straight
        return  # your code here
    elif kind(3, ranks):                           # 3 of a kind
        return  # your code here
    elif two_pair(ranks):                          # 2 pair
        return  # your code here
    elif kind(2, ranks):                           # kind
        return  # your code here
    else:                                          # high card
        return  # your code here

    if flush(ranks) and straight(ranks):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(ranks):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    return hand


def two_pair(hand):
    pass


def flush(hand):
    # 同花
    pass


def straight(hand):
    # 顺子
    pass


def kind(n, hand):
    pass


def test():
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    # assert poker([sf,fk,fh]) == sf
    assert 1 + 1 == 2
    assert poker([sf]) == sf
    assert poker([sf * 100]) == sf
    return 'test pass'

    # assert 1 + 2 == 4
print('hello')
test()

'''
牌型大小：皇家同花顺＞同花顺＞四条＞葫芦＞同花＞顺子＞三条＞两队＞对子＞高牌
皇家同花顺
8 同花顺  
7 四条  4+1
6 葫芦 3+2
5 同花 
4 顺子 
3 三条 3+1+1
2 两队 2+2+1
1 对子 2+1+1+1
0高牌 
'''
