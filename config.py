# src/config.py
import os

# Models

MODELS = [  "EleutherAI/pythia-70m-deduped",
	    "EleutherAI/pythia-160m-deduped",
            "EleutherAI/pythia-410m-deduped",
            "EleutherAI/pythia-1b-deduped",
            #"EleutherAI/pythia-1.4b-deduped",
            #"EleutherAI/pythia-1b-deduped",
            #"EleutherAI/pythia-2.8b-deduped",
            #"EleutherAI/pythia-6.9b-deduped",
            #"EleutherAI/pythia-12b-deduped",
         ]

PROMPT = "Artificial intelligence is useful because"

# General settings
NUM_NEW_TOKENS = 50
N_REPEATS = 5

# X-axis labels (must match order in models.txt)
MODEL_X_AXIS = ["70m", "160m", "410m", "1b"]

# Metrics to plot
PLOT_METRICS = ["RAM", "GPU", "execution_time_sec"]

# Directory for saving plots
PLOTS_DIR = os.path.join(os.path.dirname(__file__), "plots")
CSV_DIR = os.path.join(os.path.dirname(__file__), "csv")

# Disable parallelism warning from HuggingFace tokenizers
os.environ["TOKENIZERS_PARALLELISM"] = "false"
