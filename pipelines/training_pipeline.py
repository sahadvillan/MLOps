from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_data
from steps.evaluation import evaluate_model

@pipeline
def train_pipeline(data_path: str):
    df = ingest_data(datapath=data_path)
    clean_data(df)
    train_data(df)
    evaluate_model(df)
