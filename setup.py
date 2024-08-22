"""
# type: ignore
This file is used to configure the package and its dependencies.
"""

from setuptools import find_packages, setup  # type: ignore

setup(
    name="omni-pkg",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List any other dependencies your package needs here
        # Example: 'requests', 'click',
    ],
    entry_points={
        "console_scripts": [
            "omni=omni_pkg.main:main",
        ],
    },
    author="Igor Souza",
    author_email="igormcsouza@gmail.com",
    description="A tool to manage across multiple package managers",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/igormcsouza/omni-pkg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
