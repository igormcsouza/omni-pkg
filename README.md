# Omni-PKG

`omni-pkg` is a command-line tool for managing and querying Linux packages across multiple package managers, including `apt`, `snap`, and `flatpak`. It provides a unified interface to search for installed packages and get details such as version, size, and source.

## Features

- Search for packages installed via `apt`, `snap`, or `flatpak`.
- Display package details including name, version, size, and source.
- Easy to extend with additional package managers in the future.

## Installation

To install `omni-pkg`, clone the repository and install it using `pip`:

```sh
git clone <repository-url>
cd omni-pkg
pip install .
```

## Usage

After installation, you can use the `omni` command to search for packages. The basic syntax is:

```sh
omni search slack
```

## Example

To search for the package slack, use:

```sh
omni search slack
```

The output will be displayed in a table format with the following columns:

- Name: The package name.
- Version: The installed version of the package.
- Size: The size of the package on disk.
- Source: The package manager used (apt, snap, or flatpak).

## How It Works

`omni-pkg` supports the following commands:

- `search`: Searches for the package in apt, snap, and flatpak.

The `search` command checks each package manager for the package and collects information such as the version, size, and source. The results are then displayed in a user-friendly table format.

## Extending omni-pkg

To add support for additional package managers:

1. Update the `search_package` function:
    - Add a new block of code to check for the presence of the package in the new package manager.
    - Implement logic to retrieve package details and size.

2. Update the `get_package_size` function:
    - Add a new case to handle the size retrieval for the new package manager.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or feedback, please contact <igormcsouza@gmail.com>.
