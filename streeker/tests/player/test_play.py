from streeker.testing.fixtures import streeker_player
import time

SOAK_TIME = time.time() + 10


def test_streeker_player(streeker_player):

    streeker_player.start()
    while True:
        if time.time() > SOAK_TIME:
            break
        time.sleep(.1)
    streeker_player.stop()
