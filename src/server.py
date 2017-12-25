#! coding:utf8

import json
import sys
import time
import grpc
from concurrent import futures
import RemoteFileReader_pb2
import RemoteFileReader_pb2_grpc

import Works


class RemoteFileServier(RemoteFileReader_pb2_grpc.RemoteFileRreaderServiceServicer):
    """
        这个类是grpc和业务的中间层
    """

    def __init__(self, jsonobject):
        self.remoteFileReader = Works.RemoteFileReader(jsonobject)

    def exists(self, request, context):
        filename = request.filename
        fstatus_msg = self.remoteFileReader.check_if_file_exists(filename)
        return fstatus_msg

    def read(self, request, context):
        filename = request.filename
        line_message_generator = self.remoteFileReader.read(filename)
        for line_msg in line_message_generator:
            yield line_msg

    def get_all_filestatus(self, request, context):
        fstatus_msg_generator = self.remoteFileReader.get_all_filestatus()
        for msg in fstatus_msg_generator:
            yield msg


def serve(jsonobject):

    maxworkers = jsonobject['server']['worker']['max_num']
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=maxworkers))
    RemoteFileReader_pb2_grpc.add_RemoteFileRreaderServiceServicer_to_server(
        RemoteFileServier(jsonobject), server)

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
