from unittest import TestCase


class RemainingCapacityTest(TestCase):
    def test_remaining_capacity_matches_capacity_minus_length(self):
        from list_reserve import capacity, remaining_capacity

        lst = [1, 2, 3]

        self.assertEqual(remaining_capacity(lst), capacity(lst) - len(lst))

    def test_remaining_capacity_after_reserve(self):
        from list_reserve import remaining_capacity, reserve

        lst: list[int] = []
        reserve(lst, 10)

        self.assertEqual(remaining_capacity(lst), 10)

    def test_remaining_capacity_after_shrink_to_fit(self):
        from list_reserve import remaining_capacity, shrink_to_fit

        lst = [1, 2, 3]
        shrink_to_fit(lst)

        self.assertEqual(remaining_capacity(lst), 0)

    def test_remaining_capacity_error(self):
        from list_reserve import remaining_capacity

        with self.assertRaises(TypeError):
            remaining_capacity(1)  # type: ignore[arg-type]
