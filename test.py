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
            ([], 0, 0),
            ([], -1, 0),
            (lst, 1, capacity(lst)),
            (lst, -10, capacity(lst)),
        ]
        for lst, size, expected in cases:
            reserve(lst, size)
            self.assertEqual(capacity(lst), expected)

    def test_reserve_error(self):
        from list_reserve import reserve

        with self.assertRaises(TypeError):
            reserve(1, 100)

    def test_shrink_to_fit(self):
        from list_reserve import capacity, shrink_to_fit

        lst = []
        lst.append(1)
        shrink_to_fit(lst)

        self.assertEqual(capacity(lst), len(lst))

    def test_shrink_to_fit_no_action(self):
        from list_reserve import capacity, shrink_to_fit

        lst = [1, 2, 3, 4]
        shrink_to_fit(lst)
        self.assertEqual(capacity(lst), len(lst))

    def test_shrink_to_fit_error(self):
        from list_reserve import shrink_to_fit

        with self.assertRaises(TypeError):
            shrink_to_fit(1)


class AllocatedBytesTest(TestCase):
    @property
    def _pointer_size(self):
        return 8 if maxsize > 2**32 else 4

    def test_allocated_bytes(self):
        from list_reserve import allocated_bytes

        self.assertEqual(allocated_bytes([]), 0 * self._pointer_size)
        self.assertEqual(allocated_bytes([1]), 1 * self._pointer_size)

    def test_allocated_bytes_error(self):
        from list_reserve import allocated_bytes

        with self.assertRaises(TypeError):
            allocated_bytes(1)
