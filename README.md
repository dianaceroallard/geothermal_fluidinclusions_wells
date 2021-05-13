# geothermal_fluidinclusions_wells
analysis of continuous fluid inclusion - gas analysis data from geothermal wells

## COSO Fluid Inclusion Gas Analysis

Source files are located at [gdr.openei.org](https://gdr.openei.org/submissions/191)

### Hosted data
There are two files worht looking at in the `data` folder:
 - `raw_collated.csv` is a combined csv of all the samples downloaded from the above link. This is useful if you want to do anything with all of the sampled fluid inclusions.
 - `located_wells.csv` has the latitude and longitude of a portion of the wells associated. This will be of use if you want to do any analysis involving geospatial distributions and such. It covers has 6896 of the 9712 rows present in `raw_collated`.
 