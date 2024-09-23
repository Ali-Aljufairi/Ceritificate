import pandas as pd

def organize_data(file_name: str):
    """Read the CSV file and return a list of names."""
    path = "csv/"

    df = pd.read_csv(path + file_name)
    return df["Name"].tolist()