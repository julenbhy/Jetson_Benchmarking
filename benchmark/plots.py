import os
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("classic")

def plot_metrics(all_results, model_x_axis, metrics_to_plot, save_dir):
    """Generate and save line + bar plots (error bars) with value annotations (slightly shifted)."""
    os.makedirs(save_dir, exist_ok=True)
    x_labels = model_x_axis
    x_pos = np.arange(len(x_labels))

    for metric in metrics_to_plot:
        y_means = []
        y_stdevs = []
        for model_name in all_results.keys():
            if metric in all_results[model_name]:
                y_means.append(all_results[model_name][metric]["mean"])
                y_stdevs.append(all_results[model_name][metric]["stdev"])
            else:
                y_means.append(np.nan)
                y_stdevs.append(np.nan)

        y_means = np.array(y_means, dtype=float)
        y_stdevs = np.array(y_stdevs, dtype=float)

        # ---- Line plot with error bars ----
        plt.figure(figsize=(6, 4))
        plt.errorbar(
            x_pos,
            y_means,
            yerr=y_stdevs,
            fmt='o-',
            ecolor='black',
            elinewidth=1,
            capsize=4,
            markersize=5,
            color='black'
        )
        # Add values
        for x, y in zip(x_pos, y_means):
            if not np.isnan(y):
                plt.text(
                    x + 0.05,
                    y + 0.02 * np.nanmax(y_means),
                    f"{y:.2f}",
                    ha='left',
                    va='bottom',
                    fontsize=8
                )

        plt.xticks(x_pos, x_labels, fontsize=10)
        plt.xlabel("Model (parameters)", fontsize=11)
        plt.ylabel(metric, fontsize=11)
        plt.title(f"{metric} vs Model size", fontsize=12)
        plt.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)
        plt.tight_layout()
        line_path = os.path.join(save_dir, f"{metric}_line.png")
        plt.savefig(line_path, dpi=300)
        plt.close()
        print(f"Saved line plot: {line_path}")

        # ---- Bar plot with error bars ----
        plt.figure(figsize=(6, 4))
        bar_color = 'grey'
        bars = plt.bar(
            x_pos,
            y_means,
            yerr=y_stdevs,
            capsize=4,
            color=bar_color,
            edgecolor='black',
            linewidth=0.8
        )
        # Add values
        for bar, y in zip(bars, y_means):
            if not np.isnan(y):
                plt.text(
                    bar.get_x() + bar.get_width() / 2 + 0.05,
                    bar.get_height() + 0.02 * np.nanmax(y_means),
                    f"{y:.2f}",
                    ha='left',
                    va='bottom',
                    fontsize=8
                )

        plt.xticks(x_pos, x_labels, fontsize=10)
        plt.xlabel("Model (parameters)", fontsize=11)
        plt.ylabel(metric, fontsize=11)
        plt.title(f"{metric} vs Model size", fontsize=12)
        plt.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.7)
        plt.tight_layout()
        bar_path = os.path.join(save_dir, f"{metric}_bar.png")
        plt.savefig(bar_path, dpi=300)
        plt.close()
        print(f"Saved bar plot: {bar_path}")
