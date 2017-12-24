import HelloWorld_pb2
import HelloWorld_pb2_grpc
import grpc
import time
from concurrent import futures


class Greeter(HelloWorld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return HelloWorld_pb2.HelloReply(message="hello,%s" % request.name)

    def SayHelloAgain(self, request, context):
        return HelloWorld_pb2.HelloReply(message="hello again,%s" % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    HelloWorld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
