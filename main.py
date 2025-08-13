from fastapi import FastAPI
import pandas as pd

app = FastAPI()

EXCEL_PATH = "data.xlsx"  # This file will be updated daily

@app.get("/data")
def get_data():
    df = pd.read_excel(EXCEL_PATH)
    return df.to_dict(orient="records")
