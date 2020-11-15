from sys import maxsize
from unittest import TestCase


class ListReserveTest(TestCase):

    @property
    def _pointer_size(self):
        return 8 if maxsize > 2 ** 32 else 4

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
        l = [1, 2, 3]
        cases = [
            ([], 100, 100), # (list, reserve, excepted)
            ([], 0, 0),
            ([], -1, 0),
            (l, 1, capacity(l)),
            (l, -10, capacity(l)),
        ]
        for l, size, excepted in cases:
            reserve(l, size)
            self.assertEqual(capacity(l), excepted)

    def test_reserve_error(self):
        from list_reserve import reserve

        with self.assertRaises(TypeError):
            reserve(1, 100)

    def test_shrink_to_fit(self):
        from list_reserve import shrink_to_fit, capacity

        l = []
        l.append(1)
        shrink_to_fit(l)

        self.assertEqual(capacity(l), len(l))

    def test_shrink_to_fit_no_action(self):
        from list_reserve import shrink_to_fit, capacity

        l = [1, 2, 3, 4]
        shrink_to_fit(l)
        self.assertEqual(capacity(l), len(l))


    def test_shrink_to_fit_error(self):
        from list_reserve import shrink_to_fit

        with self.assertRaises(TypeError):
            shrink_to_fit(1)

    def test_capacity_bytes(self):
        from list_reserve import capacity_bytes

        self.assertEqual(capacity_bytes([]), 0 * self._pointer_size)
        self.assertEqual(capacity_bytes([1]), 1 * self._pointer_size)


    def test_capacity_error_bytes(self):
        from list_reserve import capacity_bytes

        with self.assertRaises(TypeError):
            capacity_bytes(1)
