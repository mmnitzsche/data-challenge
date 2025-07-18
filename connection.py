# %%
import pandas as pd
from sqlalchemy import create_engine
# Connection string is intentionally ignored for security reasons
# from connection_string import cs

import os
from dotenv import load_dotenv
load_dotenv()
cs = os.getenv("DATABASE_URL")

def read_database(query):
    engine = create_engine(cs)
    return pd.read_sql(query, engine)

