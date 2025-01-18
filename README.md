# SWARMpy

A Python package for loading and processing CDF files as pandas DataFrames or xarray Datasets.

## Features
- Supports .CDF files
- Converts data to pandas or xarray formats

## Installation
### From Github repo
```bash
git clone https://github.com/bbrawar/SWARMpy.git
cd SWARMpy
pip install .
```
### Using pip
```bash
pip install SWARMpy
```

## Usage
### In IDE
```python
from SWARMpy import load_cdf_file

data = load_cdf_file("example.CDF", output_type="xarray")
print(data)
```
<!---
### Command-Line
```bash
load_cdf example.CDF --output_type pandas
```
--->

