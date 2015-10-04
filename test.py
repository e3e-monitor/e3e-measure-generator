
import numpy as np
import matplotlib.pyplot as plt

from generator import *
from locate_blast import *

# geneva bounding box
bbox = np.array([[46.139402, 6.018432], 
                 [ 46.282900, 6.308197]])

sensors = []
for lon in bbox[:,0]:
    for lat in bbox[:,1]:
        sensors.append(Sensor(lon,lat))

# generate random event
ev = generate_event(bbox)
measure(ev, sensors)

ev_loc = locate_event(sensors)

# plot locations
plt.figure()
x = [s.lon for s in sensors]
y = [s.lat for s in sensors]
plt.plot(x, y, 'x')
plt.plot(ev_loc.lon, ev_loc.lat, 'o')
plt.plot(ev.lon, ev.lat, '*')
plt.legend(('sensors', 'localized','True'))
plt.show()
