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
    #Make WindRose
    ax = WindroseAxes.from_ax()
    ax.set_title("Wind Rose for coordinates "+str(latitude)+" , "+str(longitude)+ ' at elevation '+str(elevation) + 'm')
    ax.bar(df.wdir, df.wspd, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    
def windRose(latitude, longitude, start, end):
    # Define location
    location = Point(latitude, longitude)
    # Grab data for location
    data = Hourly(location, start, end)
    df = data.fetch()
    #Make WindRose
    ax = WindroseAxes.from_ax()
    ax.set_title("Wind Rose for coordinates "+str(latitude)+" , "+str(longitude))
    ax.bar(df.wdir, df.wspd, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()