# geothermal_fluidinclusions_wells
analysis of continuous fluid inclusion - gas analysis data from geothermal wells

## COSO Fluid Inclusion Gas Analysis

Source files are located at [gdr.openei.org](https://gdr.openei.org/submissions/191)

### Hosted data
There are two files worht looking at in the `data` folder:
 - `raw_collated.csv` is a combined csv of all the samples downloaded from the above link. This is useful if you want to do anything with all of the sampled fluid inclusions.
 - `located_wells.csv` has the latitude and longitude of a portion of the wells associated. This will be of use if you want to do any analysis involving geospatial distributions and such. It covers has 6896 of the 9712 rows present in `raw_collated`.
 

#### Reference: Fluid Stratigraphy and Permeable Zones of the Coso Geothermal Reservoir. Dilley, L. M., Norman, D.I., Moore, J., and McCulloch, J. Geothermal Resource Council Transactions, Vol. 30. 2006

#### Fluid inclusions gaseous species in drill cuttings by mass spectrometry analyses
N2 = AMU28
Ar = AMU40
CO2 = AMU44
CH4 = AMU16 
propane = AMU43
propene = AMU39

##### Reservoir fluids
N2/Ar (mass 28/mass 40) > 200
CO2/CH4 (mass 44/mass 16) > 4, 
R1 = (N2/Ar (mass 28/mass 40)+ CO2/CH4)/(propane/propene (mass 43/mass 39))
R2 = (N2/Ar (mass 28/mass 40)+ CO2/N2 (mass 44/mass 28))

##### Shallow Meteoric Fluids
N2/Ar < 200, CO2/CH4 < 4,  propane/propene >1, 1/R1 > 0.5

##### Permeable zones
Relative change in the CO2/N2
