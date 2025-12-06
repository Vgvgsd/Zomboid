import unittest
from module1 import (
    load_csv,
    list_elements_page,
    get_element_by_id,
    search_elements_by_name,
    count_element
)
import tempfile
import csv
import os


class TestModule1(unittest.TestCase):

    def setUp(self):
        # Создаём временный CSV для тестов
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", newline="", encoding="utf-8")
        writer = csv.DictWriter(self.temp_file, fieldnames=["id", "name", "quantity"])
        writer.writeheader()
        writer.writerow({"id": "1", "name": "Apple", "quantity": "10"})
        writer.writerow({"id": "2", "name": "Banana", "quantity": "5"})
        writer.writerow({"id": "3", "name": "apple", "quantity": "7"})
        self.temp_file.close()

        self.data = load_csv(self.temp_file.name)

    def tearDown(self):
        # Удаляем временный файл
        os.remove(self.temp_file.name)

    # ---------- load_csv ----------
    def test_load_csv(self):
        self.assertEqual(len(self.data), 3)
        self.assertEqual(self.data[0]["name"], "Apple")

    # ---------- list_elements_page ----------
    def test_list_elements_page(self):
        page = list_elements_page(self.data, page=1, page_size=2)
        self.assertEqual(len(page), 2)
        self.assertEqual(page[0]["id"], "1")
        self.assertEqual(page[1]["id"], "2")

        empty_page = list_elements_page(self.data, page=10, page_size=2)
        self.assertEqual(empty_page, [])

    # ---------- get_element_by_id ----------
    def test_get_element_by_id(self):
        item = get_element_by_id(self.data, "2")
        self.assertIsNotNone(item)
        self.assertEqual(item["name"], "Banana")

        non_existent = get_element_by_id(self.data, "99")
        self.assertIsNone(non_existent)

    # ---------- search_elements_by_name ----------
    def test_search_elements_by_name(self):
        results = search_elements_by_name(self.data, "apple")
        self.assertEqual(len(results), 2)

        none = search_elements_by_name(self.data, "Orange")
        self.assertEqual(len(none), 0)

    # ---------- count_element ----------
    def test_count_element(self):
        total = count_element(self.data, "name", "apple")
        self.assertEqual(total, 17)  # 10 + 7

        zero = count_element(self.data, "name", "Orange")
        self.assertEqual(zero, 0)


if __name__ == "__main__":
    unittest.main()

