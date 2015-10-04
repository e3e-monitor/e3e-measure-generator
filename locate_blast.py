
from __future__ import division
import numpy as np
from generator import Sensor, Event, haversine

def locate_event(sensors):

    normals = np.array([[-np.sin(s.theta), np.cos(s.theta)] for s in sensors])

    A = normals
    b = np.array([np.inner(n, [s.lon, s.lat]) for s,n in zip(sensors, normals)])

    ev_loc = np.linalg.lstsq(A, b)[0]

    d = np.array([haversine(ev_loc[0], ev_loc[1], s.lon, s.lat) for s in sensors])
    P = np.array([s.P for s in sensors])

    ev_P = np.mean(P + 20*np.log10(d))

    return Event(ev_loc[0], ev_loc[1], ev_P)
