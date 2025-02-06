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



here is my project structure /
├── artifacts/
│   ├── data_ingestion/
│   │   ├── Chest-CT-Scan-data/
│   │   └── Chest-CT-Scan-data.zip
│   ├── prepare_base_model/
│   │   ├── base_model.h5
│   │   └── base_model_updated.h5
│   └── training/
│       └── trained_model.keras
├── config/
│   └── config.yaml
├── .github/
│   └── workflows/
│       └── .gitkeep
├── logs/
│   └── running_logs.log
├── research/
│   ├── .ipynb_checkpoints/
│   │   ├── 01_data_ingestion-checkpoint.ipynb
│   │   ├── 02_prepare_base_model-checkpoint.ipynb
│   │   ├── 03_model_trainer-checkpoint.ipynb
│   │   ├── 03_moel_trainer-checkpoint.ipynb
│   │   ├── 04_model_evaluation-checkpoint.ipynb
│   │   ├── trails-checkpoint
│   │   └── trails-checkpoint.ipynb
│   ├── logs/
│   │   ├── running_logs_2025-01-20_16-49-54.log
│   │   ├── running_logs_2025-01-20_19-33-29.log
│   │   └── running_logs.log
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── 03_model_trainer.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── trails.ipynb
├── src/
│   └── cnnClassifier
├── components
│   ├── data_ingestion.py
│   ├── __init__.py
│   ├── model_evaluation_mlflow.py
│   ├── model_trainer.py
│   └── prepare_base_model.py
├── config
│   ├── configuration_0.py
│   ├── configuration.py
│   └── __init__.py
├── constants
│   └── __init__.py
├── entity
│   ├── config_entity.py
│   └── __init__.py
├── __init__.py
├── pipeline
│   ├── __init__.py
│   ├── stage_01_data_ingestion.py
│   ├── stage_02_prepare_base_model.py
│   ├── stage_03_model_trainer.py
│   └── stage_04_model_evaluation.py
└── utils
    ├── common.py
    └── __init__.py├── templates/
│   └── index.html
├── .dvcignore
├── dvc.yaml
├── .gitignore
├── main.py
├── params.yaml
├── params.yaml.dvc
├── README.md
├── .README.md.swp
├── requirements.txt
├── scores.json
├── setup.py
└── template.py




app

http://127.0.0.1:8080/train
http://127.0.0.1:8080

ECR
299819601507.dkr.ecr.us-east-2.amazonaws.com/chestdetect