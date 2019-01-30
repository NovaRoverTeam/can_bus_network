import socket, sys
import struct

sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
interface = "can1"
try:
    sock.bind((interface,))
except OSError:
    sys.stderr.write("Could not bind to interface '%s'\n" % interface)
    # do something about the error...



fmt = "<IB3x8s"
can_pkt = struct.pack(fmt, 0x741, len(b"hello"), b"hello")
sock.send(can_pkt)

