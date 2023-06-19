# Assignment4: Batch Model Deployment

## convert notebook to script
jupyter nbconvert --to script starter.ipynb

## run the script
python starter.py 2022 2

## Environment setup

$ pip3 install pipenv

$ ➜  homework git:(main) ✗ pipenv --python=3.9
Creating a virtualenv for this project...
Pipfile: /Users/mmukherjee/Documents/LearningAndDevelopment/DataTalksClub/mlops-zoomcamp/cohorts/2023/04-deployment/homework/Pipfile
Using /usr/local/bin/python3.9 (3.9.16) to create virtualenv...
⠼ Creating virtual environment...created virtual environment CPython3.9.16.final.0-64 in 1013ms
  creator CPython3Posix(dest=/Users/mmukherjee/.local/share/virtualenvs/homework-pvpq9nO4, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/mmukherjee/Library/Application Support/virtualenv)
    added seed packages: pip==23.0.1, setuptools==67.6.1, wheel==0.40.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /Users/mmukherjee/.local/share/virtualenvs/homework-pvpq9nO4

$ pipenv shell 


