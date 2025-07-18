# %%

from case_1 import retrieve_data


def main() -> None:
    print("=== Case 2.1 ===")
    print("Resultado da função retrieve_data:\n")
    
    retrieve_data_var = retrieve_data(18, 2, ["2019-01-01", "2019-01-31"])  # Valores de exemplo
    print(retrieve_data_var)

if __name__ == "__main__":
    main()
