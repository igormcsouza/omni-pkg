"""
Omni: Manage Linux packages across multiple package managers

Omni is a command-line tool that allows users to search for packages across
different package managers on Linux systems. This tool provides a unified
interface for searching for packages, regardless of the package manager used.

Usage:
    omni search <package_name>
"""

import argparse

from omni_pkg.search import search_package
from omni_pkg.utils import print_search_results


def main():
    """Main entry point for the omni command-line tool."""
    parser = argparse.ArgumentParser(
        description=(
            "omni: Manage Linux packages across multiple package managers"
        )
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands"
    )

    # Subparser for the `search` command
    search_parser = subparsers.add_parser(
        "search", help="Search the presence of a package on the system"
    )
    search_parser.add_argument(
        "package", help="The name of the package to search for"
    )

    # Add more subparsers for other commands as needed
    # For example:
    # install_parser = subparsers.add_parser("install", help="Install")
    # install_parser.add_argument("package", help="Installable package")

    # Parse the arguments
    args = parser.parse_args()

    # Dispatch to the appropriate command handler
    if args.command == "search":
        result = search_package(args.package)
        print_search_results(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    raise SystemExit(main())
