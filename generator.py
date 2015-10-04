
from __future__ import division
from math import radians

import numpy as np

# average earth radius
R_earth = 6367444.7

class Sensor:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat
        self.event = False
        self.theta = 0.
        self.P = 0

class Event:
    def __init__(self, lon, lat, P):
        self.lon = lon
        self.lat = lat
        self.P = P

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    return c * R_earth

def generate_event(bbox):

    # random location
    h = bbox[1,0] - bbox[0,0]
    w = bbox[1,1] - bbox[0,1]
    p_unit = np.random.uniform(size=(2,))
    lon = bbox[0,0]+w*p_unit[0]
    lat = bbox[0,1]+h*p_unit[1]

    # random magnitude in dB
    P = 120+np.random.uniform()*80

    return Event(lon, lat, P)

def measure(event, sensors):

    for s in sensors:

        d = haversine(s.lon, s.lat, event.lon, event.lat)
        s.theta = np.arctan2(event.lat - s.lat, event.lon - s.lon)
        s.P = event.P - 20*np.log10(d)
        s.event = True

