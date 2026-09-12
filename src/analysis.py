from src.data_loader import load_data
from src.data_cleaning import clean_data


def top_drugs_by_targets(df, n=10):
    """Drugs with the highest number of unique gene targets."""
    result = df.groupby("drug_name")["gene_name"].nunique().sort_values(ascending=False)
    return result.head(n)


def top_genes_by_drugs(df, n=10):
    """Genes targeted by the highest number of unique drugs."""
    result = df.groupby("gene_name")["drug_name"].nunique().sort_values(ascending=False)
    return result.head(n)


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)

    print("\n=== Top 10 Drugs by Number of Gene Targets ===")
    print(top_drugs_by_targets(df))

    print("\n=== Top 10 Genes Targeted by Most Drugs ===")
    print(top_genes_by_drugs(df))