import Echo_pb2
import Echo_pb2_grpc
import grpc


def run():
    request = Echo_pb2.EchoRequest(words='hello world')
    channel = grpc.insecure_channel('localhost:8888')
    stub = Echo_pb2_grpc.EchoServiceStub(channel)
    response = stub.echo(request)

    print response.words


def main():
    run()


if __name__ == '__main__':
    main()
