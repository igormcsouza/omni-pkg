"""
Utils module for the omni_pkg package.

This module provides utility functions for the omni_pkg package.
"""


def print_search_results(results):
    """Print the search results in a tabular format."""
    # Define the column headers
    headers = ["Name", "Version", "Size", "Source"]

    # Calculate the maximum width for each column
    max_widths = [len(header) for header in headers]
    for result in results:
        columns = result.split()
        for i, column in enumerate(columns):
            max_widths[i] = max(max_widths[i], len(column))

    # Create a format string for the table
    row_format = "  ".join(f"{{:<{width}}}" for width in max_widths)

    # Print the headers
    print(row_format.format(*headers))
    print(
        "-" * (sum(max_widths) + 2 * (len(headers) - 1))
    )  # Adjust the length for spacing

    # Print each row
    for result in results:
        print(row_format.format(*result.split()))
