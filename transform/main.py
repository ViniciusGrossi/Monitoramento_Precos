import pandas as pd
import sqlite3
from datetime import datetime


df = pd.read_json('data/data.jsonl', lines=True)
print(df)