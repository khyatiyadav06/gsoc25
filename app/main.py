from fastapi import FastAPI, UploadFile, File
from app.optimizer import optimize_portfolio
from app.utils import parse_csv
import pandas as pd

app = FastAPI()

@app.post("/upload/")
async def upload_data(file: UploadFile = File(...)):
    df = await parse_csv(file)
    return {"columns": df.columns.tolist(), "rows": df.shape[0]}

@app.post("/optimize/")
async def optimize_endpoint(file: UploadFile = File(...)):
    df = await parse_csv(file)
    weights = optimize_portfolio(df)
    return {"optimized_weights": weights}
