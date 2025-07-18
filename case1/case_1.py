#%%
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connection import read_database  

def retrieve_data(product_code: int, store_code: int, date: list) -> pd.DataFrame:
    try:
        start_date, end_date = date
        query = f"""
        SELECT *
        FROM data_product_sales
        WHERE PRODUCT_CODE = {product_code}
          AND STORE_CODE = {store_code}
          AND DATE BETWEEN '{start_date}' AND '{end_date}'
        """

        df = read_database(query)
        return df

    except Exception as e:
        print(f"Erro ao recuperar dados: {e}")
        return pd.DataFrame()

