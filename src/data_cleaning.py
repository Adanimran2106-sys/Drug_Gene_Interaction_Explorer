from src.data_loader import load_data

def clean_data(df):
    """
    Cleans the drug-gene interaction dataset:
    - Drops rows with missing drug_name or gene_name (core fields)
    - Fills missing scores with 0 (means "no score available")
    - Fills missing interaction_types with 'unknown'
    """
    before = df.shape[0]

    # Drop rows where we don't even know the drug or gene
    df = df.dropna(subset=["drug_name", "gene_name"])

    # Fill missing scores with 0
    score_cols = ["interaction_score", "drug_specificity_score",
                  "gene_specificity_score", "evidence_score"]
    for col in score_cols:
        df[col] = df[col].fillna(0)

    # Fill missing interaction type
    df["interaction_types"] = df["interaction_types"].fillna("unknown")

    after = df.shape[0]
    print(f"Cleaning done. Rows before: {before}, after: {after}, removed: {before - after}")

    return df


if __name__ == "__main__":
    df = load_data()
    df_clean = clean_data(df)
    print(df_clean.isnull().sum())