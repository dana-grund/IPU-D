# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:18:55 2019

@author: Joerg

Updated by Dana Grund on 2023-03-08
"""

from pandas import read_csv
from tephigram_python import Tephigram
import click

def get_met_data(filename):
    
    dat = read_csv(filename,header=14) #21)

    # clean data, remove entries containing no value, respectively only 99999
    # and use only data, when the sonde was rising ascent rate > 1.5 m/s
    dat = dat[(dat[' iMet air temperature (corrected) [deg C]']<30) & \
            (dat[' iMet humidity [RH %]']<1000) & \
            (dat[' iMet frostpoint [deg C]']<1000) & \
            (dat[' iMet pressure [mb]']<1000) & \
            (dat[' GPS ascent rate [m/s]']!=99999) & \
            (dat[' iMet ascent rate [m/s]']<1000) & \
            (dat[' GPS ascent rate [m/s]']>0)]

    p = dat[' iMet pressure [mb]']
    #T = dat[' iMet internal temperature [deg C]']
    T = dat[' iMet air temperature (corrected) [deg C]']
    T_dp = dat[' iMet frostpoint [deg C]']
    RH = dat[' iMet humidity [RH %]']/100.
    z = dat[' GPS altitude [km]']

    return p,T,T_dp,RH,z 

@click.command()
@click.option("-f", '--filename', default="2022-data-group1/zh-999_20220504.csv", help=".csv file to plot")
def plot_tephigram(filename):
    print('plotting ',filename)
    p,T,T_dp,RH,z = get_met_data(filename)
    
    tephigram = Tephigram()
    
    tephigram.plot_sounding(P=p, T=T, T_dp=T_dp)
    tephigram.plot_legend()
    tephigram.savefig(filename.rstrip('.csv')+'_tephigram.png')    
    
if __name__ == "__main__":
    
    plot_tephigram()
