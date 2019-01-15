# "ODD+ODD==EVEN"
import string
import re
import itertools


def get_letters(f):
    items = set([i for i in f])
    # s = set(items)
    return ''.join(items).replace(r'+-*/=', '')


print(get_letters('ODD+ODD==EVEN'))

print(itertools.permutations('123', 2))

for i in itertools.permutations('123', ):
    print(i)


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.

    r = r'^[A-Z]{1,}$'
    if re.fullmatch(r, word):
        arr = []
        max = len(word)
        for i, char in enumerate(word):
            arr.append('%d*%s' % (10**(max-i), char))
        res = '(' + '+'.join(arr) + ')'
    else:
        res = word
    return res
