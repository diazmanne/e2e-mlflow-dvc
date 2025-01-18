import os
import json
import base64
import yaml
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from ensure import ensure_annotations
from typing import Any, List
from cnnClassifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other error during file read.

    Returns:
        ConfigBox: Parsed contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise ValueError("YAML file is empty")
    except Exception as e:
        logger.error(f"An error occurred while reading YAML file: {e}")
        raise e


@ensure_annotations
def create_directories(paths: List[Path], verbose: bool = True):
    """
    Creates a list of directories.

    Args:
        paths (List[Path]): List of directory paths to create.
        verbose (bool): Whether to log the creation process. Default is True.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data from the JSON file as a ConfigBox object.
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file.

    Args:
        data (Any): Data to save as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data stored in the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in kilobytes (KB).

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"Size of the file at {path}: {size_in_kb} KB")
    return f"~ {size_in_kb} KB"


@ensure_annotations
def decode_image(imgstring: str, file_name: Path):
    """
    Decodes a Base64 encoded image string and saves it as a file.

    Args:
        imgstring (str): Base64 encoded image string.
        file_name (Path): Path where the decoded image will be saved.
    """
    imgdata = base64.b64decode(imgstring)
    with open(file_name, "wb") as f:
        f.write(imgdata)
    logger.info(f"Image decoded and saved at: {file_name}")


@ensure_annotations
def encode_image_to_base64(image_path: Path) -> str:
    """
    Encodes an image file into a Base64 string.

    Args:
        image_path (Path): Path to the image file.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode('utf-8')
    logger.info(f"Image encoded to Base64 from: {image_path}")
    return encoded_string

