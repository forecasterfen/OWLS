#For this program to work, start and end variables use datetime function, example is datetime(yyyy,m,d) if month and/or day has double digits
#then you will add the second digit, otherwise, just add only one digit. The start and end defines how farback you want to grab the data and
#how far foward you want your data from

%matplotlib inline
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from meteostat import Point, Hourly
from windrose import WindroseAxes
from datetime import datetime

def windRoseElevation(latitude, longitude, elevation, start, end):
    # Define location
    location = Point(latitude, longitude, elevation)
    # Grab data for location
    data = Hourly(location, start, end)
    df = data.fetch()
    normalized_df=(df-df.mean())/df.std()
    #Make WindRose
    ax = WindroseAxes.from_ax()
    ax.set_title("Wind Rose for coordinates "+str(latitude)+" , "+str(longitude)+ ' at elevation '+str(elevation) + 'm'+ ' from '+str(start)+' to '+str(end))
    ax.bar(df.wdir, normalized_df.wspd, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    
def windRose(latitude, longitude, start, end):
    # Define location
    location = Point(latitude, longitude)
    # Grab data for location
    data = Hourly(location, start, end)
    df = data.fetch()
    normalized_df=(df-df.mean())/df.std()
    #Make WindRose
    ax = WindroseAxes.from_ax()
    ax.set_title("Wind Rose for coordinates "+str(latitude)+" , "+str(longitude)+ ' from '+str(start)+' to '+str(end))
    ax.bar(df.wdir, normalized_df.wspd, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
