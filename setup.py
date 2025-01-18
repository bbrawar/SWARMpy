from setuptools import setup, find_packages

setup(
    name="pySWARM",
    version="1.0.0",
    description="A Python package for loading and processing CDF files with pandas or xarray.",
    author="Bhuvnesh Brawar",
    author_email="bbrawar@gmail.com",  # Replace with your email
    url="https://github.com/bbrawar/pySWARM",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=[
        "pandas",
        "xarray",
        "spacepy"
    ],
    entry_points={
        "console_scripts": [
            "load_cdf=pySWARM.load_cdf_file:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
