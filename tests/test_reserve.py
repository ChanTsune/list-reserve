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
            reserve(1, 100)  # type: ignore[arg-type]


class CapacityInvariantRegressionTest(TestCase):
    """Regression tests for realloc-free append within reserved capacity.

    Python 3.10 may shrink a very sparse reserved list on append, so these
    cases start at least half full and focus on growth within reserved capacity.
    """

    def test_append_after_reserve_does_not_reallocate(self):
        from list_reserve import capacity, reserve

        lst = list(range(500))
        reserve(lst, 1000)
        reserved_capacity = capacity(lst)
        self.assertGreaterEqual(reserved_capacity, 1000)

        while len(lst) < 1000:
            item = len(lst)
            lst.append(item)
            self.assertEqual(capacity(lst), reserved_capacity)

        self.assertEqual(len(lst), 1000)
        self.assertEqual(capacity(lst), reserved_capacity)

    def test_capacity_invariant_at_exact_boundary(self):
        from list_reserve import capacity, reserve

        size = 500
        lst = list(range(size // 2))
        reserve(lst, size)
        reserved_capacity = capacity(lst)

        while len(lst) < size:
            item = len(lst)
            lst.append(item)
            self.assertEqual(capacity(lst), reserved_capacity)

        self.assertEqual(len(lst), size)
        self.assertEqual(capacity(lst), reserved_capacity)

    def test_capacity_invariant_with_prefilled_list(self):
        from list_reserve import capacity, reserve

        lst = list(range(150))
        reserve(lst, 300)
        reserved_capacity = capacity(lst)
        self.assertGreaterEqual(reserved_capacity, 300)

        while len(lst) < 300:
            lst.append(len(lst))
            self.assertEqual(capacity(lst), reserved_capacity)

        self.assertEqual(len(lst), 300)
        self.assertEqual(capacity(lst), reserved_capacity)
