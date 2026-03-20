''' >>> import random
    >>> random.random()
    0.7580791151546706
    >>> random.random()
    0.3339069326508808
    >>> random.random()
    0.15127154750723637
    >>> random.randint(1,10)
    5
    >>> random.randint(1,10)
    3
    >>> random.randint(1,10)
    3
    >>> random.randint(1,10)
    6
    >>> random.randrange(1,25,2)
    19
    >>> random.randrange(1,25,2)
    15
    >>> random.randrange(0,30,3)
    24
    >>> random.randrange(0,30,3)
    21
    >>> list = [1, 2, 7, 9, 34, 69]
    >>> random.choice(list)
    69
    >>> random.choice(list)
    7
    >>> random.choice(list)
    1
    >>> random.choice(list)
    69
    >>> random.choice('abcdefghijklmnopqrstuvwxyz')
    'i'
    >>> random.choice('abcdefghijklmnopqrstuvwxyz')
    'v'
    >>> random.choice('abcdefghijklmnopqrstuvwxyz')
    'p'
    >>> random.sample(list, 2)
    [1, 9]
    >>> random.sample(list, 3)
    [69, 34, 7]
    >>> random.sample(list, 5)
    [1, 34, 69, 7, 9]   '''