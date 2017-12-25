import sys
import json
import grpc
import RemoteFileReader_pb2
import RemoteFileReader_pb2_grpc


def run(jsonobject):
    port = jsonobject['server']['listen']['address'] + \
        ':' + jsonobject['server']['listen']['port']
    channel = grpc.insecure_channel(port)
    stub = RemoteFileReader_pb2_grpc.RemoteFileRreaderServiceStub(channel)

    # filename = sys.argv[-1]

    # response = stub.exists(
    #     RemoteFileReader_pb2.File(filename=filename))

    # if response.file_exists:
    #     responses = stub.read(RemoteFileReader_pb2.File(filename=filename))
    #     for res in responses:
    #         print res.line,
    # else:
    #     print "ERROR_FILE_NOT_EXISTS"

    ress = stub.get_all_filestatus(RemoteFileReader_pb2.EmptyRequest())
    for res in ress:
        print res


def main():
    josnfilename = sys.argv[-1]
    jsonobject = json.load(open(josnfilename, 'r'))
    run(jsonobject)


if __name__ == '__main__':
    main()
