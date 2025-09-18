import csv
import os

def save_results_to_csv(all_results, save_dir):
    """
    Save aggregated benchmark results to one CSV file per model.
    Each CSV contains all metrics (mean & stdev) for that model.
    """
    os.makedirs(save_dir, exist_ok=True)

    for model_name, metrics in all_results.items():
        csv_path = os.path.join(save_dir, f"{model_name.replace('/', '_')}.csv")
        # Column headers: metric_mean, metric_stdev for each metric
        headers = []
        row = []
        for metric_name, stat_dict in metrics.items():
            headers.append(f"{metric_name}_mean")
            headers.append(f"{metric_name}_stdev")
            row.append(stat_dict["mean"])
            row.append(stat_dict["stdev"])

        with open(csv_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(row)

        print(f"Saved CSV: {csv_path}")


def save_raw_results_to_csv(raw_results, save_dir):
    """
    Save raw benchmark results to one CSV file per model.
    raw_results: dict[model_name] -> list[dict] (cada dict es una repetición)
    """
    os.makedirs(save_dir, exist_ok=True)

    for model_name, runs in raw_results.items():
        if not runs:
            continue
        csv_path = os.path.join(save_dir, f"{model_name.replace('/', '_')}.csv")
        # Headers = keys del primer run
        headers = list(runs[0].keys())

        with open(csv_path, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for run in runs:
                writer.writerow(run)

        print(f"Saved raw CSV: {csv_path}")
