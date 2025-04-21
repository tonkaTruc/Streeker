import socket

STREAM_ADDR = "127.0.0.1"
STREAM_PORT = 5000


def create_socket(addr: str = STREAM_ADDR, port: int = STREAM_PORT) -> socket.socket:
    """Generic socket creation function

    Args:
        addr (str, optional): Address to create the socket with. Defaults to STREAM_ADDR.
        port (int, optional): Bound port for socket communication. Defaults to STREAM_PORT.

    Returns:
        socket.socket: Bound socket object
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((addr, port))
    print(f">> Socket bound: {STREAM_ADDR}:{STREAM_PORT}")
    return s

