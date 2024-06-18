import os
import matplotlib.pyplot as plt
from flask import url_for
import logging
# function to generate the graph when the user clicks on the order numberes button
def generate_plot(app_root_path, numbers):
    graph_dir = os.path.join(app_root_path, 'static', 'assets', 'graph')
    if not os.path.exists(graph_dir):
        logging.debug(f"Creating directory: {graph_dir}")
        os.makedirs(graph_dir)

    plt.figure()

    plt.plot(numbers, marker='o', linestyle='-', color='b')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Ordered Numbers')
    
    for i, num in enumerate(numbers):
        plt.text(i, num, str(num), ha='center', va='bottom')

    plot_path = os.path.join(graph_dir, 'plot.png')
    logging.debug(f"Saving plot to: {plot_path}")
    plt.savefig(plot_path)
    plt.close()
    
    if not os.path.exists(plot_path):
        logging.error(f"Failed to save plot to: {plot_path}")
    else:
        logging.debug(f"Plot successfully saved to: {plot_path}")
    
    return url_for('static', filename='assets/graph/plot.png')