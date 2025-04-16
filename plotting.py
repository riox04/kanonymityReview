#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
This script creates tables and charts from K-anonymity experimental results
with dynamic inputs for different types of analyses.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visualize_anonymity(graph_name, x_axis_label, x_axis_values, ncp_values, runtime_values):
    """
    Create a table and chart from K-anonymity results with dynamic inputs.
    
    Parameters:
    -----------
    graph_name : str
        Name of the graph and table (used for file naming and title)
    x_axis_label : str
        Label for the X axis (e.g., "K Values", "Dataset Size", "Number of QIs")
    x_axis_values : list
        List of values for the X axis
    ncp_values : list
        List of NCP values
    runtime_values : list
        List of running times
    """
    # Create a DataFrame for the table
    column_name = x_axis_label.lower().replace(" ", "_")
    data = {
        column_name: x_axis_values,
        'ncp': ncp_values,
        'running_times': runtime_values
    }
    df = pd.DataFrame(data)
    
    # Display the table
    print("\nTable of " + graph_name + ":")
    print(df)
    
    # Create filenames based on graph name (sanitized for file system)
    base_filename = graph_name.lower().replace(" ", "_").replace(":", "").replace("/", "_")
    table_filename = base_filename + "_table.csv"
    chart_filename = base_filename + "_chart.png"
    
    # Save the table to CSV
    df.to_csv(table_filename, index=False)
    print("\nTable saved to: " + table_filename)
    
    # Create the chart with two y-axes
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Primary y-axis for NCP
    ax1.set_xlabel(x_axis_label)
    ax1.set_ylabel('NCP', color='blue')
    ax1.plot(x_axis_values, ncp_values, 'bo-', label='NCP')
    ax1.tick_params(axis='y', labelcolor='blue')
    
    # Secondary y-axis for running time
    ax2 = ax1.twinx()
    ax2.set_ylabel('Running Time (s)', color='red')
    ax2.plot(x_axis_values, runtime_values, 'rs-', label='Running Time')
    ax2.tick_params(axis='y', labelcolor='red')
    
    # Title and grid
    plt.title(graph_name + ': NCP and Running Time vs ' + x_axis_label)
    ax1.grid(True, alpha=0.3)
    
    # Legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')
    
    # Adjust layout to prevent clipping
    plt.tight_layout()
    
    # Save and show the chart
    plt.savefig(chart_filename)
    print("Chart saved to: " + chart_filename)
    plt.show()

def get_input_list(prompt):
    """
    Helper function to get a list of values from user input.
    
    Parameters:
    -----------
    prompt : str
        Message to display when asking for input
    
    Returns:
    --------
    list
        List of values (converted to appropriate type)
    """
    try:
        input_str = raw_input(prompt)
        # Handle different input formats
        input_str = input_str.replace("[", "").replace("]", "")
        values = [x.strip() for x in input_str.split(",")]
        
        # Try to convert to numeric if possible
        try:
            return [float(x) for x in values]
        except ValueError:
            print("Warning: Some values could not be converted to numbers.")
            return values  # Return as strings if not all numeric
    except Exception as e:
        print("Error reading input: " + str(e))
        return []



if __name__ == "__main__":
    print("\nK-Anonymity Visualization Tool")
    print("==============================")

    #examples if needed
    # if "-e" in [arg.lower() for arg in [a for a in np.array(raw_input("Show examples? (y/n): ").lower())]]:
    #     print_examples()
    
    # Get inputs from user
    graph_name = raw_input("Enter graph/table name (e.g. 'K-Anonymity for Adult Dataset'): ")
    x_axis_label = raw_input("Enter X-axis label (e.g. 'K Values', 'Dataset Size', 'Number of QIs'): ")
    
    # Get array inputs
    x_axis_values = get_input_list("Enter X-axis values (comma-separated): ")
    ncp_values = get_input_list("Enter NCP values (comma-separated): ")
    runtime_values = get_input_list("Enter Running Time values (comma-separated): ")
    
    # Check if all arrays have the same length
    if len(x_axis_values) == 0 or len(ncp_values) == 0 or len(runtime_values) == 0:
        print("Error: One or more input arrays are empty.")
    elif not (len(x_axis_values) == len(ncp_values) == len(runtime_values)):
        print("Error: All input arrays must have the same length.")
        print("X-axis values: {0}, NCP values: {1}, Running Time values: {2}".format(
            len(x_axis_values), len(ncp_values), len(runtime_values)))
    else:
        visualize_anonymity(graph_name, x_axis_label, x_axis_values, ncp_values, runtime_values)
