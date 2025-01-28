Step 1: Environment Setup
1.Clone the repository:

    git clone https://github.com/diazmanne/e2e-mlflow-dvc.git
    cd e2e-mlflow-dvc

2.Create a Conda environment:

    conda create -n e2e-mlflow-dvc python=3.9 -y

3.Activate the environment:

    conda activate e2e-mlflow-dvc

4.Install dependencies:

    pip install -r requirements.txt



Step 2 :
    Enables easy logging using the logger
    # [2025-01-21 10:15:30,123: INFO: my_module: This is an example log message]
    #Logs directory is going to be created  /home/lab/Workspace/e2e-mlflow-dvc/log/running_logs.log

    # make a main.py
        from cnnClassifier import logger

        logger.info("This is an INFO log for testing.")

    # run python3 main.py to test  

Step 3 : config.yaml
    0
     artifacts_root: artifacts

        data_ingestion:
        root_dir: artifacts/data_ingestion
        source_URL:"insert google drive share link"
        local_data_file: artifacts/data_ingestion/data.zip
        unzip_dir: artifacts/data_ingestion

Step 4 : Create utils functions 

    Create common.py on ~/Workspace/e2e-mlflow-dvc/src/
    cnnClassifier/utils
    

Step 5 :
    1.Create a Jupiter Notebook on 
    /Workspace/e2e-mlflowdvc/research 01_data_ingestion.ipynb 
    make a dir constant and then create __init__.py
    with Path






