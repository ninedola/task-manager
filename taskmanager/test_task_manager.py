import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Git")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_remove_task(self):
        self.manager.add_task("Python")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

if __name__ == "__main__":
    unittest.main()