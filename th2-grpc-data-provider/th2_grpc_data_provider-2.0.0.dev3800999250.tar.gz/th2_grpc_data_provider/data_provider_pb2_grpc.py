# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from th2_grpc_common import common_pb2 as th2__grpc__common_dot_common__pb2
from th2_grpc_data_provider import data_provider_pb2 as th2__grpc__data__provider_dot_data__provider__pb2


class DataProviderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getEvent = channel.unary_unary(
                '/th2.data_provider.DataProvider/getEvent',
                request_serializer=th2__grpc__common_dot_common__pb2.EventID.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.EventResponse.FromString,
                )
        self.getEvents = channel.unary_unary(
                '/th2.data_provider.DataProvider/getEvents',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.BulkEventRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.BulkEventResponse.FromString,
                )
        self.getMessage = channel.unary_unary(
                '/th2.data_provider.DataProvider/getMessage',
                request_serializer=th2__grpc__common_dot_common__pb2.MessageID.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageGroupResponse.FromString,
                )
        self.getMessageStreams = channel.unary_unary(
                '/th2.data_provider.DataProvider/getMessageStreams',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageStreamsRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageStreamsResponse.FromString,
                )
        self.getBooks = channel.unary_unary(
                '/th2.data_provider.DataProvider/getBooks',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.BooksRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.BooksResponse.FromString,
                )
        self.searchMessages = channel.unary_stream(
                '/th2.data_provider.DataProvider/searchMessages',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchResponse.FromString,
                )
        self.searchEvents = channel.unary_stream(
                '/th2.data_provider.DataProvider/searchEvents',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.EventSearchRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.EventSearchResponse.FromString,
                )
        self.loadCradleMessageGroups = channel.unary_unary(
                '/th2.data_provider.DataProvider/loadCradleMessageGroups',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.CradleMessageGroupsRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.CradleMessageGroupsResponse.FromString,
                )
        self.searchMessageGroups = channel.unary_stream(
                '/th2.data_provider.DataProvider/searchMessageGroups',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageGroupsSearchRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchResponse.FromString,
                )
        self.getMessagesFilters = channel.unary_unary(
                '/th2.data_provider.DataProvider/getMessagesFilters',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageFiltersRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterNamesResponse.FromString,
                )
        self.getEventsFilters = channel.unary_unary(
                '/th2.data_provider.DataProvider/getEventsFilters',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.EventFiltersRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterNamesResponse.FromString,
                )
        self.getEventFilterInfo = channel.unary_unary(
                '/th2.data_provider.DataProvider/getEventFilterInfo',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoResponse.FromString,
                )
        self.getMessageFilterInfo = channel.unary_unary(
                '/th2.data_provider.DataProvider/getMessageFilterInfo',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoResponse.FromString,
                )
        self.matchEvent = channel.unary_unary(
                '/th2.data_provider.DataProvider/matchEvent',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.EventMatchRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MatchResponse.FromString,
                )
        self.matchMessage = channel.unary_unary(
                '/th2.data_provider.DataProvider/matchMessage',
                request_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageMatchRequest.SerializeToString,
                response_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MatchResponse.FromString,
                )


class DataProviderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getEvent(self, request, context):
        """returns a single event with the specified id 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEvents(self, request, context):
        """returns a list of events with the specified ids 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessage(self, request, context):
        """returns a single message with the specified id 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessageStreams(self, request, context):
        """returns a list of message stream names 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBooks(self, request, context):
        """Returns the set of books stored in cradle cache
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def searchMessages(self, request, context):
        """creates a message stream that matches the filter. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def searchEvents(self, request, context):
        """creates an event or an event metadata stream that matches the filter. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def loadCradleMessageGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def searchMessageGroups(self, request, context):
        """
        Searches for messages groups in specified timestamp
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessagesFilters(self, request, context):
        """returns available message filters 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEventsFilters(self, request, context):
        """returns available event filters 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEventFilterInfo(self, request, context):
        """returns available filter parameters 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessageFilterInfo(self, request, context):
        """returns available filter parameters 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def matchEvent(self, request, context):
        """checks if the specified event matches the filter 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def matchMessage(self, request, context):
        """checks if the specified message matches the filter 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataProviderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.getEvent,
                    request_deserializer=th2__grpc__common_dot_common__pb2.EventID.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.EventResponse.SerializeToString,
            ),
            'getEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.getEvents,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.BulkEventRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.BulkEventResponse.SerializeToString,
            ),
            'getMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.getMessage,
                    request_deserializer=th2__grpc__common_dot_common__pb2.MessageID.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageGroupResponse.SerializeToString,
            ),
            'getMessageStreams': grpc.unary_unary_rpc_method_handler(
                    servicer.getMessageStreams,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageStreamsRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageStreamsResponse.SerializeToString,
            ),
            'getBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.getBooks,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.BooksRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.BooksResponse.SerializeToString,
            ),
            'searchMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.searchMessages,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchResponse.SerializeToString,
            ),
            'searchEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.searchEvents,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.EventSearchRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.EventSearchResponse.SerializeToString,
            ),
            'loadCradleMessageGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.loadCradleMessageGroups,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.CradleMessageGroupsRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.CradleMessageGroupsResponse.SerializeToString,
            ),
            'searchMessageGroups': grpc.unary_stream_rpc_method_handler(
                    servicer.searchMessageGroups,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageGroupsSearchRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchResponse.SerializeToString,
            ),
            'getMessagesFilters': grpc.unary_unary_rpc_method_handler(
                    servicer.getMessagesFilters,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageFiltersRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterNamesResponse.SerializeToString,
            ),
            'getEventsFilters': grpc.unary_unary_rpc_method_handler(
                    servicer.getEventsFilters,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.EventFiltersRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterNamesResponse.SerializeToString,
            ),
            'getEventFilterInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getEventFilterInfo,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoResponse.SerializeToString,
            ),
            'getMessageFilterInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getMessageFilterInfo,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoResponse.SerializeToString,
            ),
            'matchEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.matchEvent,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.EventMatchRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MatchResponse.SerializeToString,
            ),
            'matchMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.matchMessage,
                    request_deserializer=th2__grpc__data__provider_dot_data__provider__pb2.MessageMatchRequest.FromString,
                    response_serializer=th2__grpc__data__provider_dot_data__provider__pb2.MatchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'th2.data_provider.DataProvider', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataProvider(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getEvent',
            th2__grpc__common_dot_common__pb2.EventID.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.EventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getEvents',
            th2__grpc__data__provider_dot_data__provider__pb2.BulkEventRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.BulkEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getMessage',
            th2__grpc__common_dot_common__pb2.MessageID.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.MessageGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMessageStreams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getMessageStreams',
            th2__grpc__data__provider_dot_data__provider__pb2.MessageStreamsRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.MessageStreamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getBooks',
            th2__grpc__data__provider_dot_data__provider__pb2.BooksRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.BooksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def searchMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.DataProvider/searchMessages',
            th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def searchEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.DataProvider/searchEvents',
            th2__grpc__data__provider_dot_data__provider__pb2.EventSearchRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.EventSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def loadCradleMessageGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/loadCradleMessageGroups',
            th2__grpc__data__provider_dot_data__provider__pb2.CradleMessageGroupsRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.CradleMessageGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def searchMessageGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/th2.data_provider.DataProvider/searchMessageGroups',
            th2__grpc__data__provider_dot_data__provider__pb2.MessageGroupsSearchRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.MessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMessagesFilters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getMessagesFilters',
            th2__grpc__data__provider_dot_data__provider__pb2.MessageFiltersRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.FilterNamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEventsFilters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getEventsFilters',
            th2__grpc__data__provider_dot_data__provider__pb2.EventFiltersRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.FilterNamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEventFilterInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getEventFilterInfo',
            th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMessageFilterInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/getMessageFilterInfo',
            th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.FilterInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def matchEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/matchEvent',
            th2__grpc__data__provider_dot_data__provider__pb2.EventMatchRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.MatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def matchMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/th2.data_provider.DataProvider/matchMessage',
            th2__grpc__data__provider_dot_data__provider__pb2.MessageMatchRequest.SerializeToString,
            th2__grpc__data__provider_dot_data__provider__pb2.MatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
