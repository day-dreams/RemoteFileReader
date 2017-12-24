import json
import sys
import time
import grpc
from concurrent import futures
import RemoteFileReader_pb2
import RemoteFileReader_pb2_grpc

import Works

class RemoteFileServier(RemoteFileReader_pb2_grpc.RemoteFileRreaderServiceServicer):
    def exists(self, request, context):
        filename = request.filename
        rv = Works.RemoteFileReader.check_if_file_exists(filename)
        return RemoteFileReader_pb2.FileStatus(file_exists=rv)

    def read(self, request, context):
        filename=request.filename
        linegenerator=Works.RemoteFileReader.read(filename)
        for line in linegenerator:
            yield RemoteFileReader_pb2.FileLine(line=line)


def serve(jsonobject):

    maxworkers=jsonobject['server']['worker']['max_num']
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=maxworkers))
    RemoteFileReader_pb2_grpc.add_RemoteFileRreaderServiceServicer_to_server(
        RemoteFileServier(), server)

    port = jsonobject['server']['listen']['address'] + \
        ':' + jsonobject['server']['listen']['port']
    server.add_insecure_port(port)
    server.start()

    try:
        while True:
            time.sleep(60 * 10)
    except KeyboardInterrupt as err:
        server.stop(0)

def main():
    josnfilename = sys.argv[-1]
    jsonobject = json.load(open(josnfilename, 'r'))
    serve(jsonobject)


if __name__ == '__main__':
    main()
