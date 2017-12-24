import HelloWorld_pb2
import HelloWorld_pb2_grpc
import grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = HelloWorld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(HelloWorld_pb2.HelloRequest(name='daydream'))
    print("greeter client received: " + response.message)


if __name__ == "__main__":
    run()
