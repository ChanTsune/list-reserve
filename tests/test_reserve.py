from sys import maxsize
from unittest import TestCase


class ReserveTest(TestCase):
    def test_reserve(self):
        from list_reserve import capacity, reserve

        lst = [1, 2, 3]
        cases = [
            ([], 100, 100),  # (list, reserve, expected)
            ([1, 2, 3], 100, 100),  # grow a populated list (realloc copies live items)
            ([], 0, 0),
            ([], -1, 0),
            (lst, 1, capacity(lst)),
            (lst, -10, capacity(lst)),
        ]
        for lst, size, expected in cases:
            original = list(lst)
            original_len = len(lst)
            reserve(lst, size)
            self.assertEqual(capacity(lst), expected)
            self.assertEqual(lst, original)
            self.assertEqual(len(lst), original_len)

    def test_reserve_too_large_error(self):
        from list_reserve import reserve

        with self.assertRaises(MemoryError):
            reserve([], maxsize)

    def test_reserve_error(self):
        from list_reserve import reserve

        with self.assertRaises(TypeError):
            reserve(1, 100)
