#!/usr/bin/env python

import os
import gi
gi.require_version('Gtk', '3.0')
import gtk
import cv2
import sys
import time
from awesomeWindow import *
from gi.repository import Gtk
from gi.repository import GLib

WIDTH = 800
HEIGHT = 640
CAPTURE = True
image = None
quit = False

def onDraw():
    if CAPTURE == True:
        return image
    rval, image = camera.read()
    return image

def onCapture():
    CAPTURE = True

def onCamera():
    CAPTURE = False

def onQuit():
    quit = True


if __name__ == '__main__':
    app = AwesomeWindow()
    camera = cv2.VideoCapture(0)
    rval, image = camera.read()

    app.setOnDraw(onDraw)
    app.setOnCamera(onCamera)
    app.setOnCapture(onCapture)

    app.start()

    camera.release()
    app.quit()
