# Radiosounding of CircBrazil campaign
[![Data](https://img.shields.io/badge/Data-10.5281%2Fzenodo.7051674-green)](https://doi.org/110.5281/zenodo.7051674)

This repository contains references to the campaigns radiosoundings its post-processing steps.

## Dataset
The [dataset](https://doi.org/110.5281/zenodo.7051674) contains three processing levels:

|Processing level | Description | Usage examples |
| --- | --- | --- |
| 0 | mwx sounding files as delivered by Vaisalas sounding software | Checking specific setup of sounding station, Archival of data |
| 1 | Level 0 data converted to netCDF4 | Analysis of single soundings for the most accurate measurements possible |
| 2 | Level 1 data interpolated to a vertical grid | Analysis of entire campaign or comparison with other observations or simulations |

## Reprocessing
By running `reproduce.sh` the level 1 and level 2 data can be reproduced. Output units, variable names, and global attributes
can be setup with the yaml files in the `config` folder.

To release a new version of the dataset, please make sure to adjust the DOI in `config/level1.yaml` and `config/level2.yaml`.
DOI can be reserved before publishing at most DOI providers, e.g. at [zenodo.org](https://help.zenodo.org/) by creating a new record/version.
