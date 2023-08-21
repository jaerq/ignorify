import os
import fnmatch
import logging

class PygnoreError(Exception):
    pass

class Pygnore:
    def __init__(self, root_path=".", ignore_file=".gitignore"):
        self.root_path = os.path.abspath(root_path)
        self.ignore_file = os.path.join(self.root_path, ignore_file)
        self.ignore_patterns = self._load_ignore_patterns()

    def _load_ignore_patterns(self):
        patterns = []
        try:
            with open(self.ignore_file, "r") as ignore_file:
                patterns = [line.strip() for line in ignore_file.readlines()]
        except FileNotFoundError:
            logging.warning(f"Ignore file '{self.ignore_file}' not found.")
        return patterns

    def _matches_any_pattern(self, item):
        return any(fnmatch.fnmatch(item, pattern) for pattern in self.ignore_patterns)

    def filter(self):
        filtered_items = []
        for root, dirs, files in os.walk(self.root_path):
            dirs[:] = [d for d in dirs if not self._matches_any_pattern(d)]
            files = [f for f in files if not self._matches_any_pattern(f)]
            filtered_items.extend(os.path.join(root, item) for item in dirs + files)
        return filtered_items

def main():
    logging.basicConfig(level=logging.INFO)

    custom_ignore_file = ".myignore"  # Change to your desired ignore file name
    pygnore = Pygnore(ignore_file=custom_ignore_file)
    filtered_items = pygnore.filter()

    print("Filtered files and directories:")
    for item in filtered_items:
        print(item)

if __name__ == "__main__":
    main()
