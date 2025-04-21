
from streeker.core.player import StreekerPlayer
import gi
from threading import Thread
from time import sleep

gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib

STREAM_ADDR = "127.0.0.1"
STREAM_PORT = 5000


# Initialise GStreamer
Gst.init()

# Initialise the main loop in a separate thread
main_loop = GLib.MainLoop()
thread = Thread(target=main_loop.run)
thread.start()

player = StreekerPlayer(name="test", id="test")
try:
    player.start()
    while True:
        sleep(.1)
except KeyboardInterrupt:
    pass
finally:
    player.stop()

# Clean up after exiting loop
main_loop.quit()
