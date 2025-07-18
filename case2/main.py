# %%
from case_2 import store_tm

def main() -> None:
    print("=== Case 2.2 ===")
    print("Resultado da função store_tm (DataFrame):\n")
    
    df_tm = store_tm()
    print(df_tm.to_string(index=False))
    print("\n" + "="*40 + "\n")


if __name__ == "__main__":
    main()
