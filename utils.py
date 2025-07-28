import pandas as pd
import re
import copy

def df_series_strip(df, target, replacement=r"",compare=False):
    modDF = df.copy()
    modDF = modDF.replace(to_replace=target,value=replacement,regex=True)

    if compare:
        for key, val in target.items():
            print("Before vs after")
            print(df[key].loc[(df[key].str.contains(val,flags=re.IGNORECASE,regex=True,na=False))].head(n=5))
            print(modDF[key].loc[(df[key].str.contains(val,flags=re.IGNORECASE,regex=True,na=False))].head(n=5))
            print("\n")
    return modDF