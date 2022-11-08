
import gi
import socket
from threading import Thread
from time import sleep

gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib

STREAM_ADDR = "127.0.0.1"
STREAM_PORT = 5000

def create_socket(addr: str=STREAM_ADDR, port: int=STREAM_PORT):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((addr, port))
  print(f"Socket bound: {STREAM_ADDR}:{STREAM_PORT}")
  return s

# Initialise GStreamer
Gst.init()

# Initialise the main loop in a separate thread
main_loop = GLib.MainLoop()
thread = Thread(target=main_loop.run)
thread.start()

#cmd = "v4l2src ! decodebin ! videoconvert ! autovideosink"		# Barebones using webcam input  (ksvideosrc on Win)
#cmd = "fakesrc silent=false num-buffers=3 ! fakesink silent=false"	# State information return by fake elements
cmd = "videotestsrc ! videoconvert ! autovideosink"			# Test video source with colour bars

#cmd_mpeg_rtsp = f"videotestsrc ! ffenc_mpeg4 ! rtpmp4vpay config-interval=3 ! udpsink host={} port={}"

pipeline = Gst.parse_launch(cmd)

# Set the pipeline state to playing and enter loop
pipeline.set_state(Gst.State.PLAYING)
try:
  while True:
    sleep(.1)
except KeyboardInterrupt:
  pass

# Clean up after exiting loop
pipeline.set_state(Gst.State.NULL)
main_loop.quit()
