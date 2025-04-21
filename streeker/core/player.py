
import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib


class StreekerPlayer:
    """
    A class to represent a Streeker player.
    """

    def __init__(self, name: str, id: str):
        """
        Initialize the player with a name and ID.

        :param name: The name of the player.
        :param id: The ID of the player.
        """
        self.name = name
        self.id = id
        self.cmd = "videotestsrc ! videoconvert ! autovideosink"
        self.pipeline = Gst.parse_launch(self.cmd)

    def start(self):
        """
        Start the player.
        """
        self.pipeline.set_state(Gst.State.PLAYING)
        print(f">> Running pipeline: {self.cmd}")

    def stop(self):
        """
        Stop the player.
        """
        self.pipeline.set_state(Gst.State.NULL)
        print(f">> Stopping pipeline: {self.cmd}")
