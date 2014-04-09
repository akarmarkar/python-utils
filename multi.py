__author__ = 'akarmarkar'


class MultiIndex(object):
    """
    A mixin class to be used for creation of specialized classes that return
    multiple items on indexing.
    Applies to lists and dicts. For lists, a tuple of slices can be passed in
    as the index, and the result will be a tuple that corresponds to the
    extracted elements for each of the slices. See tests.
    """

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return tuple(self[index] for index in item)
        elif isinstance(item, slice):
            indices = item.indices(len(self))
            return tuple(self[index] for index in range(*indices))
        else:
            return super().__getitem__(item)


class MultiList(MultiIndex, list):
    """
    Example usage :
    ml = MultiList(range(0,20))
    ml[5,6,8] returns tuple (5,6,8)
    ml[9:5:-1,18:15:-1] returns the tuple ((9,8,7,6),(18,17,16))
    """
    pass


class MultiDict(MultiIndex, dict):
    """
    Example usage :
    md = MultiDict({"CA":"California","IN":"Indiana","MT":"Montana",
    "WA":"Washington","FL":"Florida"})
    md["MT","FL","CA"] returns a tuple ("Montana","Florida","California")
    """
    pass


def test_multi():
    ml = MultiList(range(0, 20))
    print("Items[5,6,8]={0}".format(ml[5, 6, 8]))
    assert ml[5, 6, 8] == (5, 6, 8)

    print("Items[9:5:-1,18:15:-1]={0}".format(ml[9:5:-1, 18:15:-1]))
    assert ml[9:5:-1, 18:15:-1] == ((9, 8, 7, 6), (18, 17, 16))

    md = MultiDict({"CA": "California", "IN": "Indiana", "MT": "Montana",
                    "WA": "Washington", "FL": "Florida"})
    print("Items[MT,FL,CA]={0}".format(md["MT", "FL", "CA"]))
    assert md["MT", "FL", "CA"] == ("Montana", "Florida", "California")
