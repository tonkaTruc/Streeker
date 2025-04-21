
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

# cmd = "v4l2src ! decodebin ! videoconvert ! autovideosink"		# Barebones using webcam input  (ksvideosrc on Win)
# cmd = "fakesrc silent=false num-buffers=3 ! fakesink silent=false"	# State information return by fake elements
# cmd = "videotestsrc ! videoconvert ! autovideosink"			# Test video source with colour bars

# TODO: Construct the SDP before parsing / launching the pipeline
# Reformat src into mpeg4, convert to RTP payload and send via UDP to given addrs
cmd = f"videotestsrc ! avenc_mpeg4 ! rtpmp4vpay config-interval=3 ! udpsink host={STREAM_ADDR} port={STREAM_PORT}"

# Set the pipeline state to playing and enter loop
pipeline = Gst.parse_launch(cmd)
pipeline.set_state(Gst.State.PLAYING)
print(f">> Running pipeline: {cmd}")
try:
    while True:
        sleep(.1)
except KeyboardInterrupt:
    pass

# Clean up after exiting loop
pipeline.set_state(Gst.State.NULL)
main_loop.quit()
