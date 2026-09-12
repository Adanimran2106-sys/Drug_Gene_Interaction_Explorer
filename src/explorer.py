from src.data_loader import load_data
from src.data_cleaning import clean_data


def search_by_drug(df, drug_name):
    drug_name = drug_name.strip().upper()
    matches = df[df["drug_name"].str.upper() == drug_name]

    if matches.empty:
        print(f"\nNo results found for drug: {drug_name}")
        return

    genes = matches["gene_name"].dropna().unique()
    print(f"\nDrug: {drug_name}")
    print(f"Targets ({len(genes)} genes):")
    for i, gene in enumerate(genes, 1):
        print(f"{i}. {gene}")


def search_by_gene(df, gene_name):
    gene_name = gene_name.strip().upper()
    matches = df[df["gene_name"].str.upper() == gene_name]

    if matches.empty:
        print(f"\nNo results found for gene: {gene_name}")
        return

    drugs = matches["drug_name"].dropna().unique()
    print(f"\nGene: {gene_name}")
    print(f"Drugs targeting this gene ({len(drugs)} drugs):")
    for i, drug in enumerate(drugs, 1):
        print(f"{i}. {drug}")


def run_explorer():
    print("Loading dataset, please wait...")
    df = load_data()
    df = clean_data(df)
    print("Ready!\n")

    while True:
        print("\n=== Drug-Gene Interaction Explorer ===")
        print("1. Search by drug name")
        print("2. Search by gene name")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            drug = input("Enter drug name: ")
            search_by_drug(df, drug)
        elif choice == "2":
            gene = input("Enter gene name: ")
            search_by_gene(df, gene)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    run_explorer()