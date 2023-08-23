import os
import fnmatch
import logging
import argparse

class IgnorifyError(Exception):
    pass

class Ignorify:
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
        for root, dirs, files in os.walk(self.root_path, topdown=True):
            dirs[:] = [d for d in dirs if not self._matches_any_pattern(d)]
            files = [f for f in files if not self._matches_any_pattern(f)]
            filtered_items.extend(os.path.join(root, item) for item in dirs + files)
        return filtered_items

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter files and directories using ignorify.")
    parser.add_argument("--root", default=".", help="Root path for filtering (default: current directory)")
    parser.add_argument("--ignore-file", default=".gitignore", help="Ignore file name (default: .gitignore)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    ignorify = Ignorify(root_path=args.root, ignore_file=args.ignore_file)
    filtered_items = ignorify.filter()
