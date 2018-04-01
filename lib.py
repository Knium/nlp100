def n_gram(iterable, n):
    return [iterable[i:i+n] for i in range(len(iterable)-1)]