from pathlib import Path
import os


def save_to(directory):
    workspace = Path(os.getcwd())
    save_to = Path(workspace, directory)
    return save_to
