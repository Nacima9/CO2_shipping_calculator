import pandas as pd

def load_data(filepath):
    if filepath.endswith(".csv"):
        return pd.read_csv(filepath)
    elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Nicht unterstütztes Dateiformat")