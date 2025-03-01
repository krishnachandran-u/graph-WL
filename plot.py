import matplotlib.pyplot as plt
import numpy as np
import json

def plot_bar_graph(data: dict, title: str, xlabel: str, ylabel: str, main_title: str):
    plt.rcParams['font.family'] = 'Courier Prime' 

    groups = list(data.keys())
    metrics = ['true positive', 'true negative', 'false positive', 'false negative']
    
    bar_width = 0.2
    index = np.arange(len(groups))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    fig.suptitle(main_title, fontsize=16, fontweight='bold', y=0.98)
    
    for i, metric in enumerate(metrics):
        values = []
        for group in groups:
            group_sum = sum(data[group].values())
            values.append(data[group].get(metric, 0) / group_sum if group_sum > 0 else 0)
        
        ax1.bar(index + i * bar_width, values, bar_width, label=metric)
    
    ax1.set_title(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_xticks(index + 1.5 * bar_width)
    ax1.set_xticklabels(groups)
    ax1.legend(title="Metrics")
    
    true_values = []
    false_values = []
    
    for group in groups:
        group_sum = sum(data[group].values())
        if group_sum > 0:
            true_values.append((data[group]["true positive"] + data[group]["true negative"]) / group_sum)
            false_values.append((data[group]["false positive"] + data[group]["false negative"]) / group_sum)
        else:
            true_values.append(0)
            false_values.append(0)
    
    ax2.bar(index - bar_width / 2, true_values, bar_width, label="True", color="green")
    ax2.bar(index + bar_width / 2, false_values, bar_width, label="False", color="red")
    
    ax2.set_title("True vs False")
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel("Proportions")
    ax2.set_xticks(index)
    ax2.set_xticklabels(groups)
    ax2.legend(title="True vs False")
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])  
    plt.savefig("./img/wl1xnetworkx.png")

data = json.loads(open("./result/wl1xnetworkx.json").read())

plot_bar_graph(data, title="Model Performance", xlabel="Groups", ylabel="Proportions", main_title="Performance of WL1")