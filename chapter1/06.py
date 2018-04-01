from lib import n_gram

def bi_gram(iterable):
    return n_gram(iterable, 2)

X = set(bi_gram("paraparaparadise"))
Y = set(bi_gram("paragraph"))
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
print('X contains se') if 'se' in X else print('X doesn\'t contain se')
print('Y contains se') if 'se' in Y else print('Y doesn\'t contain se')
