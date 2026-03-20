''' >>> import datetime
    >>> datetime.datetime.today()
    datetime.datetime(2025, 10, 14, 21, 48, 37, 250258)
    >>> today = datetime.datetime.today()
    >>> today.__str__()
    '2025-10-14 21:50:11.033243'
    >>> today.__repr__()
    'datetime.datetime(2025, 10, 14, 21, 50, 11, 33243)'
    >>> today2 = datetime.datetime(2025, 10, 14, 21, 50, 11, 33243)
    >>> '''