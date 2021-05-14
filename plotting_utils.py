import numpy as np
import matplotlib.pyplot as plt

def norm(s, norm_type):
    '''Normalise a 1D array.
    
    Args:
        s: (np.ndarray) a given 1D ndarray.
        norm_type: (str) one of 'max' or 'std', used to normalise the ndarray.
        
    Returns:
        (np.ndarray) normalised 1D ndarray.
    '''
    if norm_type == 'max':
        if np.nanmax(s) == 0:
            return s
        else:
            return s / np.nanmax(s)
    if norm_type == 'std':
        if np.std(s) == 0:
            return s
        else:
            return s / np.std(s)
    
    
def _add_heatplot_to_axis(data, well_name, norm_type, ax):
    '''Make a heatplot of a single well.
    The y-axis is reset to be the depth of the well.
    The x-axis is the AMU of the fluid inclusions per record.
    
    To use this interactively in a notebook:
        interact(plotting_utils.make_heatplot,
                data=fixed(my_dataframe),
                well_name=names,
                norm_type=['max', 'std']
                )
    
    Args:
        data: (DataFrame) Fluid inclusion data and such.
        well_name: (str) The well ID to plot.
        norm_type: (str) normalises each column in the array by either
            `std` (standard deviation) or `max` in each column.
        ax: (matplotlib axes) The axes object to plot onto.
            
    Returns:
        None, side effect to display a plot.
    '''
    print(well_name, type(well_name))
    # Get a list of the AMUs available
    amu_list = data.columns[7:-5]
    
    # Get the AMUs for a specific well
    X = data.loc[data['Well ID'] == well_name][amu_list]
    X = np.nan_to_num(X.astype(float).values)
    
    # Normalise each AMU (column)
    X2 = np.apply_along_axis(norm, axis=0, arr=X, norm_type=norm_type)
    
    # Get depths for the plots
    depths = data.loc[data['Well ID'] == well_name]['Depth (ft)']
    extents = (0, 6500, np.nanmax(depths), np.nanmin(depths))
    
    # Change the vmax based on the norm used
    if norm_type == 'std':
        ma = 5
    else:
        ma = 1
    
    # Plotting stuff
    im = ax.imshow(X2, vmax=ma, extent=extents)
    ax.set_title(well_name)
    ax.set_xticks(np.linspace(0, 4500, 5))
    ax.set_xticklabels(np.arange(0, 181, 40))
    #ax.set_ylabel('Depth (ft)')
    ax.set_xlabel('AMU')
    plt.colorbar(im, ax=ax, shrink=0.5, orientation='horizontal')
    return ax


def make_heatplot(data, well_names, norm_type):
    '''Make a heatplot of a group of wells.
    The y-axis is reset to be the depth of the well.
    The x-axis is the AMU of the fluid inclusions per record.
    
    Args:
        data: (DataFrame) Fluid inclusion data and such.
        well_names: (list of str) The well IDs to plot. The list may have
            only one element.
        norm_type: (str) normalises each column in the array by either
            `std` (standard deviation) or `max` in each column.
            
    Returns:
        fig,
        axs,
    '''
    if isinstance(well_names, str):
        fig, axs = plt.subplots(figsize=(15,8), sharey=True)
    else:
        fig, axs = plt.subplots(ncols=len(well_names), figsize=(15,8), sharey=True)
    
    if isinstance(well_names, str):
        print('Found a string, so plotting a single heatplot')
        _add_heatplot_to_axis(data, well_names, norm_type, axs)
        return None
    
    print('Found a list, so plotting multiple heatplots')
    for ax, well_name in zip(axs, well_names):
        _add_heatplot_to_axis(data, well_name, norm_type, ax)
        
    return fig, axs

