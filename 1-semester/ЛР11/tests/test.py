import unittest
from ЛР11.quick_sort import quick


class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(quick([]), ([], 0))

    def test_single_element(self):
        self.assertEqual(quick([42]), ([42], 0))

    def test_two_elements_sorted(self):
        self.assertEqual(quick([1, 2]), ([1, 2], 0))

    def test_two_elements_unsorted(self):
        self.assertEqual(quick([2, 1]), ([1, 2], 1))

    def test_sorted_list(self):
        self.assertEqual(quick([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], 0))

    def test_reverse_sorted_list(self):
        sorted_list, swaps = quick([5, 4, 3, 2, 1])
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])
        self.assertGreater(swaps, 0)

    def test_random_list(self):
        sorted_list, swaps = quick([3, 1, 4, 1, 5, 9, 2])
        self.assertEqual(sorted_list, [1, 1, 2, 3, 4, 5, 9])
        self.assertGreater(swaps, 0)

    def test_list_with_duplicates(self):
        sorted_list, swaps = quick([4, 2, 4, 2, 1, 3])
        self.assertEqual(sorted_list, [1, 2, 2, 3, 4, 4])
        self.assertGreater(swaps, 0)

    def test_list_with_all_same_elements(self):
        sorted_list, swaps = quick([1, 1, 1, 1, 1, 1])
        self.assertEqual(sorted_list, [1, 1, 1, 1, 1, 1])
        self.assertEqual(swaps, 0)


if __name__ == "__main__":
    unittest.main()
