from .messaging import LivesplitMessaging
from .networking import LivesplitConnection


def get_client(server="localhost", port=16834, timeout=1):
    return LivesplitMessaging(LivesplitConnection(server, port, timeout))
