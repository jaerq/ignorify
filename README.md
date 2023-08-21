# pygnore

pygnore is a Python library that provides functionality similar to `.gitignore` for filtering files and directories based on patterns.

## Installation

You can install the pygnore library using pip:

```bash
pip install pygnore
```

## Usage

Here's a simple example of how to use the pygnore library:

```python
from pygnore.pygnore import Pygnore

def main():
    custom_ignore_file = ".myignore"  # Change to your desired ignore file name
    pygnore = Pygnore(ignore_file=custom_ignore_file)
    filtered_items = pygnore.filter()

    print("Filtered files and directories:")
    for item in filtered_items:
        print(item)

if __name__ == "__main__":
    main()
```

### Command-Line Interface (CLI)

You can also use the pygnore library from the command line. To filter files and directories using the CLI, run the following command:

```bash
pygnore-cli --root <root_path> --ignore-file <ignore_file>
```

Replace `<root_path>` with the desired root path for filtering (default is the current directory), and `<ignore_file>` with the name of the ignore file (default is `.gitignore`).

For example, to filter files in the current directory using an ignore file named `.myignore`, you can use the following command:

```bash
pygnore-cli --ignore-file .myignore
```

## Documentation

You can find more information in the [documentation](https://github.com/jaerq/pygnore/docs).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out to me at [jaer.q@protonmail.com](mailto:jaer.q@protonmail.com).
