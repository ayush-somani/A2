import grpc
import time
import uuid
import sys
from concurrent import futures

import registry_pb2
import registry_pb2_grpc


class RegistryServer(registry_pb2_grpc.RegistryServicer):

    def __init__(self):
        self.processes = {}
        self.primary_server = None

    def Register(self, request, context):
        process_id = str(uuid.uuid4())
        ip = request.ip
        port = request.port
        self.processes[process_id] = (ip, port)

        if not self.primary_server:
            self.primary_server = self.processes[process_id]
            return registry_pb2.RegisterResponse(is_primary=True)

        return registry_pb2.RegisterResponse(is_primary=False, primary_server_ip=self.primary_server[0], primary_server_port=self.primary_server[1])

    def GetProcesses(self, request, context):
        process_list = [registry_pb2.Process(ip=ip, port=port) for ip, port in self.processes.values()]
        return registry_pb2.GetProcessesResponse(processes=process_list)

    def Unregister(self, request, context):
        process_id = request.process_id
        if process_id in self.processes:
            del self.processes[process_id]
        if self.primary_server == self.processes[process_id]:
            self.primary_server = None

        return registry_pb2.UnregisterResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    registry_pb2_grpc.add_RegistryServicer_to_server(RegistryServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Registry Server started at port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
