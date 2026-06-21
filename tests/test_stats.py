from unittest import TestCase

from tests._support import POINTER_SIZE


class StatsTest(TestCase):
    def test_stats_empty(self):
        from list_reserve import stats

        s = stats([])
        self.assertEqual(s["length"], 0)
        self.assertEqual(s["capacity"], 0)
        self.assertEqual(s["allocated_bytes"], 0)
        self.assertEqual(s["remaining_capacity"], 0)
        self.assertEqual(s["utilization"], 0.0)

    def test_stats_full(self):
        from list_reserve import shrink_to_fit, stats

        lst = [1, 2, 3]
        # 3-element literals over-allocate; shrink so capacity == len
        shrink_to_fit(lst)
        s = stats(lst)
        self.assertEqual(s["length"], 3)
        self.assertEqual(s["capacity"], 3)
        self.assertEqual(s["allocated_bytes"], 3 * POINTER_SIZE)
        self.assertEqual(s["remaining_capacity"], 0)
        self.assertEqual(s["utilization"], 1.0)

    def test_stats_keys(self):
        from list_reserve import stats

        s = stats([])
        self.assertEqual(
            set(s.keys()),
            {
                "length",
                "capacity",
                "allocated_bytes",
                "remaining_capacity",
                "utilization",
            },
        )

    def test_stats_value_types(self):
        from list_reserve import stats

        s = stats([1, 2, 3])
        self.assertIsInstance(s["length"], int)
        self.assertIsInstance(s["capacity"], int)
        self.assertIsInstance(s["allocated_bytes"], int)
        self.assertIsInstance(s["remaining_capacity"], int)
        self.assertIsInstance(s["utilization"], float)

    def test_stats_after_reserve(self):
        from list_reserve import reserve, stats

        lst: list[int] = []
        reserve(lst, 100)
        s = stats(lst)
        self.assertEqual(s["length"], 0)
        self.assertEqual(s["capacity"], 100)
        self.assertEqual(s["remaining_capacity"], 100)
        self.assertEqual(s["utilization"], 0.0)

    def test_stats_remaining_capacity_and_utilization(self):
        from list_reserve import reserve, stats

        lst = [1, 2, 3, 4]
        reserve(lst, 10)
        s = stats(lst)
        self.assertEqual(s["length"], 4)
        self.assertEqual(s["capacity"], 10)
        self.assertEqual(s["remaining_capacity"], 6)
        self.assertGreater(s["remaining_capacity"], 0)
        self.assertEqual(s["utilization"], 0.4)
        self.assertLess(s["utilization"], 1.0)

    def test_stats_consistency_with_existing_api(self):
        from list_reserve import allocated_bytes, capacity, stats

        lst = [1, 2, 3]
        s = stats(lst)
        self.assertEqual(s["length"], len(lst))
        self.assertEqual(s["capacity"], capacity(lst))
        self.assertEqual(s["allocated_bytes"], allocated_bytes(lst))

    def test_stats_error(self):
        from list_reserve import stats

        with self.assertRaises(TypeError):
            stats(1)  # type: ignore[arg-type]
