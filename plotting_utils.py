import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

def norm(s, norm_type='std'):
    '''Normalise a 1D array.
    
    Args:
        s: (np.ndarray) a given 1D ndarray.
        norm_type: (str) one of 'none', 'max' or 'std',
            used to normalise the ndarray.
        
    Returns:
        (np.ndarray) normalised 1D ndarray.
    '''
    assert (norm_type in ['max', 'std', 'none', None]), f"Normalisation method not recognised. Please use one of 'max', 'std', 'none'"
    
    if norm_type is None or norm_type.lower() == 'none':
        return s
    if norm_type.lower() == 'max':
        if np.nanmax(s) == 0:
            return s
        else:
            return s / np.nanmax(s)
    if norm_type.lower() == 'std':
        if np.std(s) == 0:
            return s
        else:
            return s / np.std(s)
    
    
def _add_heatplot_to_axis(data, well_name, norm_type, ax, vmax=None):
    '''Make a heatplot of a single well.
    The y-axis is reset to be the depth of the well.
    The x-axis is the AMU of the fluid inclusions per record.
    
    Args:
        data: (DataFrame) Fluid inclusion data and such.
        well_name: (str) The well ID to plot.
        norm_type: (str) normalises each column in the array by either
            `std` (standard deviation) or `max` in each column.
        ax: (matplotlib axes) The axes object to plot onto.
            
    Returns:
        None, side effect to display a plot.
    '''
    # Get a list of the AMUs available
    amu_list = data.columns[7:-5]
    
    # Get the AMUs for a specific well
    X = data.loc[data['Well ID'] == well_name][amu_list]
    X = np.nan_to_num(X.astype(float).values)
    
    # Normalise each AMU (column)
    X2 = np.apply_along_axis(norm, axis=0, arr=X, norm_type=norm_type)
    
    # Get depths for the plots
    depths = data.loc[data['Well ID'] == well_name]['Depth (ft)']
    x_width = 2000
    extents = (0, x_width, np.nanmax(depths), np.nanmin(depths))
    
    # Change the vmax based on the norm used
    if vmax is not None:
        ma = vmax
    elif norm_type == 'std':
        ma = 5
    elif norm_type == 'max':
        ma = 1
    else:
        ma = 25
    
    # Plotting stuff
    im = ax.imshow(X2, vmax=ma, extent=extents)
    ax.set_title(well_name)
    ax.set_xticks(np.linspace(0, x_width, 10))
    ax.set_xticklabels(np.arange(0, 181, 20))
    ax.set_xlabel('AMU')
    plt.colorbar(im, ax=ax, shrink=0.5, orientation='vertical')
    return ax


def make_heatplot(data, well_names, norm_type='std', vmax=None):
    '''Make a heatplot of a group of wells.
    The y-axis is reset to be the depth of the well.
    The x-axis is the AMU of the fluid inclusions per record.
    
    To use this interactively in a notebook:
        interact(plotting_utils.make_heatplot,
                data=fixed(my_dataframe),  # pass the data as-is
                well_name=names,
                norm_type=['max', 'std', 'none'],
                vmax=np.arange(1, 400),
                )
    
    Args:
        data: (DataFrame) Fluid inclusion data and such.
        well_names: (list of str) The well IDs to plot. The list may have
            only one element.
        norm_type: (str) normalises each column in the array by either
            `std` (standard deviation) or `max` in each column.
            
    Returns:
        fig, matplotlibe figure
        axs, matplotlib axes or list of matplotlib axes
    '''
    if isinstance(well_names, str):
        fig, axs = plt.subplots(figsize=(15,8), sharey=True)
    else:
        fig, axs = plt.subplots(ncols=len(well_names), figsize=(15,8), sharey=True)
    
    if isinstance(well_names, str):
        _add_heatplot_to_axis(data, well_names, norm_type, axs, vmax)
        axs.set_ylabel('Depth (ft)')
        return None
    
    for ax, well_name in zip(axs, well_names):
        _add_heatplot_to_axis(data, well_name, norm_type, ax, vmax)
        
    axs[0].set_ylabel('Depth (ft)')
        
    return fig, axs


def plot_map_heatplot(well_name):
    tiles = ctx.providers.Stamen.Terrain
    image = ctx.providers.Esri.WorldImagery
    coords = gpd.read_file('./data/well_locations.gpkg')
    
    fig, ax = plt.subplots(figsize=(10,10))

    coords.plot(ax=ax, color='white', ec='k', markersize=50)
    if coords.loc[coords['WellNumber'] == well_name].empty:
        print(f'Location of {well_name} not available.')
    else:
        coords.loc[coords['WellNumber'] == well_name].plot(ax=ax, color='red', ec='k', markersize=50)

    ctx.add_basemap(ax=ax, source=tiles, crs=4326, attribution='')
    ctx.add_basemap(ax=ax, source=image, crs=4326, alpha=0.6, attribution='')
    ctx.add_attribution(ax=ax, text=f'{tiles.attribution}\n{image.attribution}')

    plt.show()
    return ax
