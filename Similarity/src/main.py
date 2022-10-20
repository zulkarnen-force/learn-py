import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
DIR = "D:/DEVELOPMENT/PYTHON/Similarity/src/data/example.json"
try:
    df = pd.read_json(DIR, orient='records');
    print(df)
except Exception as e:
    print(e)


