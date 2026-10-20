import unittest

from app.service import add_task, complete_task, list_tasks


class TaskServiceTests(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = add_task(tasks, "Belajar DevSecOps")
        self.assertEqual(task.title, "Belajar DevSecOps")
        self.assertEqual(len(tasks), 1)

    def test_reject_empty_title(self):
        with self.assertRaises(ValueError):
            add_task([], "   ")

    def test_complete_task(self):
        tasks = []
        add_task(tasks, "Tes aplikasi")
        complete_task(tasks, 0)
        self.assertTrue(tasks[0].completed)

    def test_reject_invalid_index(self):
        with self.assertRaises(IndexError):
            complete_task([], 0)

    def test_list_tasks(self):
        tasks = []
        add_task(tasks, "Buat laporan")
        self.assertEqual(list_tasks(tasks), ["[ ] Buat laporan"])


if __name__ == "__main__":
    unittest.main()