import Echo_pb2
import Echo_pb2_grpc
import grpc
import time

from concurrent import futures


class MyEcho(Echo_pb2_grpc.EchoServiceServicer):
    def echo(self, request, context):
        return Echo_pb2.EchoReply(words=request.words)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    Echo_pb2_grpc.add_EchoServiceServicer_to_server(MyEcho(), server)

    server.add_insecure_port('0.0.0.0:8888')
    server.start()

    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        server.stop(0)


def main():
    serve()


if __name__ == '__main__':
    main()
