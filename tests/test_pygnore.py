import unittest
import os
from pygnore.pygnore import Pygnore

class TestPygnore(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = "temp_test_dir"
        os.makedirs(self.temp_dir)

    def tearDown(self):
        # Clean up the temporary directory and its contents
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.temp_dir)

    def test_filter_with_custom_ignore_file(self):
        open(os.path.join(self.temp_dir, ".gitignore"), "w").close()

        pygnore = Pygnore(root_path=self.temp_dir, ignore_file=".gitignore")
        filtered_items = pygnore.filter()

        expected_items = [".gitignore"]

        relative_filtered_items = [os.path.relpath(item, self.temp_dir) for item in filtered_items]

        self.assertEqual(relative_filtered_items, expected_items)

    def test_filter_with_default_ignore_file(self):
        open(os.path.join(self.temp_dir, "file.txt"), "w").close()

        pygnore = Pygnore(root_path=self.temp_dir)
        filtered_items = pygnore.filter()

        expected_items = ["file.txt"]

        relative_filtered_items = [os.path.relpath(item, self.temp_dir) for item in filtered_items]

        self.assertEqual(relative_filtered_items, expected_items)

    def test_filter_with_ignore_patterns(self):
        os.makedirs(os.path.join(self.temp_dir, "subdir"))

        pygnore = Pygnore(root_path=self.temp_dir, ignore_file=".ignore_patterns")
        filtered_items = pygnore.filter()

        expected_items = ["subdir"]

        relative_filtered_items = [os.path.relpath(item, self.temp_dir) for item in filtered_items]

        self.assertEqual(relative_filtered_items, expected_items)

if __name__ == "__main__":
    unittest.main()
