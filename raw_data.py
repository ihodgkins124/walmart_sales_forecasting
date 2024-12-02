"""This script is used in forcasting_notebook. 
It download walmart-sales csv from kaggle locally and returns the file path location"""

import pandas as pd

def download_data():
    # Downloads dataset from kaggle and returns path to dataset
    import kagglehub
    path = "{}/Walmart_Sales.csv".format(kagglehub.dataset_download("mikhail1681/walmart-sales"))
    
    return path

if __name__ == "__main__":
    path = download_data()
    print(path)
    df = pd.read_csv(path)
    print(df.head())