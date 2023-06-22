import argparse
from pathlib import Path

def commandParser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dataset-path', type=Path, help='Path to the dataset')


    args = parser.parse_args()
    return args