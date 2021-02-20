import zmq
import time

if __name__ == "__main__":

    port = "5556"
    context = zmq.Context()
    zsocket = context.socket(zmq.PUB)
    zsocket.bind("tcp://{0}:{1}".format('*', port))
    while True:
        messagedata = b'hello-world'
        print("{0}".format(messagedata))
        zsocket.send(messagedata)
        time.sleep(1)
