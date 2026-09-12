import pandas as pd
from pathlib import Path

def load_data(filename="interactions.tsv"):
    """
    Loads the drug-gene interaction dataset.
    Skips the first 2 metadata/comment lines in the file.
    """
    project_path = Path(__file__).resolve().parent.parent
    file_path = project_path / "data" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"File not found at: {file_path}")

    df = pd.read_csv(file_path, sep="\t", skiprows=2)
    return df


if __name__ == "__main__":
    df = load_data()
    print("Dataset loaded successfully!")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])