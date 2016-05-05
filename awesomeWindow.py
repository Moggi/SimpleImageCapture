
import os
import gi
gi.require_version('Gtk', '3.0')
import gtk
from gi.repository import Gtk
from gi.repository import GLib

class AwesomeWindow(Gtk.Window):
    WIDTH = 800
    HEIGHT = 640
    refresh_rate = 200 #in milliseconds = 30fps
    IMG = None
    onDraw = None
    onCamera = None
    onCapture = None
    onQuit = None

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Awesome Window")
        self.set_size_request(self.WIDTH,self.HEIGHT)
        self.set_resizable(False)
        self.connect("delete-event", Gtk.main_quit)

        self.init_ui()
        self.show_all()

    def init_ui(self):
        overallGrid = Gtk.Box()

        ############################
        imgLayer = Gtk.Box()

        ## Add the camera/image area
        self.IMG = Gtk.Image()
        #FIXME: usar gtk.DrawingArea
        #TODO: definir tamanho da imagem conforme o tamanho da janela
        self.IMG.connect("draw", self.onRefresh)
        self.IMG.show()
        imgLayer.add(self.IMG)

        ############################
        menuGrid = Gtk.Grid()

        ## Add Camera live button
        button = Gtk.Button.new_with_label("Camera")
        button.connect("clicked", self.on_camera_clicked)
        menuGrid.add(button)

        ## Add Capture image button
        button = Gtk.Button.new_with_label("Capture")
        button.connect("clicked", self.on_capture_clicked)
        menuGrid.add(button)

        ## Add Preview background button
        button = Gtk.Button.new_with_label("Preview")
        # button.connect("clicked", self.on_preview_clicked)
        menuGrid.add(button)

        ## Add Next background button
        button = Gtk.Button.new_with_label("Next")
        # button.connect("clicked", self.on_next_clicked)
        menuGrid.add(button)

        ############################
        overlay = Gtk.Overlay()
        overlay.add(imgLayer)
        overlay.add_overlay(menuGrid)
        overallGrid.add(overlay)
        self.add(overallGrid)

        self.show_all()

    def onRefresh(self,widget, cairo):
        if self.onDraw is None:
            self.quit()

        self.DisplayImage(self.onDraw())
        return True

    def on_capture_clicked(self, button):
        if self.onCapture is not None:
            self.onCapture()

    def on_camera_clicked(self, button):
        if self.onCamera is not None:
            self.onCamera()

    def DisplayImage(self,image):
        if image is not None:
            converted_image = gtk.gdk.pixbuf_new_from_array(image, gtk.gdk.COLORSPACE_RGB, 8)
            self.IMG.set_from_pixbuf(converted_image)
            self.IMG.show()

    def setOnQuit(self, callback):
        self.onQuit = callback

    def setOnCapture(self, callback):
        self.onCapture = callback

    def setOnCamera(self, callback):
        self.onCamera = callback

    def setOnDraw(self, callback):
        self.onDraw = callback

    def on_close_clicked(self, button):
        if self.onQuit is not None:
            self.onQuit()
        Gtk.main_quit()

    def quit(self):
        self.on_close_clicked(None)

    def start(self):
        Gtk.main()
