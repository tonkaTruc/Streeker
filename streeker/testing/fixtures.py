import pytest
from gi.repository import Gst, GLib
from streeker.core.player import StreekerPlayer
from threading import Thread


@pytest.fixture
def streeker_player():
    """
    Fixture to create a GStreamer player instance.
    """

    # Initialise the main loop in a separate thread
    main_loop = GLib.MainLoop()
    thread = Thread(target=main_loop.run)
    thread.start()

    player = StreekerPlayer(name="test", id="test")
    yield player
    player.stop()
    main_loop.quit()
