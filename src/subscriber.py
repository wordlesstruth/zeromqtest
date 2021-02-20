import zmq
import socket

if __name__ == "__main__":
    port = "5556"

    context = zmq.Context()
    zsocket = context.socket(zmq.SUB)
    zsocket.setsockopt(zmq.SUBSCRIBE, b"")
    zsocket.connect("tcp://{0}:{1}".format(socket.gethostbyname('publisher'), port))
    print("Starting receive loop")
    while True:
        msg = zsocket.recv()
        print(msg)
