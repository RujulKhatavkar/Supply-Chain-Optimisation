import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def custom_plot(data, cols, agg_col, chart_type='bar', agg_type='sum'):
    # Validate the inputs
    if chart_type not in ['bar', 'pie']:
        raise ValueError("chart_type must be either 'bar' or 'pie'")
    if agg_type not in ['sum', 'average', 'count']:
        raise ValueError("agg_type must be either 'sum', 'average', or 'count'")
    if len(cols) < 1:
        raise ValueError("cols must contain at least one grouping column")

    # Prepare the data
    group_cols = cols
    if agg_type == 'sum':
        agg_data = data.groupby(group_cols[0])[agg_col].sum().reset_index()

    elif agg_type == 'average':
        agg_data = data.groupby(group_cols[0])[agg_col].mean().reset_index()
  
    elif agg_type == 'count':
        agg_data = data.groupby(group_cols[0]).size().reset_index(name='count')
        agg_col = 'count'
    display(agg_data)

    # Plot the chart
    if chart_type == 'bar':
     
        # Single Bar Chart
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(agg_data[group_cols[0]], agg_data[agg_col], label=f'{agg_col} ({agg_type})')
        # Add data labels on the bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, height, round(height, 2), ha='center', va='bottom')

        ax.set_xlabel(group_cols[0])
        ax.set_ylabel(f'{agg_type.capitalize()} of {agg_col}')
        ax.set_title(f'{agg_type.capitalize()} of {agg_col} by {group_cols[0]}')
        ax.legend()
        plt.show()
       
    elif chart_type == 'pie':
        plt.figure(figsize=(8, 8))
        plt.pie(agg_data[agg_col], labels=agg_data[group_cols[0]], autopct='%1.1f%%', startangle=140)
        plt.title(f'{agg_type.capitalize()} of {agg_col} by {group_cols[0]}')
        plt.show()






def custom_subplot(ax, data, cols, agg_col, chart_type='bar', agg_type='sum'):
# Validate the inputs
    if chart_type not in ['bar', 'pie']:
        raise ValueError("chart_type must be either 'bar' or 'pie'")
    if agg_type not in ['sum', 'average', 'count']:
        raise ValueError("agg_type must be either 'sum', 'average', or 'count'")
    if len(cols) < 1:
        raise ValueError("cols must contain at least one grouping column")

    # Prepare the data
    group_cols = cols
    if agg_type == 'sum':
        agg_data = data.groupby(group_cols)[agg_col].sum().reset_index()
    elif agg_type == 'average':
        agg_data = data.groupby(group_cols)[agg_col].mean().reset_index()
    elif agg_type == 'count':
        agg_data = data.groupby(group_cols).size().reset_index(name='count')
        agg_col = 'count'

    # Plot the chart on the given subplot axis
    if chart_type == 'bar':
        if len(cols) == 1:
            # Single Bar Chart
            bars = ax.bar(agg_data[group_cols[0]], agg_data[agg_col], label=f'{agg_col} ({agg_type})')
            # Add data labels on the bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2.0, height, round(height, 2), ha='center', va='bottom')

            ax.set_xlabel(group_cols[0])
            ax.set_ylabel(f'{agg_type.capitalize()} of {agg_col}')
            ax.set_title(f'{agg_type.capitalize()} of {agg_col} by {group_cols[0]}')
            ax.legend()
        elif len(cols) == 2:
            # Double Bar Chart
            group_col1, group_col2 = group_cols
            agg_data = data.groupby([group_col1, group_col2])[agg_col].sum().unstack(fill_value=0).reset_index()
            bar_width = 0.35
            index = np.arange(len(agg_data))

            bars1 = ax.bar(index - bar_width / 2, agg_data[agg_data.columns[1]], bar_width, label=f'{agg_data.columns[1]}')
            bars2 = ax.bar(index + bar_width / 2, agg_data[agg_data.columns[2]], bar_width, label=f'{agg_data.columns[2]}')

            # Add data labels on the bars
            for bar in bars1:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2.0, height, round(height, 2), ha='center', va='bottom')
            for bar in bars2:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2.0, height, round(height, 2), ha='center', va='bottom')

            ax.set_xlabel(group_col1)
            ax.set_ylabel(f'{agg_type.capitalize()} of {agg_col}')
            ax.set_title(f'{agg_type.capitalize()} of {agg_col} by {group_col1} and {group_col2}')
            ax.set_xticks(index)
            ax.set_xticklabels(agg_data[group_col1])
            ax.legend()
    elif chart_type == 'pie':
        ax.pie(agg_data[agg_col], labels=agg_data[group_cols[0]], autopct='%1.1f%%', startangle=140)
        ax.set_title(f'{agg_type.capitalize()} of {agg_col} by {group_cols[0]}')