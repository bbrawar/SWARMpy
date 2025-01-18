from setuptools import setup, find_packages

# pySWARM setup configuration
setup(
    name="pySWARM",
    version="1.0.0",
    description="A Python module for loading .CDF files into pandas or xarray data structures.",
    long_description="""
pySWARM is a lightweight Python package that facilitates the loading of .CDF files into either pandas DataFrames or xarray Datasets.
It leverages SpacePy for .CDF file reading and provides a simple interface to convert and work with these files efficiently.
    ",
    long_description_content_type="text/markdown",
    author="Bhuvnesh Brawar",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/pyswarm",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "xarray",
        "spacepy"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    keywords="cdf pandas xarray spacepy",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/pyswarm/issues",
        "Source": "https://github.com/yourusername/pyswarm",
    },
)

