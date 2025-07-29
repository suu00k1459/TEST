import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

DATA_DIR = os.path.join(project_root, r"raw_data\01_rawdata")
RESULTS_DIR = os.path.join(project_root, "output")
IMAGE_DIR = os.path.join(RESULTS_DIR, "output\images")
