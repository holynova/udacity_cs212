# coding
import random


def deal(numhands, n=5, deck=[n+s for n in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    hands = []
    for i in range(numhands):
        hand = deck[i*n:(i+1)*n]
        hands.append(hand)
    return hands
    # hands = [my_deck[]]


def hand_percentage(n=700*1000):
    res = [0]*9
    for i in range(n//10):
        hands = deal(10)
        for hand in hands:
            index = hand_rank(hand)[0]
            res[index] += 1

    for i, r in enumerate(reversed(res)):
        print('%d : %6.5f%%' % (i, r/n*100.0))


def poker(hands):
    "return best hand"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    key = key or (lambda x: x)
    res = []
    max_val = None
    for x in iterable:
        val = key(x)
        if not max_val or val > max_val:
            res = [x]
            max_val = val
        elif val == max_val:
            res.append(x)
    return res

    # cur_max = max(iterable, key)
    # max_val = key(cur_max)
    # for item in iterable:
    #     if key(item) == max_val:
    #         res.append(item)
    # return res[0] if len(res) == 1 else res
    # # handle ties 处理平局的情况
    # arr = [(hand, hand_rank(hand)) for hand in hands]
    # # hands.sort(key=lambda x: hand_rank(x), reverse=True)
    # arr.sort(key=lambda x: x[1], reverse=True)
    # # max_hand, max_value = arr[0]
    # if arr.count()


def hand_rank(hand):
    ranks = card_ranks(hand)
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
    table = '--23456789TJQKA'
    ranks = [table.index(n) for n, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks
    # dict = {
    #     'T': 10,
    #     'J': 11,
    #     'Q': 12,
    #     'K': 13,
    #     'A': 14
    # }
    # ranks = [int(dict.get(n, n)) for n, s in hand]
    # ranks.sort(reverse=True)
    # return ranks


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


def kind(n, ranks):
    for card in ranks:
        if ranks.count(card) == n:
            return card
    return None
    # dict = {}
    # for item in ranks:
    #     dict[item] = dict.get(item)+1 if item in dict else 1
    # cnt = 0
    # res = None
    # for card, amount in dict.items():
    #     if n == amount:
    #         res = card
    #         cnt += 1
    # if cnt != 1:
    #     res = None
    # return res


def test():
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    sf2 = "6H 7H 8H 9H TH".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "2D 2C 3D 3C KH".split()
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight

    rank_case1 = 'TD JD QD KD AD'.split()
    rank_case2 = '8D JD 7D KD AD'.split()
    all_cases = [sf, fk, fh, tp, rank_case1, rank_case2]
    # for c in all_cases:
    #     print(c)
    #     print(hand_rank(c))
    #     print('-'*100)

    assert poker([sf, fk, fh]) == [sf]
    # # assert 1 + 1 == 2
    assert poker([sf, sf]) == [sf, sf]
    assert poker([sf, sf2]) == [sf, sf2]
    assert poker([sf*100]) == [sf*100]
    # assert poker([sf * 100]) == sf

    assert card_ranks(rank_case1) == [14, 13, 12, 11, 10]
    assert card_ranks(rank_case2) == [14, 13, 11, 8, 7]
    assert card_ranks(al) == [5, 4, 3, 2, 1]

    assert flush(sf) == True
    assert flush(fk) == False

    assert straight(card_ranks(sf)) == True
    assert straight(card_ranks(fk)) == False
    assert straight(card_ranks(al)) == True

    fk_ranks = card_ranks(fk)
    tp_ranks = card_ranks(tp)

    assert two_pair(tp_ranks) == (3, 2)
    assert two_pair(fk_ranks) == None

    assert kind(4, fk_ranks) == 9
    assert kind(3, fk_ranks) == None
    assert kind(2, fk_ranks) == None
    assert kind(1, fk_ranks) == 7
    assert kind(1, tp_ranks) == 13

    # assert kind(tp_ranks, 2) == None

    print('test pass')


test()
hand_percentage(10000)
# print(deal(5))

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
