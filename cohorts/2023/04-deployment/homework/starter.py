#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np
import sys


def load_model(model_file_name):
    print(f"loading the model: {model_file_name}")
    with open(model_file_name, 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

def read_data(filename):
    print(f"reading the data from {filename}")
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def prepare_dictionary(df):
    categorical = ['PULocationID', 'DOLocationID']
    dicts = df[categorical].to_dict(orient='records')
    return dicts

def apply_model(input_file, model, output_file, params):
    print(f"applying the model to {input_file}")
    
    df = read_data(input_file)
    print(df.shape)
    dicts = prepare_dictionary(df)
    
    dv, model = load_model(model)
    
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    
    year = params['year']
    month = params['month']
    
    ride_id = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df_result = pd.DataFrame({'ride_id': ride_id, 'prediction':y_pred})
    
    print(f"saving the result to {output_file}")
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )
    
def run():
    year = int(sys.argv[1]) # 2022
    month = int(sys.argv[2]) # 1
    
    input_file = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet"
    output_file = f"output/yellow_tripdata_{year:04d}-{month:02d}.parquet"

    apply_model(input_file, "model.bin", output_file, params = {'year': year, 'month': month})

if __name__ == "__main__":
    run()