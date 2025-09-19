# src/config.py
import os
import torch

# Models to test
MODEL_NAMES = ["70m", "160m", "410m", "1b", "1.4b"] # "70m", "160m", "410m", "1b", "1.4b", "2.8b", "6.9b", "12b"
MODELS = [f"EleutherAI/pythia-{label}-deduped" for label in MODEL_NAMES]

# Metrics to plot
PLOT_METRICS = ["RAM", "GPU", "execution_time_sec"]

PROMPT = "Artificial intelligence is useful because"

# General settings
NUM_NEW_TOKENS = 50
N_REPEATS = 10

# Precision to test
DTYPE = torch.bfloat16  # torch.float32
DTYPE_NAME = "bfloat16" # Also change for result directory

# Directory for saving plots
BASE_DIR = os.path.dirname(__file__)
RESULTS_DIR = os.path.join(BASE_DIR, "results", DTYPE_NAME)
PLOTS_DIR = os.path.join(RESULTS_DIR, "plots")
CSV_DIR = os.path.join(RESULTS_DIR, "csv")


# Disable parallelism warning from HuggingFace tokenizers
os.environ["TOKENIZERS_PARALLELISM"] = "false"

