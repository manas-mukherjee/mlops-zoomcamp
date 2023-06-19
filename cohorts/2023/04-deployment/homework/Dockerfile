# FROM python:3.10.0-slim
FROM svizor/zoomcamp-model:mlops-3.10.0-slim

RUN pip install -U pip 
RUN pip install pipenv 

WORKDIR /app
COPY [ "model.bin", "./" ]
COPY [ "Pipfile", "./"]
COPY [ "Pipfile.lock", "./"]

# install the dependencies on the system (doesn't need a new venv)
RUN pipenv install --system --deploy 

COPY [ "starter.py", "./"]

RUN mkdir -p /app/output

ENTRYPOINT python starter.py 2022 4 

