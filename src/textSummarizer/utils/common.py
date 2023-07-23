import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (str): Path like input.
        
    Raises:
        BoxValueError: If the yaml file is not valid.
        e: If the yaml file is not found.
        e: If there is any other error.
    
    Returns:
        ConfigBox: A ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read yaml file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading yaml file: {e}")
        raise e
    except FileNotFoundError as e:
        logger.error(f"Error reading yaml file: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they don't exist.
    Args:
        path_to_directories (list): List of paths to directories.
        ignore_errors (bool, optional): If True, ignores errors. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory: {path}")



@ensure_annotations
def get_size(path:Path) -> str:
    """Gets the size of a file or directory.
    
    Args:
        path (Path): Path to the file or directory.
    
    Returns:
        str: Size of the file or directory.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"