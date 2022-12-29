# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: modal_proto/api.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.empty_pb2
import modal_proto.api_pb2


class ModalClientBase(abc.ABC):

    @abc.abstractmethod
    async def AppCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppCreateRequest, modal_proto.api_pb2.AppCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppClientDisconnect(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppClientDisconnectRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def AppGetLogs(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppGetLogsRequest, modal_proto.api_pb2.TaskLogsBatch]') -> None:
        pass

    @abc.abstractmethod
    async def AppSetObjects(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppSetObjectsRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def AppGetObjects(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppGetObjectsRequest, modal_proto.api_pb2.AppGetObjectsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppList(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, modal_proto.api_pb2.AppListResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppLookupObject(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppLookupObjectRequest, modal_proto.api_pb2.AppLookupObjectResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppDeploy(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppDeployRequest, modal_proto.api_pb2.AppDeployResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppGetByDeploymentName(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppGetByDeploymentNameRequest, modal_proto.api_pb2.AppGetByDeploymentNameResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AppStop(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppStopRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def AppHeartbeat(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.AppHeartbeatRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def BlobCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.BlobCreateRequest, modal_proto.api_pb2.BlobCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BlobGet(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.BlobGetRequest, modal_proto.api_pb2.BlobGetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClientCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.ClientCreateRequest, modal_proto.api_pb2.ClientCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClientHeartbeat(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.ClientHeartbeatRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ContainerHeartbeat(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.ContainerHeartbeatRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def DictCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.DictCreateRequest, modal_proto.api_pb2.DictCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DictUpdate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.DictUpdateRequest, modal_proto.api_pb2.DictUpdateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DictGet(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.DictGetRequest, modal_proto.api_pb2.DictGetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DictPop(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.DictPopRequest, modal_proto.api_pb2.DictPopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DictContains(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.DictContainsRequest, modal_proto.api_pb2.DictContainsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DictLen(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.DictLenRequest, modal_proto.api_pb2.DictLenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionCreateRequest, modal_proto.api_pb2.FunctionCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionGetSerialized(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionGetSerializedRequest, modal_proto.api_pb2.FunctionGetSerializedResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionMap(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionMapRequest, modal_proto.api_pb2.FunctionMapResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionPutInputs(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionPutInputsRequest, modal_proto.api_pb2.FunctionPutInputsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionPutOutputs(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionPutOutputsRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionGetInputs(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionGetInputsRequest, modal_proto.api_pb2.FunctionGetInputsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionGetOutputs(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionGetOutputsRequest, modal_proto.api_pb2.FunctionGetOutputsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionGetCallGraph(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionGetCallGraphRequest, modal_proto.api_pb2.FunctionGetCallGraphResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FunctionGetCurrentStats(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.FunctionGetCurrentStatsRequest, modal_proto.api_pb2.FunctionStats]') -> None:
        pass

    @abc.abstractmethod
    async def ImageGetOrCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.ImageGetOrCreateRequest, modal_proto.api_pb2.ImageGetOrCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ImageJoin(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.ImageJoinRequest, modal_proto.api_pb2.ImageJoinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MountPutFile(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.MountPutFileRequest, modal_proto.api_pb2.MountPutFileResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MountBuild(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.MountBuildRequest, modal_proto.api_pb2.MountBuildResponse]') -> None:
        pass

    @abc.abstractmethod
    async def QueueCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.QueueCreateRequest, modal_proto.api_pb2.QueueCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def QueueGet(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.QueueGetRequest, modal_proto.api_pb2.QueueGetResponse]') -> None:
        pass

    @abc.abstractmethod
    async def QueuePut(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.QueuePutRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SecretCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.SecretCreateRequest, modal_proto.api_pb2.SecretCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SecretList(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, modal_proto.api_pb2.SecretListResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SharedVolumeCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.SharedVolumeCreateRequest, modal_proto.api_pb2.SharedVolumeCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SharedVolumeList(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, modal_proto.api_pb2.SharedVolumeListResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SharedVolumeListFiles(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.SharedVolumeListFilesRequest, modal_proto.api_pb2.SharedVolumeListFilesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SharedVolumePutFile(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.SharedVolumePutFileRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SharedVolumeGetFile(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.SharedVolumeGetFileRequest, modal_proto.api_pb2.SharedVolumeGetFileResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SharedVolumeRemoveFile(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.SharedVolumeRemoveFileRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def TaskResult(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.TaskResultRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def TokenFlowCreate(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.TokenFlowCreateRequest, modal_proto.api_pb2.TokenFlowCreateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TokenFlowWait(self, stream: 'grpclib.server.Stream[modal_proto.api_pb2.TokenFlowWaitRequest, modal_proto.api_pb2.TokenFlowWaitResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/modal.client.ModalClient/AppCreate': grpclib.const.Handler(
                self.AppCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppCreateRequest,
                modal_proto.api_pb2.AppCreateResponse,
            ),
            '/modal.client.ModalClient/AppClientDisconnect': grpclib.const.Handler(
                self.AppClientDisconnect,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppClientDisconnectRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/AppGetLogs': grpclib.const.Handler(
                self.AppGetLogs,
                grpclib.const.Cardinality.UNARY_STREAM,
                modal_proto.api_pb2.AppGetLogsRequest,
                modal_proto.api_pb2.TaskLogsBatch,
            ),
            '/modal.client.ModalClient/AppSetObjects': grpclib.const.Handler(
                self.AppSetObjects,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppSetObjectsRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/AppGetObjects': grpclib.const.Handler(
                self.AppGetObjects,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppGetObjectsRequest,
                modal_proto.api_pb2.AppGetObjectsResponse,
            ),
            '/modal.client.ModalClient/AppList': grpclib.const.Handler(
                self.AppList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                modal_proto.api_pb2.AppListResponse,
            ),
            '/modal.client.ModalClient/AppLookupObject': grpclib.const.Handler(
                self.AppLookupObject,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppLookupObjectRequest,
                modal_proto.api_pb2.AppLookupObjectResponse,
            ),
            '/modal.client.ModalClient/AppDeploy': grpclib.const.Handler(
                self.AppDeploy,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppDeployRequest,
                modal_proto.api_pb2.AppDeployResponse,
            ),
            '/modal.client.ModalClient/AppGetByDeploymentName': grpclib.const.Handler(
                self.AppGetByDeploymentName,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppGetByDeploymentNameRequest,
                modal_proto.api_pb2.AppGetByDeploymentNameResponse,
            ),
            '/modal.client.ModalClient/AppStop': grpclib.const.Handler(
                self.AppStop,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppStopRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/AppHeartbeat': grpclib.const.Handler(
                self.AppHeartbeat,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.AppHeartbeatRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/BlobCreate': grpclib.const.Handler(
                self.BlobCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.BlobCreateRequest,
                modal_proto.api_pb2.BlobCreateResponse,
            ),
            '/modal.client.ModalClient/BlobGet': grpclib.const.Handler(
                self.BlobGet,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.BlobGetRequest,
                modal_proto.api_pb2.BlobGetResponse,
            ),
            '/modal.client.ModalClient/ClientCreate': grpclib.const.Handler(
                self.ClientCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.ClientCreateRequest,
                modal_proto.api_pb2.ClientCreateResponse,
            ),
            '/modal.client.ModalClient/ClientHeartbeat': grpclib.const.Handler(
                self.ClientHeartbeat,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.ClientHeartbeatRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/ContainerHeartbeat': grpclib.const.Handler(
                self.ContainerHeartbeat,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.ContainerHeartbeatRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/DictCreate': grpclib.const.Handler(
                self.DictCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.DictCreateRequest,
                modal_proto.api_pb2.DictCreateResponse,
            ),
            '/modal.client.ModalClient/DictUpdate': grpclib.const.Handler(
                self.DictUpdate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.DictUpdateRequest,
                modal_proto.api_pb2.DictUpdateResponse,
            ),
            '/modal.client.ModalClient/DictGet': grpclib.const.Handler(
                self.DictGet,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.DictGetRequest,
                modal_proto.api_pb2.DictGetResponse,
            ),
            '/modal.client.ModalClient/DictPop': grpclib.const.Handler(
                self.DictPop,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.DictPopRequest,
                modal_proto.api_pb2.DictPopResponse,
            ),
            '/modal.client.ModalClient/DictContains': grpclib.const.Handler(
                self.DictContains,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.DictContainsRequest,
                modal_proto.api_pb2.DictContainsResponse,
            ),
            '/modal.client.ModalClient/DictLen': grpclib.const.Handler(
                self.DictLen,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.DictLenRequest,
                modal_proto.api_pb2.DictLenResponse,
            ),
            '/modal.client.ModalClient/FunctionCreate': grpclib.const.Handler(
                self.FunctionCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionCreateRequest,
                modal_proto.api_pb2.FunctionCreateResponse,
            ),
            '/modal.client.ModalClient/FunctionGetSerialized': grpclib.const.Handler(
                self.FunctionGetSerialized,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionGetSerializedRequest,
                modal_proto.api_pb2.FunctionGetSerializedResponse,
            ),
            '/modal.client.ModalClient/FunctionMap': grpclib.const.Handler(
                self.FunctionMap,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionMapRequest,
                modal_proto.api_pb2.FunctionMapResponse,
            ),
            '/modal.client.ModalClient/FunctionPutInputs': grpclib.const.Handler(
                self.FunctionPutInputs,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionPutInputsRequest,
                modal_proto.api_pb2.FunctionPutInputsResponse,
            ),
            '/modal.client.ModalClient/FunctionPutOutputs': grpclib.const.Handler(
                self.FunctionPutOutputs,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionPutOutputsRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/FunctionGetInputs': grpclib.const.Handler(
                self.FunctionGetInputs,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionGetInputsRequest,
                modal_proto.api_pb2.FunctionGetInputsResponse,
            ),
            '/modal.client.ModalClient/FunctionGetOutputs': grpclib.const.Handler(
                self.FunctionGetOutputs,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionGetOutputsRequest,
                modal_proto.api_pb2.FunctionGetOutputsResponse,
            ),
            '/modal.client.ModalClient/FunctionGetCallGraph': grpclib.const.Handler(
                self.FunctionGetCallGraph,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionGetCallGraphRequest,
                modal_proto.api_pb2.FunctionGetCallGraphResponse,
            ),
            '/modal.client.ModalClient/FunctionGetCurrentStats': grpclib.const.Handler(
                self.FunctionGetCurrentStats,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.FunctionGetCurrentStatsRequest,
                modal_proto.api_pb2.FunctionStats,
            ),
            '/modal.client.ModalClient/ImageGetOrCreate': grpclib.const.Handler(
                self.ImageGetOrCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.ImageGetOrCreateRequest,
                modal_proto.api_pb2.ImageGetOrCreateResponse,
            ),
            '/modal.client.ModalClient/ImageJoin': grpclib.const.Handler(
                self.ImageJoin,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.ImageJoinRequest,
                modal_proto.api_pb2.ImageJoinResponse,
            ),
            '/modal.client.ModalClient/MountPutFile': grpclib.const.Handler(
                self.MountPutFile,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.MountPutFileRequest,
                modal_proto.api_pb2.MountPutFileResponse,
            ),
            '/modal.client.ModalClient/MountBuild': grpclib.const.Handler(
                self.MountBuild,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.MountBuildRequest,
                modal_proto.api_pb2.MountBuildResponse,
            ),
            '/modal.client.ModalClient/QueueCreate': grpclib.const.Handler(
                self.QueueCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.QueueCreateRequest,
                modal_proto.api_pb2.QueueCreateResponse,
            ),
            '/modal.client.ModalClient/QueueGet': grpclib.const.Handler(
                self.QueueGet,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.QueueGetRequest,
                modal_proto.api_pb2.QueueGetResponse,
            ),
            '/modal.client.ModalClient/QueuePut': grpclib.const.Handler(
                self.QueuePut,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.QueuePutRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/SecretCreate': grpclib.const.Handler(
                self.SecretCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.SecretCreateRequest,
                modal_proto.api_pb2.SecretCreateResponse,
            ),
            '/modal.client.ModalClient/SecretList': grpclib.const.Handler(
                self.SecretList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                modal_proto.api_pb2.SecretListResponse,
            ),
            '/modal.client.ModalClient/SharedVolumeCreate': grpclib.const.Handler(
                self.SharedVolumeCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.SharedVolumeCreateRequest,
                modal_proto.api_pb2.SharedVolumeCreateResponse,
            ),
            '/modal.client.ModalClient/SharedVolumeList': grpclib.const.Handler(
                self.SharedVolumeList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                modal_proto.api_pb2.SharedVolumeListResponse,
            ),
            '/modal.client.ModalClient/SharedVolumeListFiles': grpclib.const.Handler(
                self.SharedVolumeListFiles,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.SharedVolumeListFilesRequest,
                modal_proto.api_pb2.SharedVolumeListFilesResponse,
            ),
            '/modal.client.ModalClient/SharedVolumePutFile': grpclib.const.Handler(
                self.SharedVolumePutFile,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.SharedVolumePutFileRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/SharedVolumeGetFile': grpclib.const.Handler(
                self.SharedVolumeGetFile,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.SharedVolumeGetFileRequest,
                modal_proto.api_pb2.SharedVolumeGetFileResponse,
            ),
            '/modal.client.ModalClient/SharedVolumeRemoveFile': grpclib.const.Handler(
                self.SharedVolumeRemoveFile,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.SharedVolumeRemoveFileRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/TaskResult': grpclib.const.Handler(
                self.TaskResult,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.TaskResultRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/modal.client.ModalClient/TokenFlowCreate': grpclib.const.Handler(
                self.TokenFlowCreate,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.TokenFlowCreateRequest,
                modal_proto.api_pb2.TokenFlowCreateResponse,
            ),
            '/modal.client.ModalClient/TokenFlowWait': grpclib.const.Handler(
                self.TokenFlowWait,
                grpclib.const.Cardinality.UNARY_UNARY,
                modal_proto.api_pb2.TokenFlowWaitRequest,
                modal_proto.api_pb2.TokenFlowWaitResponse,
            ),
        }


class ModalClientStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AppCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppCreate',
            modal_proto.api_pb2.AppCreateRequest,
            modal_proto.api_pb2.AppCreateResponse,
        )
        self.AppClientDisconnect = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppClientDisconnect',
            modal_proto.api_pb2.AppClientDisconnectRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.AppGetLogs = grpclib.client.UnaryStreamMethod(
            channel,
            '/modal.client.ModalClient/AppGetLogs',
            modal_proto.api_pb2.AppGetLogsRequest,
            modal_proto.api_pb2.TaskLogsBatch,
        )
        self.AppSetObjects = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppSetObjects',
            modal_proto.api_pb2.AppSetObjectsRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.AppGetObjects = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppGetObjects',
            modal_proto.api_pb2.AppGetObjectsRequest,
            modal_proto.api_pb2.AppGetObjectsResponse,
        )
        self.AppList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppList',
            google.protobuf.empty_pb2.Empty,
            modal_proto.api_pb2.AppListResponse,
        )
        self.AppLookupObject = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppLookupObject',
            modal_proto.api_pb2.AppLookupObjectRequest,
            modal_proto.api_pb2.AppLookupObjectResponse,
        )
        self.AppDeploy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppDeploy',
            modal_proto.api_pb2.AppDeployRequest,
            modal_proto.api_pb2.AppDeployResponse,
        )
        self.AppGetByDeploymentName = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppGetByDeploymentName',
            modal_proto.api_pb2.AppGetByDeploymentNameRequest,
            modal_proto.api_pb2.AppGetByDeploymentNameResponse,
        )
        self.AppStop = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppStop',
            modal_proto.api_pb2.AppStopRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.AppHeartbeat = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/AppHeartbeat',
            modal_proto.api_pb2.AppHeartbeatRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.BlobCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/BlobCreate',
            modal_proto.api_pb2.BlobCreateRequest,
            modal_proto.api_pb2.BlobCreateResponse,
        )
        self.BlobGet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/BlobGet',
            modal_proto.api_pb2.BlobGetRequest,
            modal_proto.api_pb2.BlobGetResponse,
        )
        self.ClientCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/ClientCreate',
            modal_proto.api_pb2.ClientCreateRequest,
            modal_proto.api_pb2.ClientCreateResponse,
        )
        self.ClientHeartbeat = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/ClientHeartbeat',
            modal_proto.api_pb2.ClientHeartbeatRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ContainerHeartbeat = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/ContainerHeartbeat',
            modal_proto.api_pb2.ContainerHeartbeatRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.DictCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/DictCreate',
            modal_proto.api_pb2.DictCreateRequest,
            modal_proto.api_pb2.DictCreateResponse,
        )
        self.DictUpdate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/DictUpdate',
            modal_proto.api_pb2.DictUpdateRequest,
            modal_proto.api_pb2.DictUpdateResponse,
        )
        self.DictGet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/DictGet',
            modal_proto.api_pb2.DictGetRequest,
            modal_proto.api_pb2.DictGetResponse,
        )
        self.DictPop = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/DictPop',
            modal_proto.api_pb2.DictPopRequest,
            modal_proto.api_pb2.DictPopResponse,
        )
        self.DictContains = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/DictContains',
            modal_proto.api_pb2.DictContainsRequest,
            modal_proto.api_pb2.DictContainsResponse,
        )
        self.DictLen = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/DictLen',
            modal_proto.api_pb2.DictLenRequest,
            modal_proto.api_pb2.DictLenResponse,
        )
        self.FunctionCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionCreate',
            modal_proto.api_pb2.FunctionCreateRequest,
            modal_proto.api_pb2.FunctionCreateResponse,
        )
        self.FunctionGetSerialized = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionGetSerialized',
            modal_proto.api_pb2.FunctionGetSerializedRequest,
            modal_proto.api_pb2.FunctionGetSerializedResponse,
        )
        self.FunctionMap = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionMap',
            modal_proto.api_pb2.FunctionMapRequest,
            modal_proto.api_pb2.FunctionMapResponse,
        )
        self.FunctionPutInputs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionPutInputs',
            modal_proto.api_pb2.FunctionPutInputsRequest,
            modal_proto.api_pb2.FunctionPutInputsResponse,
        )
        self.FunctionPutOutputs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionPutOutputs',
            modal_proto.api_pb2.FunctionPutOutputsRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.FunctionGetInputs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionGetInputs',
            modal_proto.api_pb2.FunctionGetInputsRequest,
            modal_proto.api_pb2.FunctionGetInputsResponse,
        )
        self.FunctionGetOutputs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionGetOutputs',
            modal_proto.api_pb2.FunctionGetOutputsRequest,
            modal_proto.api_pb2.FunctionGetOutputsResponse,
        )
        self.FunctionGetCallGraph = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionGetCallGraph',
            modal_proto.api_pb2.FunctionGetCallGraphRequest,
            modal_proto.api_pb2.FunctionGetCallGraphResponse,
        )
        self.FunctionGetCurrentStats = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/FunctionGetCurrentStats',
            modal_proto.api_pb2.FunctionGetCurrentStatsRequest,
            modal_proto.api_pb2.FunctionStats,
        )
        self.ImageGetOrCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/ImageGetOrCreate',
            modal_proto.api_pb2.ImageGetOrCreateRequest,
            modal_proto.api_pb2.ImageGetOrCreateResponse,
        )
        self.ImageJoin = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/ImageJoin',
            modal_proto.api_pb2.ImageJoinRequest,
            modal_proto.api_pb2.ImageJoinResponse,
        )
        self.MountPutFile = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/MountPutFile',
            modal_proto.api_pb2.MountPutFileRequest,
            modal_proto.api_pb2.MountPutFileResponse,
        )
        self.MountBuild = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/MountBuild',
            modal_proto.api_pb2.MountBuildRequest,
            modal_proto.api_pb2.MountBuildResponse,
        )
        self.QueueCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/QueueCreate',
            modal_proto.api_pb2.QueueCreateRequest,
            modal_proto.api_pb2.QueueCreateResponse,
        )
        self.QueueGet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/QueueGet',
            modal_proto.api_pb2.QueueGetRequest,
            modal_proto.api_pb2.QueueGetResponse,
        )
        self.QueuePut = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/QueuePut',
            modal_proto.api_pb2.QueuePutRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SecretCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SecretCreate',
            modal_proto.api_pb2.SecretCreateRequest,
            modal_proto.api_pb2.SecretCreateResponse,
        )
        self.SecretList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SecretList',
            google.protobuf.empty_pb2.Empty,
            modal_proto.api_pb2.SecretListResponse,
        )
        self.SharedVolumeCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SharedVolumeCreate',
            modal_proto.api_pb2.SharedVolumeCreateRequest,
            modal_proto.api_pb2.SharedVolumeCreateResponse,
        )
        self.SharedVolumeList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SharedVolumeList',
            google.protobuf.empty_pb2.Empty,
            modal_proto.api_pb2.SharedVolumeListResponse,
        )
        self.SharedVolumeListFiles = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SharedVolumeListFiles',
            modal_proto.api_pb2.SharedVolumeListFilesRequest,
            modal_proto.api_pb2.SharedVolumeListFilesResponse,
        )
        self.SharedVolumePutFile = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SharedVolumePutFile',
            modal_proto.api_pb2.SharedVolumePutFileRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SharedVolumeGetFile = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SharedVolumeGetFile',
            modal_proto.api_pb2.SharedVolumeGetFileRequest,
            modal_proto.api_pb2.SharedVolumeGetFileResponse,
        )
        self.SharedVolumeRemoveFile = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/SharedVolumeRemoveFile',
            modal_proto.api_pb2.SharedVolumeRemoveFileRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.TaskResult = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/TaskResult',
            modal_proto.api_pb2.TaskResultRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.TokenFlowCreate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/TokenFlowCreate',
            modal_proto.api_pb2.TokenFlowCreateRequest,
            modal_proto.api_pb2.TokenFlowCreateResponse,
        )
        self.TokenFlowWait = grpclib.client.UnaryUnaryMethod(
            channel,
            '/modal.client.ModalClient/TokenFlowWait',
            modal_proto.api_pb2.TokenFlowWaitRequest,
            modal_proto.api_pb2.TokenFlowWaitResponse,
        )
