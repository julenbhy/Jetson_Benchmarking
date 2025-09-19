from config import MODELS, PROMPT, N_REPEATS, MODEL_NAMES, PLOT_METRICS, PLOTS_DIR, CSV_DIR
from benchmark import run_inference, monitor_resources, aggregate_results, print_summary, plot_metrics, save_raw_results_to_csv


def load_models_from_file(file_path: str):
    with open(file_path, "r") as f:
        models = [line.strip() for line in f if line.strip()]
    return models

def benchmark_model(model_name: str, prompt: str, n_repeats: int = N_REPEATS):
    all_runs = []
    for i in range(n_repeats):
        print(f"\n>>> Running {model_name}, repetition {i+1}/{n_repeats}")
        try:
            _, stats = monitor_resources(run_inference, model_name, prompt)
            all_runs.append(stats)
        except Exception as e:
            print(f"Error in {model_name} run {i+1}: {e}")
    return all_runs

if __name__ == "__main__":

    all_results = {}
    avg_results = {}
    for model_name in MODELS:
        runs = benchmark_model(model_name, PROMPT, N_REPEATS)
        all_results[model_name] = runs

        aggregated = aggregate_results(runs)
        avg_results[model_name] = aggregated
        print_summary(model_name, aggregated)
	
    save_raw_results_to_csv(all_results, CSV_DIR)

    plot_metrics(avg_results, MODEL_NAMES, PLOT_METRICS, PLOTS_DIR)

