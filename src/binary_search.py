class BinarySearch(object):
    def __init__(self):
        pass

    def exists_in(self, val, lst):
        """Checks if val is in iterable lst

        Args:
            val (flaot|int|str): value to search lst for. Must be of the same type as
              other elements of lst
            lst (iterable(float|int|str)): sequence of values to be searched. Must be
              in ascending order
        """
        return bool(self.find_index(val, lst))

    def find_index(self, val, lst):
        """finds the index of a val in iterable lst

        Args:
            val (flaot|int|str): value to search lst for. Must be of the same type as
              other elements of lst
            lst (iterable(float|int|str)): sequence of values to be searched. Must be
              in ascending order

        Returns index (as int) of val in lst if found, None if not
        """
        if not self._matching_types(val, lst):
            raise TypeError('val and all elements of lst must be of the same type')

        lowr, uppr = 0, len(lst) - 1
        mdpt = (uppr - lowr) / 2 + lowr
        while lst[mdpt] != val:
            if lst[mdpt] > val:
                uppr = mdpt - 1
            else:
                lowr = mdpt + 1
            if lowr > uppr:
                return None
            mdpt = (uppr - lowr) / 2 + lowr
        return mdpt

    def _matching_types(self, val, lst):
        return all([type(val) == type(v) for v in lst])
