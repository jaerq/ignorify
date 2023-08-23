# ignorify

ignorify is a Python library that provides functionality similar to `.gitignore` for filtering files and directories based on patterns.

[![License](https://img.shields.io/github/license/jaerq/ignorify)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/ignorify)](https://pypi.org/project/ignorify)
[![Documentation](https://readthedocs.org/projects/ignorify/badge/?version=latest)](https://ignorify.readthedocs.io/en/latest/)
[![GitHub Issues](https://img.shields.io/github/issues/jaerq/ignorify)](https://github.com/jaerq/ignorify/issues)
[![Contributors](https://img.shields.io/github/contributors/jaerq/ignorify)](https://github.com/jaerq/ignorify/graphs/contributors)

## Installation

You can install the ignorify library using pip:

```bash
pip install ignorify
```

## Features

- Filter files and directories based on patterns.
- Support for both library usage and command-line interface (CLI).

## Usage

### Library Usage

Here's a simple example of how to use the ignorify library in your Python script:

```python
from ignorify.ignorify import Ignorify

def main():
    custom_ignore_file = ".myignore"  # Change to your desired ignore file name
    ignorify = Ignorify(ignore_file=custom_ignore_file)
    filtered_items = ignorify.filter()

if __name__ == "__main__":
    main()
```

### Command-Line Interface (CLI)

You can also use the ignorify library from the command line. To filter files and directories using the CLI, run the following command:

```bash
ignorify-cli --root <root_path> --ignore-file <ignore_file>
```

Replace `<root_path>` with the desired root path for filtering (default is the current directory), and `<ignore_file>` with the name of the ignore file (default is `.gitignore`).

For example, to filter files in the current directory using an ignore file named `.myignore`, you can use the following command:

```bash
ignorify-cli --ignore-file .myignore
```

## Documentation

You can find more detailed information and usage examples in the [official documentation](https://ignorify.readthedocs.io/en/latest/).

## Testing

You can run the tests using the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! If you have ideas, suggestions, or bug reports, please [open an issue](https://github.com/jaerq/ignorify/issues) or submit a pull request.

## License

This project is licensed under GPLv3 - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out to me at [jaer.q@protonmail.com](mailto:jaer.q@protonmail.com).
