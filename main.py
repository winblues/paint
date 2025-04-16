import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2, Gdk, Gio

class PaintApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="win.blues.paint",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = BrowserWindow(self)
        win.show_all()

class BrowserWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, title="Paint", application=app)
        self.set_default_size(1024, 768)
        self.set_icon_name("win.blues.paint")  # This sets the app icon

        self.webview = WebKit2.WebView()
        self.webview.load_uri("https://jspaint.app")
        self.webview.set_zoom_level(1.10)
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
        current = self.webview.get_zoom_level()
        self.webview.set_zoom_level(min(current + 0.1, 3.0))

    def zoom_out(self):
        current = self.webview.get_zoom_level()
        self.webview.set_zoom_level(max(current - 0.1, 0.3))

    def reset_zoom(self):
        self.webview.set_zoom_level(1.0)

app = PaintApp()
app.run([])
