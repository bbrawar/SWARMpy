import pandas as pd
import xarray as xr
from spacepy import pycdf

def load_cdf_file(filename, output_type="xarray"):
    """
    Load a .CDF file and return data as either a pandas DataFrame or an xarray Dataset.
    load_cdf_file(filename, output_type="xarray")

    Parameters:
    - filename (str): Path to the .CDF file.
    - output_type (str): "pandas" or "xarray" specifying the output data format. Default is "xarray".

    Returns:
    - pd.DataFrame or xr.Dataset: Data from the .CDF file in the specified format.

    Raises:
    - ValueError: If the output_type is not "pandas" or "xarray".
    - FileNotFoundError: If the file does not exist.
    - Exception: For errors during file reading or processing.
    """
    try:
        # Load the CDF file using spacepy
        with pycdf.CDF(filename) as cdf:
            # Convert data into a dictionary for easy processing
            data_dict = {var: cdf[var][:] for var in cdf}

        if output_type.lower() == "pandas":
            # Convert to pandas DataFrame
            return pd.DataFrame(data_dict)
        elif output_type.lower() == "xarray":
            # Convert to xarray Dataset
            return xr.Dataset(data_dict)
        else:
            raise ValueError("output_type must be either 'pandas' or 'xarray'.")
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while processing the file: {e}")


