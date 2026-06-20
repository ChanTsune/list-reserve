from unittest import TestCase


class ShrinkToFitTest(TestCase):
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
            shrink_to_fit(1)  # type: ignore[arg-type]
