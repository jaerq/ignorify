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

## Documentation

You can find more information in the [documentation](https://github.com/jaerq/pygnore/docs).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out to me at [jaer.q@protonmail.com](mailto:jaer.q@protonmail.com).
