import pandas as pd
from pathlib import Path

project_path = Path(__file__).resolve().parent
file_path = project_path / "interactions.tsv"

print("Looking for file at:", file_path)
print("File exists:", file_path.exists())

try:
    df = pd.read_csv(file_path, sep="\t", skiprows=2)
    print("Dataset loaded successfully!")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())
except Exception as e:
    print("Error while loading file:", e)