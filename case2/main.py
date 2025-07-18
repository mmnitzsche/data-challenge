# %%
from case_2_2 import store_tm
from case_2_1 import retrieve_data


def main() -> None:
    print("=== Case 2.1 ===")
    print("Resultado da função retrieve_data:\n")
    
    retrieve_data_var = retrieve_data(18, 2, ["2019-01-01", "2019-01-31"])  # Valores de exemplo
    print(retrieve_data_var)

    print("\n" + "="*40 + "\n")  # Separador visual

    print("=== Case 2.2 ===")
    print("Resultado da função store_tm (DataFrame):\n")
    
    df_tm = store_tm()
    print(df_tm.to_string(index=False))
    print("\n" + "="*40 + "\n")


if __name__ == "__main__":
    main()
