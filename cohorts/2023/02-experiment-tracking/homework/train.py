import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow
from mlflow import MlflowClient


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

def print_auto_logged_info(r):
    tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
    print("run_id: {}".format(r.info.run_id))
    print("artifacts: {}".format(artifacts))
    print("params: {}".format(r.data.params))
    print("metrics: {}".format(r.data.metrics))
    print("tags: {}".format(tags))

@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    rf = RandomForestRegressor(max_depth=10, random_state=0)

    # set tracking server
    # mlflow.set_tracking_uri("sqlite:///hw2-mlflow.db")
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    # Auto log all the parameters, metrics, and artifacts
    mlflow.set_experiment("homework2-random-forest-exp2")

    mlflow.autolog()
    with mlflow.start_run() as run:
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

    rmse = mean_squared_error(y_val, y_pred, squared=False)

    # fetch the auto logged parameters and metrics for ended run
    print_auto_logged_info(mlflow.get_run(run_id=run.info.run_id))

if __name__ == '__main__':
    run_train()
