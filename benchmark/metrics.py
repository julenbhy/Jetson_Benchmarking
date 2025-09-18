import statistics

def aggregate_results(runs):
    """Convert list of runs (dicts) into mean and stdev per metric."""
    metrics = {}
    if not runs:
        return metrics

    keys = runs[0].keys()
    for key in keys:
        values = [run[key] for run in runs if key in run]
        if values:
            metrics[key] = {
                "mean": round(statistics.mean(values), 4),
                "stdev": round(statistics.stdev(values), 4) if len(values) > 1 else 0.0
            }
    return metrics

def print_summary(model_name, aggregated):
    print(f"\n=== Summary for {model_name} ===")
    for key, stats in aggregated.items():
        if "Temp" not in key:
            print(f"{key}: mean={stats['mean']}, stdev={stats['stdev']}")
    print("=" * 60)
