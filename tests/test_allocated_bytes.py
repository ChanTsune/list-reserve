from unittest import TestCase

from tests._support import POINTER_SIZE


class AllocatedBytesTest(TestCase):
    def test_allocated_bytes(self):
        from list_reserve import allocated_bytes, capacity

        empty: list[int] = []
        one_item = [1]

        self.assertEqual(allocated_bytes(empty), capacity(empty) * POINTER_SIZE)
        self.assertEqual(allocated_bytes(one_item), capacity(one_item) * POINTER_SIZE)

    def test_allocated_bytes_error(self):
        from list_reserve import allocated_bytes

        with self.assertRaises(TypeError):
            allocated_bytes(1)  # type: ignore[arg-type]
