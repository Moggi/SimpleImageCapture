import sys

from PyQt4 import QtCore
from PyQt4 import QtGui

from source.camera import *

class WindowWidget(QtGui.QMainWindow):

    camera = QtCore.pyqtSignal()
    capture = QtCore.pyqtSignal(cv.iplimage)

    def __init__(self, parent=None):
        super(QtGui.QMainWindow, self).__init__(parent)
        self.resize(800,640)
        self.setWindowTitle('Awesome Window')

        self.init_ui()

    def init_ui(self):

        window = QtGui.QWidget(self)
        windowLayout = QtGui.QVBoxLayout()
        windowLayout.setContentsMargins(0,0,0,0)
        window.setLayout(windowLayout)

        #############
        menuContainer = QtGui.QWidget(parent=window)
        menuLayout = QtGui.QHBoxLayout()
        menuContainer.setLayout(menuLayout)

        cameraButton = QtGui.QPushButton("CAMERA",menuContainer)
        cameraButton.clicked.connect(self._clickedCamera)

        menuLayout.addWidget(cameraButton)

        captureButton = QtGui.QPushButton("CAPTURE",menuContainer)
        captureButton.clicked.connect(self._clickedCapture)

        menuLayout.addWidget(captureButton)

        menuLayout.addItem(QtGui.QSpacerItem(0,menuContainer.height(), QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

        menuContainer.show()
        #############

        cameraDevice = CameraDevice(mirrored=True)
        self.cameraWidget = CameraWidget(cameraDevice,window)
        self.cameraWidget.show()

        windowLayout.addWidget(menuContainer)
        windowLayout.addWidget(self.cameraWidget)

        self.setCentralWidget(window)

        self.show()


    def _clickedCapture(self):
        self.capture.emit(self.cameraWidget._frame)

    def _clickedCamera(self):
        self.camera.emit()
