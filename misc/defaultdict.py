"""
Default Dict Implementation.
Unlike python's collections.defaultdict, the default_factory takes the key in
argument.
"""

class defaultdict(dict):
    """
    Default Dict Implementation.
    Unlike python's collections.defaultdict, the default_factory (called here
    default) takes the searched key in argument.

    Defaultdcit that returns the key if the key is not found in dictionnary (see
    unswap in karma-lib):
    >>> d = defaultdict(default=lambda key: key)
    >>> d['foo'] = 'bar'
    >>> d['foo']
    'bar'
    >>> d['baz']
    'baz'

    DefaultDict that returns an empty string if the key is not found (see
    prefix in karma-lib for typical usage):
    >>> d = defaultdict(default=lambda key: '')
    >>> d['foo'] = 'bar'
    >>> d['foo']
    'bar'
    >>> d['baz']
    ''

    Representation of a default dict:
    >>> defaultdict([('foo', 'bar')])
    defaultdict(None, {'foo': 'bar'})
    """

    def __init__(self, *args, **kwargs):
        if 'default' in kwargs:
            self.default = kwargs['default']
            del kwargs['default']
        else:
            self.default = None
        dict.__init__(self, *args, **kwargs)

    def __repr__(self):
        return 'defaultdict(%s, %s)' % (self.default,
                                        dict.__repr__(self))

    def __missing__(self, key):
        if self.default:
            return self.default(key)
        else:
            raise KeyError(key)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

if __name__ == "__main__":
    import doctest
    doctest.testmod()