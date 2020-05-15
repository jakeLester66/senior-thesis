## misc.py
import pandas as pd

def combinations(list1, list2):
    index = []
    for g in list1:
        for d in list2:
            index.append((g, d))

    return index

def replace_nan_none(df):
    df = df.replace({pd.np.nan: None})
    return df

import matplotlib.pyplot as plt
import six
import numpy as np

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, cell_width_custom=None, **kwargs):
    ## taken from https://stackoverflow.com/questions/26678467/export-a-pandas-dataframe-as-a-table-image

    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    cellDict = mpl_table.get_celld()
    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
        if cell_width_custom:
            cell.set_width(cell_width_custom[k[1]])
    #https://stackoverflow.com/questions/12490596/matplotlib-table-individual-column-width
    #cellDict = mpl_table.get_celld()
    #for k, cell in
    #cellDict[(0, 0)].set_width(0.1)
    #if cell_width_custom:
    #        cell.set_width(cell_width_custom[k])
    return fig, ax

