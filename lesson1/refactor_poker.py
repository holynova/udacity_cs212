def poker(hands):
    list = [hand_ranks(hand) for hand in hands]
    # list.index()
    # print(list)
    # x, hand = max([hand_ranks(hand) for hand in hands], key=lambda x: x[0])
    res = []
    max = None
    for rank, hand in list:
        if not max or rank > max:
            max = rank
            res = [hand]
        elif rank == max:
            res.append(hand)
    return res
    # return [hand]
    # dict = {
    #     # 一副牌不可能五张一样的
    #     (5,): 10,
    #     # flush and straight 9
    #     (4, 1): 7,
    #     (3, 2): 6,
    #     # flush 5
    #     # straig 4
    #     (3, 1, 1): 3,
    #     (2, 2, 1): 2,
    #     (2, 1, 1, 1): 1,
    #     (1, 1, 1, 1, 1): 0
    # }
    # res = []
    # for hand in hands:
    #     counts, ranks = unzip(group(hand))
    #     is_straight = len(counts) == 5 and max(ranks) - min(ranks) == 4
    #     is_flush = len(set([icon for number, icon in hand])) == 1
    #     score = dict.get(counts, 0) + is_straight + is_flush
    #     res.append(score, ranks))
    # x, y, hand=max(res)
    # return hand
    # [()]
    #  max(, key=lambda x: )


def hand_ranks(hand):
    dict = {
        # 一副牌不可能五张一样的
        (5,): 10,
        # flush and straight 9
        (4, 1): 7,
        (3, 2): 6,
        # flush 5
        # straig 4
        (3, 1, 1): 3,
        (2, 2, 1): 2,
        (2, 1, 1, 1): 1,
        (1, 1, 1, 1, 1): 0
    }

    counts, ranks = unzip(group(hand))
    is_straight = len(counts) == 5 and max(ranks) - min(ranks) == 4
    is_flush = len(set([icon for number, icon in hand])) == 1
    score = dict.get(counts, 0) + int(is_straight)*4 + int(is_flush)*5

    return ((score, ranks), hand)


def card_ranks(hand):
    table = '--23456789TJQKA'
    ranks = [table.index(n) for n, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks


def group(hand):
    ranks = card_ranks(hand)
    res = [(ranks.count(item), item) for item in set(ranks)]
    res.sort(reverse=True)
    return res


def unzip(grouped_data):
    return tuple(zip(*grouped_data))
    # counts = []
    # ranks = []
    # for count, rank in grouped_data:
    #     counts.append(count)
    #     ranks.append(rank)
    # return (tuple(counts), tuple(ranks))


def test():
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    sf2 = "6H 7H 8H 9H TH".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "2D 2C 3D 3C KH".split()
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight

    rank_case1 = 'TD JD QD KD AD'.split()
    rank_case2 = '8D JD 7D KD AD'.split()

    assert card_ranks(rank_case1) == [14, 13, 12, 11, 10]
    assert card_ranks(rank_case2) == [14, 13, 11, 8, 7]
    assert card_ranks(al) == [5, 4, 3, 2, 1]
    # print(group(fk))
    assert group(fk) == [(4, 9), (1, 7)]
    assert group(fh) == [(3, 10), (2, 7)]
    assert group(sf) == [(1, 10), (1, 9), (1, 8), (1, 7), (1, 6)]
    assert group(sf2) == [(1, 10), (1, 9), (1, 8), (1, 7), (1, 6)]
    assert group(tp) == [(2, 3), (2, 2), (1, 13)]
    assert group(al) == [(1, 5), (1, 4), (1, 3), (1, 2), (1, 1)]
    # print(tuple(unzip(group(fk))))
    assert unzip(group(fk)) == ((4, 1), (9, 7))
    assert unzip(group(fh)) == ((3, 2), (10, 7))
    assert unzip(group(sf)) == ((1, 1, 1, 1, 1), (10, 9, 8, 7, 6))
    assert unzip(group(sf2)) == ((1, 1, 1, 1, 1), (10, 9, 8, 7, 6))
    assert unzip(group(tp)) == ((2, 2, 1), (3, 2, 13))
    assert unzip(group(al)) == ((1, 1, 1, 1, 1), (5, 4, 3, 2, 1))
    print(poker([sf, fk, fh]))
    assert poker([sf, fk, fh]) == [sf]
    # # assert 1 + 1 == 2
    assert poker([sf, sf]) == [sf, sf]
    assert poker([sf, sf2]) == [sf, sf2]
    assert poker([sf*100]) == [sf*100]

    print('test pass')


test()
