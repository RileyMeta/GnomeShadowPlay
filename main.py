import sys
import os 

import replay_notification

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

def save_replay():
    os.system('killall -SIGUSR1 gpu-screen-recorder')
    replay_notification.show_popup()

if __name__ == "__main__":
    save_replay()
    Gtk.main()