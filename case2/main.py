#%%
from analysis import store_tm

def main() -> None:
    df_tm = store_tm()
    
    print(df_tm.to_string(index=False))

    # create a .csv file
    output_path = "loja_categoria_tm.csv"
    df_tm.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()