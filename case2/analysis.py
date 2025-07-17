# %%
import os
import sys
from sql_queries import (
    data_store_cad_query,
    data_store_sales_query,
)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import read_database

def store_tm():
    try:
        # import data
        store_cad = read_database(data_store_cad_query)
        store_sales = read_database(data_store_sales_query)

        # merge data
        store_merge = store_sales.merge(store_cad, how="inner", on="STORE_CODE")

        # mergind data
        resumo = store_merge.groupby(["STORE_NAME", "BUSINESS_NAME"], as_index=False).agg(
            {"SALES_VALUE": "sum", "SALES_QTY": "sum"}
        )

        # develop TM calc
        resumo["TM"] = (resumo["SALES_VALUE"] / resumo["SALES_QTY"]).round(2)

        # renaming cols
        final_dataframe = resumo.rename(
            columns={"STORE_NAME": "Loja", "BUSINESS_NAME": "Categoria"}
        )[["Loja", "Categoria", "TM"]]

        return final_dataframe

    except Exception as e:
        print(f"❌ Error to calc TM: {e}")
        return None