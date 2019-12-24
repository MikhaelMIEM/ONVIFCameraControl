# ONVIFCameraControl
Python module for some basic Onvif camera control actions. List of available functions watch in [code](https://github.com/MikhaelMIEM/ONVIFCameraControl/blob/master/ONVIFCameraControl/ONVIFCameraControl.py)
# Installation
```sh
$ python3.7 -m pip install ONVIFCameraControl
```
# Usage
```sh
from ONVIFCameraControl import ONVIFCameraControl
from time import sleep

cam = ONVIFCameraControl(("172.18.200.53", 80), "admin", "password")

ptz_velocity_vector = (1, 1, 1)
cam.move_continuous(ptz_velocity_vector)  
sleep(1)  
cam.stop()
```