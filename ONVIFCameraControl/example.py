from time import sleep
from ONVIFCameraControl import ONVIFCameraControl, ONVIFCameraControlError

if __name__ == '__main__':
    try:
        cam = ONVIFCameraControl(("172.18.200.53", 80), "admin", "Supervisor")
    except ONVIFCameraControlError as e:
        print(e)
        exit()

    try:
        cam.move_continuous((1, 1, 1))
        sleep(1)
        cam.stop()
    except ONVIFCameraControlError as e:
        print(e)