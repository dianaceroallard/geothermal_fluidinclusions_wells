# geothermal_fluidinclusions_wells
analysis of continuous fluid inclusion - gas analysis data from geothermal wells

## COSO Fluid Inclusion Gas Analysis

Source files are located at [gdr.openei.org](https://gdr.openei.org/submissions/191)

### Hosted data
These are files worth looking at in the `data` folder:
 - `raw_collated.csv` is a combined csv of all the samples downloaded from the above link. This is useful if you want to do anything with all of the sampled fluid inclusions, as from source.
 - `cleaned_types.csv` is a cleaned version of `raw_collated.csv`. This corrects some missing and incorrect data.
 - `located_wells.csv` has the latitude and longitude of a portion of the wells associated. This will be of use if you want to do any analysis involving geospatial distributions and such. It covers has 6896 of the 9712 rows present in `raw_collated`, and uses that as a base.
 - `fi_wells.gpkg` is a geopackage version of `located_wells.csv` rebuilt using `cleaned_types.csv`. This should be droppable into whichever GIS software you favour. It is also possible to build a shapefile version, but it will truncate the column headers.
 - `well_locations.gpkg` is a geopackage of the wells present in the Coso field. There are more of these than `fi_wells.gpkg`, but many of these do not have fluid inclusion data associated with them.
 

#### Reference: Fluid Stratigraphy and Permeable Zones of the Coso Geothermal Reservoir. Dilley, L. M., Norman, D.I., Moore, J., and McCulloch, J. Geothermal Resource Council Transactions, Vol. 30. 2006

#### Fluid inclusions gaseous species in drill cuttings by mass spectrometry analyses
- N2 = AMU28
- Ar = AMU40
- CO2 = AMU44
- CH4 = AMU16 
- propane = AMU43
- propene = AMU39

##### Reservoir fluids
- N2/Ar (mass 28/mass 40) > 200
- CO2/CH4 (mass 44/mass 16) > 4, 
- R1 = (N2/Ar (mass 28/mass 40)+ CO2/CH4)/(propane/propene (mass 43/mass 39))
- R2 = (N2/Ar (mass 28/mass 40)+ CO2/N2 (mass 44/mass 28))

##### Shallow Meteoric Fluids
N2/Ar < 200, CO2/CH4 < 4,  propane/propene >1, 1/R1 > 0.5

##### Permeable zones
Relative change in the CO2/N2
