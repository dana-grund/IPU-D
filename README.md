# IPU-D
ETH course "Integriertes Praktikum Umweltbeobachtungen - D: Mikronetz"

### Installation
Create a conda python environment with the packages needed for the tephigram code:
```
conda env create -f  requirements.yml
```
It uses python 3.8, as the code did not work with the most current python (3.10). However, this might need to be adapted once python moved to ever newer versions.

### Use of plot_tephigram
- change file location
- adapt number of header lines if needed
```
python plot_tephigram.py
```