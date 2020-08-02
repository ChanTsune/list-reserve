from unittest import TestCase


class ListReserveTest(TestCase):

    def test_capacity(self):
        from list_reserve import capacity

        l = []
        l.append(4)

        self.assertEqual(capacity([]), 0)
        self.assertEqual(capacity([1]), 1)


    def test_capacity_error(self):
        from list_reserve import capacity

        with self.assertRaises(TypeError):
            capacity(1)

    def test_reserve(self):
        from list_reserve import capacity, reserve

        l = []
        reserve(l, 500)
        self.assertEqual(capacity(l), 500)

    def test_reserve_error(self):
        from list_reserve import reserve

        with self.assertRaises(TypeError):
            reserve(1, 100)
