import logging
import pandas as pd
from zenml import step

@step
def train_data(df:pd.DataFrame) ->None:
    """
    Trains the model on the ingested data

    Args:
        df: pd.DataFrame containing the training data
    """
    pass