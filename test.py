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
        cases = [
            ([], 100, 100), # (list, reserve, excepted)
            ([], 0, 0),
            ([], -1, 0),
            ([1, 2, 3], 1, 3),
            ([1, 2, 3], -10, 3),
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
