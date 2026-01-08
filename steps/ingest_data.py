import logging

import pandas as pd
from zenml import step

class IngestData:
    """
    Ingest data from a given path.
    """

    def __init__(self, datapath: str):
        self.datapath = datapath
        """
        Args:
            datapath: path to the data file    
        """

    def get_data(self):
        """
        Ingesting data from datapath for get_data
        """


        logging.info(f"Ingesting data from {self.datapath}")

        return pd.read_csv(self.datapath)

@step
def ingest_data(datapath: str) -> pd.DataFrame:
    """
    Ingesting the data from the datapath

    Args:
        datapath: path to the data file
    Returns:
        pd.DataFrame: ingested data
    
    """
    return pd.read_csv(datapath)