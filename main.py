import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2, Gdk

class BrowserWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MS Paint")
        self.set_default_size(1024, 768)

        self.webview = WebKit2.WebView()
        self.webview.load_uri("https://jspaint.app")
        #self.webview.set_zoom_level(1.25)  # Start zoomed in a bit
        self.add(self.webview)

        self.connect("key-press-event", self.on_key_press)

    def on_key_press(self, widget, event):
        ctrl = event.state & Gdk.ModifierType.CONTROL_MASK

        if ctrl:
            if event.keyval == Gdk.KEY_equal or event.keyval == Gdk.KEY_KP_Add:
                self.zoom_in()
                return True
            elif event.keyval == Gdk.KEY_minus or event.keyval == Gdk.KEY_KP_Subtract:
                self.zoom_out()
                return True
            elif event.keyval == Gdk.KEY_0 or event.keyval == Gdk.KEY_KP_0:
                self.reset_zoom()
                return True

        return False

    def zoom_in(self):
        print("zoom in")
        current = self.webview.get_zoom_level()
        self.webview.set_zoom_level(min(current + 0.1, 3.0))

    def zoom_out(self):
        print("zoom out")
        current = self.webview.get_zoom_level()
        self.webview.set_zoom_level(max(current - 0.1, 0.3))

    def reset_zoom(self):
        print("reset")
        self.webview.set_zoom_level(1.0)

win = BrowserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
