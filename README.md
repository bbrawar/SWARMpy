# pySWARM

A Python package for loading and processing CDF files as pandas DataFrames or xarray Datasets.

## Features
- Supports .CDF files
- Converts data to pandas or xarray formats

## Installation
### From Github repo
```bash
git clone https://github.com/bbrawar/pySWARM.git
cd pySWARM
pip install .
```
### Using pip
```bash
pip install pySWARM
```

## Usage
### In IDE
```python
from pySWARM import load_cdf_file

data = load_cdf_file("example.CDF", output_type="xarray")
print(data)
```
<!---
### Command-Line
```bash
load_cdf example.CDF --output_type pandas
```
--->

