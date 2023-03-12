# client.py

import grpc
import kv_store_pb2
import kv_store_pb2_grpc


def get_primary_server():
 
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = kv_store_pb2_grpc.RegistryStub(channel)
        response = stub.GetPrimary(kv_store_pb2.Empty())
        return response.ip_address, response.port


def get_replica_servers():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = kv_store_pb2_grpc.RegistryStub(channel)
        response = stub.GetReplicas(kv_store_pb2.Empty())
        return [(r.ip_address, r.port) for r in response.replicas]


def get_kv_store_stub(server_ip, server_port):

    with grpc.insecure_channel(f"{server_ip}:{server_port}") as channel:
        return kv_store_pb2_grpc.KeyValueStoreStub(channel)


def main():
    primary_ip, primary_port = get_primary_server()
    replica_servers = get_replica_servers()

    kv_store_primary_stub = get_kv_store_stub(primary_ip, primary_port)

    response = kv_store_primary_stub.write(kv_store_pb2.KeyValue(key="key1", name="name1", value="value1"))
    print("Write response:", response.key)

    response = kv_store_primary_stub.read(kv_store_pb2.Key(key="key1"))
    print("Read response:", response.name, response.value)

    response = kv_store_primary_stub.delete(kv_store_pb2.Key(key="key1"))
    print("Delete response:", response.success)

    for replica_ip, replica_port in replica_servers:
        kv_store_replica_stub = get_kv_store_stub(replica_ip, replica_port)

        response = kv_store_replica_stub.write(kv_store_pb2.KeyValue(key="key2", name="name2", value="value2"))
        print("Write response from replica:", response.key)

        response = kv_store_replica_stub.read(kv_store_pb2.Key(key="key2"))
        print("Read response from replica:", response.name, response.value)

        response = kv_store_replica_stub.delete(kv_store_pb2.Key(key="key2"))
        print("Delete response from replica:", response.success)


if __name__ == "__main__":
    main()

