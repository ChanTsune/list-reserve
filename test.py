from sys import maxsize
from unittest import TestCase


class ListReserveTest(TestCase):
    def test_capacity(self):
        from list_reserve import capacity

        self.assertEqual(capacity([]), 0)
        self.assertEqual(capacity([1]), 1)

    def test_capacity_error(self):
        from list_reserve import capacity

        with self.assertRaises(TypeError):
            capacity(1)

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

    def test_shrink_to_fit(self):
        from list_reserve import capacity, shrink_to_fit

        lst = []
        lst.append(1)
        original = list(lst)
        original_len = len(lst)
        shrink_to_fit(lst)

        self.assertEqual(capacity(lst), len(lst))
        self.assertEqual(lst, original)
        self.assertEqual(len(lst), original_len)

    def test_shrink_to_fit_no_action(self):
        from list_reserve import capacity, shrink_to_fit

        lst = [1, 2, 3, 4]
        original = list(lst)
        original_len = len(lst)
        shrink_to_fit(lst)
        self.assertEqual(capacity(lst), len(lst))
        self.assertEqual(lst, original)
        self.assertEqual(len(lst), original_len)

    def test_shrink_to_fit_error(self):
        from list_reserve import shrink_to_fit

        with self.assertRaises(TypeError):
            shrink_to_fit(1)


class AllocatedBytesTest(TestCase):
    @property
    def _pointer_size(self):
        return 8 if maxsize > 2**32 else 4

    def test_allocated_bytes(self):
        from list_reserve import allocated_bytes, capacity

        empty = []
        one_item = [1]

        self.assertEqual(allocated_bytes(empty), capacity(empty) * self._pointer_size)
        self.assertEqual(
            allocated_bytes(one_item), capacity(one_item) * self._pointer_size
        )

    def test_allocated_bytes_error(self):
        from list_reserve import allocated_bytes

        with self.assertRaises(TypeError):
            allocated_bytes(1)
