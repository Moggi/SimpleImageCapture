# SimpleImageCapture
```
 ____  _                 _      ___                             ____            _                  
/ ___|(_)_ __ ___  _ __ | | ___|_ _|_ __ ___   __ _  __ _  ___ / ___|__ _ _ __ | |_ _   _ _ __ ___
\___ \| | '_ ` _ \| '_ \| |/ _ \| || '_ ` _ \ / _` |/ _` |/ _ \ |   / _` | '_ \| __| | | | '__/ _ \
 ___) | | | | | | | |_) | |  __/| || | | | | | (_| | (_| |  __/ |__| (_| | |_) | |_| |_| | | |  __/
|____/|_|_| |_| |_| .__/|_|\___|___|_| |_| |_|\__,_|\__, |\___|\____\__,_| .__/ \__|\__,_|_|  \___|
                  |_|                               |___/                |_|                       

A simple Python app to capture your photos
 ```

## Requirements
- Python 2.7
- OpenCV
- PyQT

## Code example

See [main.py](../master/main.py)


## ROADMAP
- Update the WindowWidget class structure
- In WindowWidget:
 - Remove the CameraWidget from it
 - Reorganize the widgets positions (layout)
 - Make window 'resizable' to a predefined resolution (include fullscreen)
- Create a Save Photo button

#### Future
- Update from cv module to cv2 (requires NumPy)
- Maybe use Pillow
- Maybe use gPhoto2

#### Other App
- Create a real time Effects module
- Maybe Face Detection
