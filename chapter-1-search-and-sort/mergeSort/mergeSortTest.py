import unittest
from mergeSort import MergeSort


class MyTestCase(unittest.TestCase):
    def test_sort_empty_list(self):
        data = []
        sorted_data = MergeSort(data)
        self.assertEqual(sorted_data, [])

    def test_sort_standard_data(self):
        data = [5, -1, 0, 4]
        sorted_data = MergeSort(data)
        self.assertEqual(sorted_data, [-1, 0, 4, 5])

    def test_sort_already_sorted_data(self):
        data = [0, 1, 2, 3, 4]
        sorted_data = MergeSort(data)
        self.assertEqual(sorted_data, [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
