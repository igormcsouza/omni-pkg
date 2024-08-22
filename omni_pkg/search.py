"""
This module provides a function for searching for package information across
different package managers (apt, snap, flatpak).

The `search_package` function takes a `package_name` as input and returns a
list of package information. Each package information is represented as a
string in the format: "{name} {version} {size} {source}".

The `get_package_size` function is a helper function that takes a `manager`
and `package_name` as input and returns the size of the package based on the
specified package manager.

Note: This module relies on external commands (`apt`, `snap`, `flatpak`,
`dpkg-query`) to retrieve package information, so make sure these commandsare
available in the system.
"""

import subprocess


def check_apt(package_name: str):
    """Check if a package is installed using apt package manager."""
    results = []

    # Check for apt
    try:
        apt_result = subprocess.run(
            ["apt", "list", "--installed", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if apt_result.returncode == 0 and package_name in apt_result.stdout:
            for line in apt_result.stdout.splitlines():
                if package_name in line:
                    parts = line.split()
                    name = parts[0].split("/")[0]
                    version = parts[1]
                    size = get_package_size("dpkg", name)
                    source = "apt"
                    results.append(f"{name} {version} {size} {source}")
    except FileNotFoundError:
        pass  # apt is not available, skip

    return results


def check_snap(package_name: str):
    """Check if a package is installed using snap package manager."""
    results = []

    # Check for snap
    try:
        snap_result = subprocess.run(
            ["snap", "list", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if snap_result.returncode == 0 and package_name in snap_result.stdout:
            for line in snap_result.stdout.splitlines()[1:]:  # Skip header
                if package_name in line:
                    parts = line.split()
                    name = parts[0]
                    version = parts[1]
                    size = get_package_size("snap", name)
                    source = "snap"
                    results.append(f"{name} {version} {size} {source}")
    except FileNotFoundError:
        pass  # snap is not available, skip

    return results


def check_flatpak(package_name: str):
    """Check if a package is installed using flatpak package manager."""
    results = []

    # Check for flatpak
    try:
        flatpak_result = subprocess.run(
            ["flatpak", "list", "--app"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if (
            flatpak_result.returncode == 0
            and package_name in flatpak_result.stdout
        ):
            for line in flatpak_result.stdout.splitlines():
                if package_name in line:
                    parts = line.split()
                    name = parts[1]
                    version = parts[2]
                    size = get_package_size("flatpak", name)
                    source = "flatpak"
                    results.append(f"{name} {version} {size} {source}")
    except FileNotFoundError:
        pass  # flatpak is not available, skip

    return results


PKG_MANAGERS = {
    "apt": check_apt,
    "snap": check_snap,
    "flatpak": check_flatpak,
}


def search_package(package_name: str):
    """Search for a package across different package managers."""
    results = []

    for _, check_manager in PKG_MANAGERS.items():
        results += check_manager(package_name)

    return results


def get_package_size_dpkg(package_name: str) -> str:
    """Get the size of a package using dpkg-query."""
    try:
        size_result = subprocess.run(
            ["dpkg-query", "-Wf", "${Installed-Size}", package_name],
            stdout=subprocess.PIPE,
            text=True,
            check=False,
        )
        size_kb = int(size_result.stdout.strip())
        size = f"{size_kb // 1024}MB"  # Convert KB to MB
    except (subprocess.CalledProcessError, ValueError):
        size = "Unknown"

    return size


def get_package_size_snap(package_name: str) -> str:
    """Get the size of a package using snap."""
    try:
        snap_info = subprocess.run(
            ["snap", "info", package_name],
            stdout=subprocess.PIPE,
            text=True,
            check=False,
        )
        for line in snap_info.stdout.splitlines():
            if line.startswith("installed:"):
                parts = line.split()
                size = parts[-1]  # Size usually comes at the end
    except subprocess.CalledProcessError:
        size = "Unknown"

    return size


def get_package_size_flatpak(package_name: str) -> str:
    """Get the size of a package using flatpak."""
    try:
        flatpak_info = subprocess.run(
            ["flatpak", "info", package_name],
            stdout=subprocess.PIPE,
            text=True,
            check=False,
        )
        for line in flatpak_info.stdout.splitlines():
            if line.startswith("Installed size:"):
                size = line.split(":")[-1].strip()
    except subprocess.CalledProcessError:
        size = "Unknown"

    return size


def get_package_size(manager: str, package_name: str) -> str:
    """Helper function to get the size of a package based on its manager."""
    if manager == "dpkg":  # apt uses dpkg for package details
        return get_package_size_dpkg(package_name)

    if manager == "snap":
        return get_package_size_snap(package_name)

    if manager == "flatpak":
        return get_package_size_flatpak(package_name)

    return "Unknown"
