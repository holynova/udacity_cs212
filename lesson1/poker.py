# coding
def poker(hands):
    "return best hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    ranks = card_ranks(hand)
    # if straight(ranks) and flush(hand):            # straight flush
    #     return (8, max(ranks))
    # elif kind(4, ranks):                           # 4 of a kind
    #     return (7, kind(4, ranks), kind(1, ranks))
    # elif kind(3, ranks) and kind(2, ranks):        # full house
    #     return  # your code here
    # elif flush(hand):                              # flush
    #     return  # your code here
    # elif straight(ranks):                          # straight
    #     return  # your code here
    # elif kind(3, ranks):                           # 3 of a kind
    #     return  # your code here
    # elif two_pair(ranks):                          # 2 pair
    #     return  # your code here
    # elif kind(2, ranks):                           # kind
    #     return  # your code here
    # else:                                          # high card
    #     return  # your code here

    if flush(hand) and straight(ranks):
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
        return (3, ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    dict = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    ranks = [int(dict.get(n, n)) for n, s in hand]
    ranks.sort(reverse=True)
    return ranks


def two_pair(ranks):
    dict = {}
    for item in ranks:
        dict[item] = dict.get(item)+1 if item in dict else 1
    pair_cnt = 0
    pair_values = []
    for card, amount in dict.items():
        if amount == 2:
            pair_cnt += 1
            pair_values.append(card)
    if pair_cnt == 2:
        pair_values.sort(reverse=True)
        return tuple(pair_values)
        # return pair_values
    else:
        return None


def flush(hand):
    # 同花
    # arr = [s for n, s in hand]
    # first = hand[0][1]
    # return ''.join(arr) == first*len(hand)
    arr = [s for n, s in hand]
    return len(set(arr)) == 1


def straight(ranks):
    # 顺子
    return ranks == list(range(max(ranks), min(ranks)-1, -1))


def kind(ranks, n):
    dict = {}
    for item in ranks:
        dict[item] = dict.get(item)+1 if item in dict else 1
    cnt = 0
    res = None
    for card, amount in dict.items():
        if n == amount:
            res = card
            cnt += 1
    if cnt != 1:
        res = None
    return res


def test():
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "2D 2C 3D 3C KH".split()

    assert poker([sf, fk, fh]) == sf
    # assert 1 + 1 == 2
    assert poker([sf]) == sf
    assert poker([sf * 100]) == sf

    rank_case1 = 'TD JD QD KD AD'.split()
    rank_case2 = '8D JD 7D KD AD'.split()
    assert card_ranks(rank_case1) == [14, 13, 12, 11, 10]
    assert card_ranks(rank_case2) == [14, 13, 11, 8, 7]

    assert flush(sf) == True
    assert flush(fk) == False

    assert straight(card_ranks(sf)) == True
    assert straight(card_ranks(fk)) == False

    fk_ranks = card_ranks(fk)
    tp_ranks = card_ranks(tp)

    assert two_pair(tp_ranks) == (3, 2)
    assert two_pair(fk_ranks) == None

    assert kind(fk_ranks, 4) == 9
    assert kind(fk_ranks, 3) == None
    assert kind(fk_ranks, 2) == None
    assert kind(fk_ranks, 1) == 7

    assert kind(tp_ranks, 2) == None
    assert kind(tp_ranks, 1) == 13

    print('test pass')


test()

'''
牌型大小：皇家同花顺＞同花顺＞四条＞葫芦＞同花＞顺子＞三条＞两队＞对子＞高牌
皇家同花顺
8 同花顺  
7 四条  4+1
6 葫芦 3+2
5 同花 flush
4 顺子 straight
3 三条 3+1+1
2 两队 2+2+1  two_pairs
1 对子 2+1+1+1  
0 高牌 
'''
