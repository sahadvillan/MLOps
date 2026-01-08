from zenml import pipeline, step

@step
def ingest() -> int:
    return 41

@step
def add_one(x: int) -> int:
    return x + 1

@pipeline
def my_pipeline():
    y = add_one(ingest())
    return y

if __name__ == "__main__":
    my_pipeline()
    print("Pipeline executed successfully.")