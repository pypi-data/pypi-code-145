# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ...muses.v1 import component_service_pb2 as muses_dot_v1_dot_component__service__pb2


class ComponentServiceStub(object):
    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
    info: {
    title: "Component Service"
    version: "1.0"
    contact: {
    name: "Component Service"
    url: "http://github.com/artistml/apis"
    }
    }
    host: "github.com/artistml/apis"
    base_path: "/muses/v1/component"
    schemes: HTTP
    schemes: HTTPS
    consumes: "application/json"
    produces: "application/json"
    external_docs: {
    description: "API specification in Markdown",
    url: "http://github.com/artistml/apis/muses/v1/component"
    }
    };

    The service that handles the CRUD of Component.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateComponent = channel.unary_unary(
                '/muses.v1.ComponentService/CreateComponent',
                request_serializer=muses_dot_v1_dot_component__service__pb2.CreateComponentRequest.SerializeToString,
                response_deserializer=muses_dot_v1_dot_component__service__pb2.CreateComponentResponse.FromString,
                )
        self.GetComponent = channel.unary_unary(
                '/muses.v1.ComponentService/GetComponent',
                request_serializer=muses_dot_v1_dot_component__service__pb2.GetComponentRequest.SerializeToString,
                response_deserializer=muses_dot_v1_dot_component__service__pb2.GetComponentResponse.FromString,
                )
        self.UpdateComponent = channel.unary_unary(
                '/muses.v1.ComponentService/UpdateComponent',
                request_serializer=muses_dot_v1_dot_component__service__pb2.UpdateComponentRequest.SerializeToString,
                response_deserializer=muses_dot_v1_dot_component__service__pb2.UpdateComponentResponse.FromString,
                )
        self.ListComponents = channel.unary_unary(
                '/muses.v1.ComponentService/ListComponents',
                request_serializer=muses_dot_v1_dot_component__service__pb2.ListComponentsRequest.SerializeToString,
                response_deserializer=muses_dot_v1_dot_component__service__pb2.ListComponentsResponse.FromString,
                )
        self.DeleteComponent = channel.unary_unary(
                '/muses.v1.ComponentService/DeleteComponent',
                request_serializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentRequest.SerializeToString,
                response_deserializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentResponse.FromString,
                )
        self.DeleteComponents = channel.unary_unary(
                '/muses.v1.ComponentService/DeleteComponents',
                request_serializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentsRequest.SerializeToString,
                response_deserializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentsResponse.FromString,
                )


class ComponentServiceServicer(object):
    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
    info: {
    title: "Component Service"
    version: "1.0"
    contact: {
    name: "Component Service"
    url: "http://github.com/artistml/apis"
    }
    }
    host: "github.com/artistml/apis"
    base_path: "/muses/v1/component"
    schemes: HTTP
    schemes: HTTPS
    consumes: "application/json"
    produces: "application/json"
    external_docs: {
    description: "API specification in Markdown",
    url: "http://github.com/artistml/apis/muses/v1/component"
    }
    };

    The service that handles the CRUD of Component.
    """

    def CreateComponent(self, request, context):
        """Creates a Component.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComponent(self, request, context):
        """Gets a Component.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateComponent(self, request, context):
        """Updates a Component.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListComponents(self, request, context):
        """Lists Components in a Location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteComponent(self, request, context):
        """Deletes a Component.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteComponents(self, request, context):
        """Batch delete Component by filter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComponentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateComponent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComponent,
                    request_deserializer=muses_dot_v1_dot_component__service__pb2.CreateComponentRequest.FromString,
                    response_serializer=muses_dot_v1_dot_component__service__pb2.CreateComponentResponse.SerializeToString,
            ),
            'GetComponent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetComponent,
                    request_deserializer=muses_dot_v1_dot_component__service__pb2.GetComponentRequest.FromString,
                    response_serializer=muses_dot_v1_dot_component__service__pb2.GetComponentResponse.SerializeToString,
            ),
            'UpdateComponent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateComponent,
                    request_deserializer=muses_dot_v1_dot_component__service__pb2.UpdateComponentRequest.FromString,
                    response_serializer=muses_dot_v1_dot_component__service__pb2.UpdateComponentResponse.SerializeToString,
            ),
            'ListComponents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListComponents,
                    request_deserializer=muses_dot_v1_dot_component__service__pb2.ListComponentsRequest.FromString,
                    response_serializer=muses_dot_v1_dot_component__service__pb2.ListComponentsResponse.SerializeToString,
            ),
            'DeleteComponent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteComponent,
                    request_deserializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentRequest.FromString,
                    response_serializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentResponse.SerializeToString,
            ),
            'DeleteComponents': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteComponents,
                    request_deserializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentsRequest.FromString,
                    response_serializer=muses_dot_v1_dot_component__service__pb2.DeleteComponentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'muses.v1.ComponentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ComponentService(object):
    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
    info: {
    title: "Component Service"
    version: "1.0"
    contact: {
    name: "Component Service"
    url: "http://github.com/artistml/apis"
    }
    }
    host: "github.com/artistml/apis"
    base_path: "/muses/v1/component"
    schemes: HTTP
    schemes: HTTPS
    consumes: "application/json"
    produces: "application/json"
    external_docs: {
    description: "API specification in Markdown",
    url: "http://github.com/artistml/apis/muses/v1/component"
    }
    };

    The service that handles the CRUD of Component.
    """

    @staticmethod
    def CreateComponent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/muses.v1.ComponentService/CreateComponent',
            muses_dot_v1_dot_component__service__pb2.CreateComponentRequest.SerializeToString,
            muses_dot_v1_dot_component__service__pb2.CreateComponentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetComponent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/muses.v1.ComponentService/GetComponent',
            muses_dot_v1_dot_component__service__pb2.GetComponentRequest.SerializeToString,
            muses_dot_v1_dot_component__service__pb2.GetComponentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateComponent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/muses.v1.ComponentService/UpdateComponent',
            muses_dot_v1_dot_component__service__pb2.UpdateComponentRequest.SerializeToString,
            muses_dot_v1_dot_component__service__pb2.UpdateComponentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListComponents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/muses.v1.ComponentService/ListComponents',
            muses_dot_v1_dot_component__service__pb2.ListComponentsRequest.SerializeToString,
            muses_dot_v1_dot_component__service__pb2.ListComponentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteComponent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/muses.v1.ComponentService/DeleteComponent',
            muses_dot_v1_dot_component__service__pb2.DeleteComponentRequest.SerializeToString,
            muses_dot_v1_dot_component__service__pb2.DeleteComponentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteComponents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/muses.v1.ComponentService/DeleteComponents',
            muses_dot_v1_dot_component__service__pb2.DeleteComponentsRequest.SerializeToString,
            muses_dot_v1_dot_component__service__pb2.DeleteComponentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
