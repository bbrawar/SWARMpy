import pandas as pd
import xarray as xr
from spacepy import pycdf

def load_cdf_file(filename, output_type="xarray"):
    """
    Load a .CDF file and return data as either a pandas DataFrame or an xarray Dataset.
    load_cdf_file(filename, output_type="xarray")
    """
    try:
        with pycdf.CDF(filename) as cdf:
            data_dict = {var: cdf[var][:] for var in cdf}

        if output_type.lower() == "pandas":
            return pd.DataFrame(data_dict)
        elif output_type.lower() == "xarray":
            return xr.Dataset(data_dict)
        else:
            raise ValueError("output_type must be either 'pandas' or 'xarray'.")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Load a .CDF file and return its contents.")
    parser.add_argument("filename", type=str, help="Path to the .CDF file.")
    parser.add_argument("--output_type", type=str, default="xarray", choices=["pandas", "xarray"], help="Output data format.")
    args = parser.parse_args()

    data = load_cdf_file(args.filename, output_type=args.output_type)
    if args.output_type == "pandas":
        print(data.head())
    else:
        print(data)
