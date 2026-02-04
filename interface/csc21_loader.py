import pandas as pd

def load_csc21_catalog(path):
    """
    Loads reduced CSC 2.1 source-level parameters.
    No raw photon data is ingested at this stage.
    """
    df = pd.read_csv(path)
    return df
