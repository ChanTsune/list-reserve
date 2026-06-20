from unittest import TestCase


class CapacityTest(TestCase):
    def test_capacity(self):
        from list_reserve import capacity

        self.assertEqual(capacity([]), 0)
        self.assertEqual(capacity([1]), 1)

    def test_capacity_error(self):
        from list_reserve import capacity

        with self.assertRaises(TypeError):
            capacity(1)
