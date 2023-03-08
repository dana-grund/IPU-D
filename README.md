# IPU-D
ETH course "Integriertes Praktikum Umweltbeobachtungen - D: Mikronetz"

### Installation
Create a conda python environment with the packages needed for the tephigram code:
```
conda env create -f  requirements.yml
```
It uses python 3.8, as the code did not work with the most current python (3.10). However, this might need to be adapted once python moved to ever newer versions.

To activate the environment, run
```
conda activate IPU-D

```
If you want to add a package to the environment, add it to `requirements.yml` and run
```
conda env update -f requirements.yml --prune
```

### Use of plot_tephigram
- adapt number of header lines in the code if needed
Run example plot with the data given in the repository (group 1 from 2022):
```
python plot_tephigram.py
```

Run with own data: create a new data folder containing the .csv file, `folder/file.vsc` and run
```
python plot_tephigram.py -f folder/file.csv
```
