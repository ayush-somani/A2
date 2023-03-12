# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import kv_store_pb2 as kv__store__pb2


class KeyValueStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.write = channel.unary_unary(
                '/kv_store.KeyValueStore/write',
                request_serializer=kv__store__pb2.KeyValue.SerializeToString,
                response_deserializer=kv__store__pb2.Key.FromString,
                )
        self.read = channel.unary_unary(
                '/kv_store.KeyValueStore/read',
                request_serializer=kv__store__pb2.Key.SerializeToString,
                response_deserializer=kv__store__pb2.KeyValue.FromString,
                )
        self.delete = channel.unary_unary(
                '/kv_store.KeyValueStore/delete',
                request_serializer=kv__store__pb2.Key.SerializeToString,
                response_deserializer=kv__store__pb2.SuccessResponse.FromString,
                )


class KeyValueStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'write': grpc.unary_unary_rpc_method_handler(
                    servicer.write,
                    request_deserializer=kv__store__pb2.KeyValue.FromString,
                    response_serializer=kv__store__pb2.Key.SerializeToString,
            ),
            'read': grpc.unary_unary_rpc_method_handler(
                    servicer.read,
                    request_deserializer=kv__store__pb2.Key.FromString,
                    response_serializer=kv__store__pb2.KeyValue.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=kv__store__pb2.Key.FromString,
                    response_serializer=kv__store__pb2.SuccessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kv_store.KeyValueStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeyValueStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kv_store.KeyValueStore/write',
            kv__store__pb2.KeyValue.SerializeToString,
            kv__store__pb2.Key.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kv_store.KeyValueStore/read',
            kv__store__pb2.Key.SerializeToString,
            kv__store__pb2.KeyValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kv_store.KeyValueStore/delete',
            kv__store__pb2.Key.SerializeToString,
            kv__store__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
