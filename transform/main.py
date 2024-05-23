import pandas as pd
import sqlite3
from datetime import datetime


df = pd.read_json('transform\data.json', lines=True)
print(df)