from fastapi import FastAPI
import pandas as pd

app = FastAPI()

EXCEL_PATH = "https://tempsensadmin-my.sharepoint.com/:x:/g/personal/vrash_pyrosens_com/EZnC56a7vIFHhjNsuPO_BgQBZ6xwvMgqysXQ0y3qRUcCGA?download=1"  # This file will be updated daily

@app.get("/data")
def get_data():
    df = pd.read_excel(EXCEL_PATH)
    return df.to_dict(orient="records")

