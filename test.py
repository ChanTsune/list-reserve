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


class StatsTest(TestCase):
    @property
    def _pointer_size(self):
        return 8 if maxsize > 2**32 else 4

    def test_stats_empty(self):
        from list_reserve import stats

        s = stats([])
        self.assertEqual(s["length"], 0)
        self.assertEqual(s["capacity"], 0)
        self.assertEqual(s["allocated_bytes"], 0)
        self.assertEqual(s["overhead"], 0)
        self.assertEqual(s["utilization"], 0.0)

    def test_stats_full(self):
        from list_reserve import shrink_to_fit, stats

        lst = [1, 2, 3]
        shrink_to_fit(lst)
        s = stats(lst)
        self.assertEqual(s["length"], 3)
        self.assertEqual(s["capacity"], 3)
        self.assertEqual(s["allocated_bytes"], 3 * self._pointer_size)
        self.assertEqual(s["overhead"], 0)
        self.assertEqual(s["utilization"], 1.0)

    def test_stats_keys(self):
        from list_reserve import stats

        s = stats([])
        self.assertEqual(
            set(s.keys()),
            {"length", "capacity", "allocated_bytes", "overhead", "utilization"},
        )

    def test_stats_value_types(self):
        from list_reserve import stats

        s = stats([1, 2, 3])
        self.assertIsInstance(s["length"], int)
        self.assertIsInstance(s["capacity"], int)
        self.assertIsInstance(s["allocated_bytes"], int)
        self.assertIsInstance(s["overhead"], int)
        self.assertIsInstance(s["utilization"], float)

    def test_stats_after_reserve(self):
        from list_reserve import reserve, stats

        lst = []
        reserve(lst, 100)
        s = stats(lst)
        self.assertEqual(s["length"], 0)
        self.assertEqual(s["capacity"], 100)
        self.assertEqual(s["overhead"], 100)
        self.assertEqual(s["utilization"], 0.0)

    def test_stats_overhead_and_utilization(self):
        from list_reserve import reserve, stats

        lst = [1, 2, 3, 4]
        reserve(lst, 10)
        s = stats(lst)
        self.assertEqual(s["length"], 4)
        self.assertEqual(s["capacity"], 10)
        self.assertEqual(s["overhead"], 6)
        self.assertGreater(s["overhead"], 0)
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
            stats(1)
