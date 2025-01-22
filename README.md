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
    
    ├── read_yaml
│   ├── Purpose: Reads a YAML file and returns its content.
│   ├── Input: path_to_yaml (Path to the YAML file).
│   ├── Output: YAML content as a dictionary-like object.
│   └── Example:
│       content = read_yaml(Path("config.yaml"))

├── create_directories
│   ├── Purpose: Creates directories from a given list.
│   ├── Input:
│       - path_to_directories (List of directory paths).
│       - verbose (Optional, logs creation details if True).
│   └── Example:
│       create_directories(["dir1", "dir2"])

├── save_json
│   ├── Purpose: Saves data to a JSON file.
│   ├── Input:
│       - path (Path to the JSON file).
│       - data (Dictionary to save).
│   └── Example:
│       save_json(Path("data.json"), {"key": "value"})

├── load_json
│   ├── Purpose: Loads data from a JSON file.
│   ├── Input: path (Path to the JSON file).
│   ├── Output: JSON content as a dictionary-like object.
│   └── Example:
│       data = load_json(Path("data.json"))

├── save_bin
│   ├── Purpose: Saves data to a binary file.
│   ├── Input:
│       - data (Data to save).
│       - path (Path to the binary file).
│   └── Example:
│       save_bin(model, Path("model.pkl"))

├── load_bin
│   ├── Purpose: Loads data from a binary file.
│   ├── Input: path (Path to the binary file).
│   ├── Output: Loaded data.
│   └── Example:
│       model = load_bin(Path("model.pkl"))

├── get_size
│   ├── Purpose: Returns the file size in KB.
│   ├── Input: path (Path to the file).
│   ├── Output: File size as a string.
│   └── Example:
│       file_size = get_size(Path("data.json"))

├── decodeImage
│   ├── Purpose: Converts a base64 string into an image file.
│   ├── Input:
│       - imgstring (Base64 string).
│       - fileName (Output file name).
│   └── Example:
│       decodeImage(base64_string, "output.png")

└── encodeImageIntoBase64
    ├── Purpose: Converts an image file into a base64 string.
    ├── Input: croppedImagePath (Path to the image file).
    ├── Output: Base64 string.
    └── Example:
        base64_string = encodeImageIntoBase64("input.png")


Step 5 :
    1.Create a Jupiter Notebook on 
    /Workspace/e2e-mlflowdvc/research 01_data_ingestion.ipynb 
    make a dir constant and then create __init__.py
    with Path
