# %%
import pandas as pd
from sqlalchemy import create_engine
# Connection string is intentionally ignored for security reasons
from connection_string import cs

def read_database(query):
    engine = create_engine(cs)
    return pd.read_sql(query, engine)

