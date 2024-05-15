import sys
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

class ReplayNotification(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Popup")
        self.set_default_size(275, 75)
        self.set_position(Gtk.WindowPosition.NONE)  # Disable automatic positioning
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_keep_above(True)     # Keep window always on top
        self.set_accept_focus(False)  # Prevent the window from taking focus
        self.connect("destroy", Gtk.main_quit)
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.add(self.box)
        
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            # Set the Replay Image and it's scaling
        filename="assets/replay.svg",
        width=100, 
        height=50, 
        preserve_aspect_ratio=True)

        self.image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a box to contain the image and label
        image_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        image_box.pack_start(self.image, False, False, 0)
        
        # Create a label
        self.label = Gtk.Label()
        self.label.set_text("Replay Saved!")
        
        # Pack the label into the image box
        image_box.pack_start(self.label, False, False, 0)
        
        # Pack the image box into the main box
        self.box.pack_start(image_box, True, True, 0)

        # Apply CSS style
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(b"""
            #popup_label {
                font-size: 18px;
                font-weight: bold;
                color: white;
            }
            #popup_window {
                background: linear-gradient(0.25turn, #e66465, #9198e5);
                border-left: 4px solid rgb(229, 222, 145);
            }
        """)
        screen = Gdk.Screen.get_default()
        Gtk.StyleContext.add_provider_for_screen(screen, style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.label.set_name("popup_label")
        self.set_name("popup_window")

        # Position window on primary monitor with offset
        self.position_window_with_offset(1920, 150)
        # self.open_window()
        
        self.connect("button-press-event", self.on_button_press)
        
        self.show_all()
        GLib.timeout_add_seconds(5, self.close_window)
        
    def position_window_on_primary_monitor(self):
        primary_monitor = Gdk.Display.get_default().get_primary_monitor()
        primary_geometry = primary_monitor.get_geometry()
        window_width, window_height = self.get_size()
        
        # Calculate center position of the primary monitor
        x = primary_geometry.x + (primary_geometry.width - window_width) // 2
        y = primary_geometry.y + (primary_geometry.height - window_height) // 2
        
        # Move the window to the calculated position
        self.move(x, y)
        
    def position_window_with_offset(self, x_offset, y_offset):
        primary_monitor = Gdk.Display.get_default().get_primary_monitor()
        primary_geometry = primary_monitor.get_geometry()
        window_width, window_height = self.get_size()

        # Calculate position with offset
        x = primary_geometry.x + x_offset
        y = primary_geometry.y + y_offset

        # Ensure the window fits within the primary monitor
        x = max(primary_geometry.x, min(x, primary_geometry.x + primary_geometry.width - window_width))
        y = max(primary_geometry.y, min(y, primary_geometry.y + primary_geometry.height - window_height))

        # Move the window to the calculated position
        self.move(x, y)
    
    def on_button_press(self, widget, event):
        if event.button == Gdk.BUTTON_PRIMARY:
            return True  # Prevent the event from propagating further
        
    def close_window(self):
        self.slide_out(275)        
    
    def open_window(self):
        self.slide_in(-275)

    def slide_in(self, target_x):
        def animate_slide():
            nonlocal frame_count
            nonlocal current_x
            
            if frame_count <= 24:
                if current_x > target_x:
                    current_x -= 10  # Adjust the amount you want the window to slide out by
                    self.move(current_x, self.get_position()[1])  # Move the window horizontally
                    frame_count += 3
                    return True
                else:
                    return False  # Stop the timeout if the window reaches the target position
        
        frame_count = 0
        current_x, _ = self.get_position()
        GLib.timeout_add(30, animate_slide)  # Call animate_slide every 30 milliseconds

    def slide_out(self, target_x):
        def animate_slide():
            nonlocal frame_count
            nonlocal current_x
            
            if frame_count <= 54:
                if current_x > target_x:
                    current_x += 10  # Adjust the amount you want the window to slide out by
                    self.move(current_x, self.get_position()[1])  # Move the window horizontally
                    frame_count += 2
                    return True
                else:
                    return False  # Stop the timeout if the window reaches the target position
            else:
                self.destroy()

        frame_count = 0
        current_x, _ = self.get_position()
        GLib.timeout_add(30, animate_slide)  # Call animate_slide every 30 milliseconds

def show_popup():
    win = ReplayNotification()
    win.show()
    GLib.timeout_add_seconds(5, lambda: win.slide_out(target_x=2270))  # Slide out to x coordinate 2270 after 5 seconds

if __name__ == "__main__":
    show_popup()
    Gtk.main()
