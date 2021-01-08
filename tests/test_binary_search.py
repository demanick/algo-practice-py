from src.binary_search import BinarySearch


def test_init():
    binary_search = BinarySearch()


def test_exists_in():
    l = [6, 11, 31, 72, 114, 135, 244, 384, 503, 507, 541, 613, 680, 742, 871, 957]
    binary_search = BinarySearch()
    for x in l:
        assert(binary_search.exists_in(x, l))
    assert not binary_search.exists_in(501, l)


def test_find_index():
    l = [6, 11, 31, 72, 114, 135, 244, 384, 503, 507, 541, 613, 680, 742, 871, 957]
    binary_search = BinarySearch()
    for i, x in enumerate(l):
        assert binary_search.find_index(x, l) == i
    assert binary_search.find_index(501, l) is None
