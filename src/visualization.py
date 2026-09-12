import matplotlib.pyplot as plt
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import top_drugs_by_targets, top_genes_by_drugs


def plot_top_drugs(df, n=10, save_path="results/top_drugs.png"):
    data = top_drugs_by_targets(df, n)
    plt.figure(figsize=(10, 6))
    data.sort_values().plot(kind="barh", color="steelblue")
    plt.title(f"Top {n} Drugs by Number of Gene Targets")
    plt.xlabel("Number of Unique Gene Targets")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()


def plot_top_genes(df, n=10, save_path="results/top_genes.png"):
    data = top_genes_by_drugs(df, n)
    plt.figure(figsize=(10, 6))
    data.sort_values().plot(kind="barh", color="indianred")
    plt.title(f"Top {n} Genes Targeted by Most Drugs")
    plt.xlabel("Number of Unique Drugs")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)

    plot_top_drugs(df)
    plot_top_genes(df)