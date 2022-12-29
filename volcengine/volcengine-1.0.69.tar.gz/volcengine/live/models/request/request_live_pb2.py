# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: live/request/request_live.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.live.models.business import deny_config_pb2 as live_dot_business_dot_deny__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1flive/request/request_live.proto\x12\x1eVolcengine.Live.Models.Request\x1a\x1flive/business/deny_config.proto\"C\n\x13\x43reateDomainRequest\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\x12\x0c\n\x04Type\x18\x02 \x01(\t\x12\x0e\n\x06Region\x18\x03 \x01(\t\"\xb3\x01\n\x17ListDomainDetailRequest\x12\x0f\n\x07PageNum\x18\x01 \x01(\x03\x12\x10\n\x08PageSize\x18\x02 \x01(\x03\x12\x11\n\tVhostList\x18\x03 \x03(\t\x12\x18\n\x10\x44omainStatusList\x18\x04 \x03(\t\x12\x16\n\x0e\x44omainTypeList\x18\x05 \x03(\t\x12\x18\n\x10\x44omainRegionList\x18\x06 \x03(\t\x12\x16\n\x0e\x44omainNameList\x18\x07 \x03(\t\"&\n\x14\x44isableDomainRequest\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\"%\n\x13\x45nableDomainRequest\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\"%\n\x13\x44\x65leteDomainRequest\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\"+\n\x15\x44\x65scribeDomainRequest\x12\x12\n\nDomainList\x18\x01 \x03(\t\"J\n ManagerPullPushDomainBindRequest\x12\x12\n\nPullDomain\x18\x01 \x01(\t\x12\x12\n\nPushDomain\x18\x02 \x01(\t\"\xa5\x01\n$DescribeRecordTaskFileHistoryRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\x12\x0e\n\x06Stream\x18\x03 \x01(\t\x12\x10\n\x08\x44\x61teFrom\x18\x04 \x01(\t\x12\x0e\n\x06\x44\x61teTo\x18\x05 \x01(\t\x12\x0f\n\x07PageNum\x18\x06 \x01(\x03\x12\x10\n\x08PageSize\x18\x07 \x01(\x03\x12\x0c\n\x04Type\x18\x08 \x01(\t\"\xa2\x01\n!DescribeCDNSnapshotHistoryRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\x12\x0e\n\x06Stream\x18\x03 \x01(\t\x12\x10\n\x08\x44\x61teFrom\x18\x04 \x01(\t\x12\x0e\n\x06\x44\x61teTo\x18\x05 \x01(\t\x12\x0f\n\x07PageNum\x18\x06 \x01(\x03\x12\x10\n\x08PageSize\x18\x07 \x01(\x03\x12\x0c\n\x04Type\x18\x08 \x01(\t\"\xaa\x01\n#DescribeLiveStreamInfoByPageRequest\x12\x0f\n\x07PageNum\x18\x01 \x01(\x03\x12\x10\n\x08PageSize\x18\x02 \x01(\x03\x12\r\n\x05Vhost\x18\x03 \x01(\t\x12\x0e\n\x06\x44omain\x18\x04 \x01(\t\x12\x0b\n\x03\x41pp\x18\x05 \x01(\t\x12\x0e\n\x06Stream\x18\x06 \x01(\t\x12\x12\n\nStreamType\x18\x07 \x01(\t\x12\x10\n\x08InfoType\x18\x08 \x01(\t\"\xbc\x01\n%DescribeClosedStreamInfoByPageRequest\x12\x0f\n\x07PageNum\x18\x01 \x01(\x03\x12\x10\n\x08PageSize\x18\x02 \x01(\x03\x12\r\n\x05Vhost\x18\x03 \x01(\t\x12\x0e\n\x06\x44omain\x18\x04 \x01(\t\x12\x0b\n\x03\x41pp\x18\x05 \x01(\t\x12\x0e\n\x06Stream\x18\x06 \x01(\t\x12\x0c\n\x04Sort\x18\x07 \x01(\t\x12\x13\n\x0b\x45ndTimeFrom\x18\x08 \x01(\t\x12\x11\n\tEndTimeTo\x18\t \x01(\t\"\x87\x01\n(DescribeForbiddenStreamInfoByPageRequest\x12\x0f\n\x07PageNum\x18\x01 \x01(\x03\x12\x10\n\x08PageSize\x18\x02 \x01(\x03\x12\r\n\x05Vhost\x18\x03 \x01(\t\x12\x0b\n\x03\x41pp\x18\x04 \x01(\t\x12\x0e\n\x06Stream\x18\x05 \x01(\t\x12\x0c\n\x04Sort\x18\x06 \x01(\t\"\\\n\x1e\x44\x65scribeLiveStreamStateRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\x12\x0e\n\x06Stream\x18\x04 \x01(\t\"Q\n\x13ResumeStreamRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\x12\x0e\n\x06Stream\x18\x04 \x01(\t\"?\n\x11KillStreamRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\x12\x0e\n\x06Stream\x18\x03 \x01(\t\"b\n\x13\x46orbidStreamRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\x12\x0e\n\x06Stream\x18\x04 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x05 \x01(\t\"6\n\x18\x44\x65leteRelaySourceRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\"+\n\x1a\x44\x65scribeRelaySourceRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\"~\n\x18\x43reateVQScoreTaskRequest\x12\x10\n\x08MainAddr\x18\x01 \x01(\t\x12\x14\n\x0c\x43ontrastAddr\x18\x02 \x01(\t\x12\x15\n\rFrameInterval\x18\x03 \x01(\x03\x12\x10\n\x08\x44uration\x18\x04 \x01(\x03\x12\x11\n\tAlgorithm\x18\x05 \x01(\t\"(\n\x1a\x44\x65scribeVQScoreTaskRequest\x12\n\n\x02ID\x18\x01 \x01(\t\"o\n\x16ListVQScoreTaskRequest\x12\x11\n\tStartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x02 \x01(\t\x12\x0f\n\x07PageNum\x18\x03 \x01(\x03\x12\x10\n\x08PageSize\x18\x04 \x01(\x03\x12\x0e\n\x06Status\x18\x05 \x01(\x03\"\x9e\x01\n\x16GeneratePlayURLRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\x12\x0e\n\x06Stream\x18\x04 \x01(\t\x12\x0e\n\x06Suffix\x18\x05 \x01(\t\x12\x0c\n\x04Type\x18\x06 \x01(\t\x12\x15\n\rValidDuration\x18\x07 \x01(\x03\x12\x13\n\x0b\x45xpiredTime\x18\x08 \x01(\t\"\x80\x01\n\x16GeneratePushURLRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\x12\x0e\n\x06Stream\x18\x04 \x01(\t\x12\x15\n\rValidDuration\x18\x05 \x01(\x03\x12\x13\n\x0b\x45xpiredTime\x18\x06 \x01(\t\"\xba\x01\n\x1b\x43reatePullToPushTaskRequest\x12\r\n\x05Title\x18\x01 \x01(\t\x12\x11\n\tStartTime\x18\x02 \x01(\x03\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\x03\x12\x13\n\x0b\x43\x61llbackURL\x18\x04 \x01(\t\x12\x0c\n\x04Type\x18\x05 \x01(\x05\x12\x11\n\tCycleMode\x18\x06 \x01(\x05\x12\x0f\n\x07\x44stAddr\x18\x07 \x01(\t\x12\x0f\n\x07SrcAddr\x18\x08 \x01(\t\x12\x10\n\x08SrcAddrS\x18\t \x03(\t\"F\n\x19ListPullToPushTaskRequest\x12\x0c\n\x04Page\x18\x01 \x01(\x05\x12\x0c\n\x04Size\x18\x02 \x01(\x05\x12\r\n\x05Title\x18\x03 \x01(\t\"\xca\x01\n\x1bUpdatePullToPushTaskRequest\x12\r\n\x05Title\x18\x01 \x01(\t\x12\x0e\n\x06TaskId\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\x03\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\x03\x12\x13\n\x0b\x43\x61llbackURL\x18\x05 \x01(\t\x12\x0c\n\x04Type\x18\x06 \x01(\x05\x12\x11\n\tCycleMode\x18\x07 \x01(\x05\x12\x0f\n\x07\x44stAddr\x18\x08 \x01(\t\x12\x0f\n\x07SrcAddr\x18\t \x01(\t\x12\x10\n\x08SrcAddrS\x18\n \x03(\t\".\n\x1cRestartPullToPushTaskRequest\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"+\n\x19StopPullToPushTaskRequest\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"-\n\x1b\x44\x65letePullToPushTaskRequest\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"\x90\x01\n\x17UpdateDenyConfigRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\x12I\n\x0e\x44\x65nyConfigList\x18\x04 \x03(\x0b\x32\x31.Volcengine.Live.Models.Business.DenyConfigDetail\"G\n\x19\x44\x65scribeDenyConfigRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\"E\n\x17\x44\x65leteDenyConfigRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0e\n\x06\x44omain\x18\x02 \x01(\t\x12\x0b\n\x03\x41pp\x18\x03 \x01(\t\"\x98\x02\n\x18UpdateRelaySourceRequest\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\x12\x1d\n\x15RelaySourceDomainList\x18\x03 \x03(\t\x12j\n\x11RelaySourceParams\x18\x04 \x03(\x0b\x32O.Volcengine.Live.Models.Request.UpdateRelaySourceRequest.RelaySourceParamsEntry\x12\x1b\n\x13RelaySourceProtocol\x18\x05 \x01(\t\x1a\x38\n\x16RelaySourceParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa6\x01\n\'CreateLiveStreamRecordIndexFilesRequest\x12\x0e\n\x06\x44omain\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\x12\x0e\n\x06Stream\x18\x03 \x01(\t\x12\x11\n\tStartTime\x18\x04 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x05 \x01(\t\x12\x14\n\x0cOutputBucket\x18\x06 \x01(\t\x12\x14\n\x0cOutputObject\x18\x07 \x01(\tB\xcd\x01\n)com.volcengine.service.live.model.requestB\x0bLiveRequestP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/live/models/request\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Live\\Models\\Request\xe2\x02$Volc\\Service\\Live\\Models\\GPBMetadatab\x06proto3')



_CREATEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['CreateDomainRequest']
_LISTDOMAINDETAILREQUEST = DESCRIPTOR.message_types_by_name['ListDomainDetailRequest']
_DISABLEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['DisableDomainRequest']
_ENABLEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['EnableDomainRequest']
_DELETEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['DeleteDomainRequest']
_DESCRIBEDOMAINREQUEST = DESCRIPTOR.message_types_by_name['DescribeDomainRequest']
_MANAGERPULLPUSHDOMAINBINDREQUEST = DESCRIPTOR.message_types_by_name['ManagerPullPushDomainBindRequest']
_DESCRIBERECORDTASKFILEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['DescribeRecordTaskFileHistoryRequest']
_DESCRIBECDNSNAPSHOTHISTORYREQUEST = DESCRIPTOR.message_types_by_name['DescribeCDNSnapshotHistoryRequest']
_DESCRIBELIVESTREAMINFOBYPAGEREQUEST = DESCRIPTOR.message_types_by_name['DescribeLiveStreamInfoByPageRequest']
_DESCRIBECLOSEDSTREAMINFOBYPAGEREQUEST = DESCRIPTOR.message_types_by_name['DescribeClosedStreamInfoByPageRequest']
_DESCRIBEFORBIDDENSTREAMINFOBYPAGEREQUEST = DESCRIPTOR.message_types_by_name['DescribeForbiddenStreamInfoByPageRequest']
_DESCRIBELIVESTREAMSTATEREQUEST = DESCRIPTOR.message_types_by_name['DescribeLiveStreamStateRequest']
_RESUMESTREAMREQUEST = DESCRIPTOR.message_types_by_name['ResumeStreamRequest']
_KILLSTREAMREQUEST = DESCRIPTOR.message_types_by_name['KillStreamRequest']
_FORBIDSTREAMREQUEST = DESCRIPTOR.message_types_by_name['ForbidStreamRequest']
_DELETERELAYSOURCEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRelaySourceRequest']
_DESCRIBERELAYSOURCEREQUEST = DESCRIPTOR.message_types_by_name['DescribeRelaySourceRequest']
_CREATEVQSCORETASKREQUEST = DESCRIPTOR.message_types_by_name['CreateVQScoreTaskRequest']
_DESCRIBEVQSCORETASKREQUEST = DESCRIPTOR.message_types_by_name['DescribeVQScoreTaskRequest']
_LISTVQSCORETASKREQUEST = DESCRIPTOR.message_types_by_name['ListVQScoreTaskRequest']
_GENERATEPLAYURLREQUEST = DESCRIPTOR.message_types_by_name['GeneratePlayURLRequest']
_GENERATEPUSHURLREQUEST = DESCRIPTOR.message_types_by_name['GeneratePushURLRequest']
_CREATEPULLTOPUSHTASKREQUEST = DESCRIPTOR.message_types_by_name['CreatePullToPushTaskRequest']
_LISTPULLTOPUSHTASKREQUEST = DESCRIPTOR.message_types_by_name['ListPullToPushTaskRequest']
_UPDATEPULLTOPUSHTASKREQUEST = DESCRIPTOR.message_types_by_name['UpdatePullToPushTaskRequest']
_RESTARTPULLTOPUSHTASKREQUEST = DESCRIPTOR.message_types_by_name['RestartPullToPushTaskRequest']
_STOPPULLTOPUSHTASKREQUEST = DESCRIPTOR.message_types_by_name['StopPullToPushTaskRequest']
_DELETEPULLTOPUSHTASKREQUEST = DESCRIPTOR.message_types_by_name['DeletePullToPushTaskRequest']
_UPDATEDENYCONFIGREQUEST = DESCRIPTOR.message_types_by_name['UpdateDenyConfigRequest']
_DESCRIBEDENYCONFIGREQUEST = DESCRIPTOR.message_types_by_name['DescribeDenyConfigRequest']
_DELETEDENYCONFIGREQUEST = DESCRIPTOR.message_types_by_name['DeleteDenyConfigRequest']
_UPDATERELAYSOURCEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRelaySourceRequest']
_UPDATERELAYSOURCEREQUEST_RELAYSOURCEPARAMSENTRY = _UPDATERELAYSOURCEREQUEST.nested_types_by_name['RelaySourceParamsEntry']
_CREATELIVESTREAMRECORDINDEXFILESREQUEST = DESCRIPTOR.message_types_by_name['CreateLiveStreamRecordIndexFilesRequest']
CreateDomainRequest = _reflection.GeneratedProtocolMessageType('CreateDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOMAINREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.CreateDomainRequest)
  })
_sym_db.RegisterMessage(CreateDomainRequest)

ListDomainDetailRequest = _reflection.GeneratedProtocolMessageType('ListDomainDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOMAINDETAILREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.ListDomainDetailRequest)
  })
_sym_db.RegisterMessage(ListDomainDetailRequest)

DisableDomainRequest = _reflection.GeneratedProtocolMessageType('DisableDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEDOMAINREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DisableDomainRequest)
  })
_sym_db.RegisterMessage(DisableDomainRequest)

EnableDomainRequest = _reflection.GeneratedProtocolMessageType('EnableDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENABLEDOMAINREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.EnableDomainRequest)
  })
_sym_db.RegisterMessage(EnableDomainRequest)

DeleteDomainRequest = _reflection.GeneratedProtocolMessageType('DeleteDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDOMAINREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DeleteDomainRequest)
  })
_sym_db.RegisterMessage(DeleteDomainRequest)

DescribeDomainRequest = _reflection.GeneratedProtocolMessageType('DescribeDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEDOMAINREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeDomainRequest)
  })
_sym_db.RegisterMessage(DescribeDomainRequest)

ManagerPullPushDomainBindRequest = _reflection.GeneratedProtocolMessageType('ManagerPullPushDomainBindRequest', (_message.Message,), {
  'DESCRIPTOR' : _MANAGERPULLPUSHDOMAINBINDREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.ManagerPullPushDomainBindRequest)
  })
_sym_db.RegisterMessage(ManagerPullPushDomainBindRequest)

DescribeRecordTaskFileHistoryRequest = _reflection.GeneratedProtocolMessageType('DescribeRecordTaskFileHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBERECORDTASKFILEHISTORYREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeRecordTaskFileHistoryRequest)
  })
_sym_db.RegisterMessage(DescribeRecordTaskFileHistoryRequest)

DescribeCDNSnapshotHistoryRequest = _reflection.GeneratedProtocolMessageType('DescribeCDNSnapshotHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBECDNSNAPSHOTHISTORYREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeCDNSnapshotHistoryRequest)
  })
_sym_db.RegisterMessage(DescribeCDNSnapshotHistoryRequest)

DescribeLiveStreamInfoByPageRequest = _reflection.GeneratedProtocolMessageType('DescribeLiveStreamInfoByPageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBELIVESTREAMINFOBYPAGEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeLiveStreamInfoByPageRequest)
  })
_sym_db.RegisterMessage(DescribeLiveStreamInfoByPageRequest)

DescribeClosedStreamInfoByPageRequest = _reflection.GeneratedProtocolMessageType('DescribeClosedStreamInfoByPageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBECLOSEDSTREAMINFOBYPAGEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeClosedStreamInfoByPageRequest)
  })
_sym_db.RegisterMessage(DescribeClosedStreamInfoByPageRequest)

DescribeForbiddenStreamInfoByPageRequest = _reflection.GeneratedProtocolMessageType('DescribeForbiddenStreamInfoByPageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEFORBIDDENSTREAMINFOBYPAGEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeForbiddenStreamInfoByPageRequest)
  })
_sym_db.RegisterMessage(DescribeForbiddenStreamInfoByPageRequest)

DescribeLiveStreamStateRequest = _reflection.GeneratedProtocolMessageType('DescribeLiveStreamStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBELIVESTREAMSTATEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeLiveStreamStateRequest)
  })
_sym_db.RegisterMessage(DescribeLiveStreamStateRequest)

ResumeStreamRequest = _reflection.GeneratedProtocolMessageType('ResumeStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUMESTREAMREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.ResumeStreamRequest)
  })
_sym_db.RegisterMessage(ResumeStreamRequest)

KillStreamRequest = _reflection.GeneratedProtocolMessageType('KillStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _KILLSTREAMREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.KillStreamRequest)
  })
_sym_db.RegisterMessage(KillStreamRequest)

ForbidStreamRequest = _reflection.GeneratedProtocolMessageType('ForbidStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORBIDSTREAMREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.ForbidStreamRequest)
  })
_sym_db.RegisterMessage(ForbidStreamRequest)

DeleteRelaySourceRequest = _reflection.GeneratedProtocolMessageType('DeleteRelaySourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERELAYSOURCEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DeleteRelaySourceRequest)
  })
_sym_db.RegisterMessage(DeleteRelaySourceRequest)

DescribeRelaySourceRequest = _reflection.GeneratedProtocolMessageType('DescribeRelaySourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBERELAYSOURCEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeRelaySourceRequest)
  })
_sym_db.RegisterMessage(DescribeRelaySourceRequest)

CreateVQScoreTaskRequest = _reflection.GeneratedProtocolMessageType('CreateVQScoreTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVQSCORETASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.CreateVQScoreTaskRequest)
  })
_sym_db.RegisterMessage(CreateVQScoreTaskRequest)

DescribeVQScoreTaskRequest = _reflection.GeneratedProtocolMessageType('DescribeVQScoreTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEVQSCORETASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeVQScoreTaskRequest)
  })
_sym_db.RegisterMessage(DescribeVQScoreTaskRequest)

ListVQScoreTaskRequest = _reflection.GeneratedProtocolMessageType('ListVQScoreTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVQSCORETASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.ListVQScoreTaskRequest)
  })
_sym_db.RegisterMessage(ListVQScoreTaskRequest)

GeneratePlayURLRequest = _reflection.GeneratedProtocolMessageType('GeneratePlayURLRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEPLAYURLREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.GeneratePlayURLRequest)
  })
_sym_db.RegisterMessage(GeneratePlayURLRequest)

GeneratePushURLRequest = _reflection.GeneratedProtocolMessageType('GeneratePushURLRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEPUSHURLREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.GeneratePushURLRequest)
  })
_sym_db.RegisterMessage(GeneratePushURLRequest)

CreatePullToPushTaskRequest = _reflection.GeneratedProtocolMessageType('CreatePullToPushTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPULLTOPUSHTASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.CreatePullToPushTaskRequest)
  })
_sym_db.RegisterMessage(CreatePullToPushTaskRequest)

ListPullToPushTaskRequest = _reflection.GeneratedProtocolMessageType('ListPullToPushTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPULLTOPUSHTASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.ListPullToPushTaskRequest)
  })
_sym_db.RegisterMessage(ListPullToPushTaskRequest)

UpdatePullToPushTaskRequest = _reflection.GeneratedProtocolMessageType('UpdatePullToPushTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPULLTOPUSHTASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.UpdatePullToPushTaskRequest)
  })
_sym_db.RegisterMessage(UpdatePullToPushTaskRequest)

RestartPullToPushTaskRequest = _reflection.GeneratedProtocolMessageType('RestartPullToPushTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESTARTPULLTOPUSHTASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.RestartPullToPushTaskRequest)
  })
_sym_db.RegisterMessage(RestartPullToPushTaskRequest)

StopPullToPushTaskRequest = _reflection.GeneratedProtocolMessageType('StopPullToPushTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPPULLTOPUSHTASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.StopPullToPushTaskRequest)
  })
_sym_db.RegisterMessage(StopPullToPushTaskRequest)

DeletePullToPushTaskRequest = _reflection.GeneratedProtocolMessageType('DeletePullToPushTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPULLTOPUSHTASKREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DeletePullToPushTaskRequest)
  })
_sym_db.RegisterMessage(DeletePullToPushTaskRequest)

UpdateDenyConfigRequest = _reflection.GeneratedProtocolMessageType('UpdateDenyConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDENYCONFIGREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.UpdateDenyConfigRequest)
  })
_sym_db.RegisterMessage(UpdateDenyConfigRequest)

DescribeDenyConfigRequest = _reflection.GeneratedProtocolMessageType('DescribeDenyConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEDENYCONFIGREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DescribeDenyConfigRequest)
  })
_sym_db.RegisterMessage(DescribeDenyConfigRequest)

DeleteDenyConfigRequest = _reflection.GeneratedProtocolMessageType('DeleteDenyConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDENYCONFIGREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.DeleteDenyConfigRequest)
  })
_sym_db.RegisterMessage(DeleteDenyConfigRequest)

UpdateRelaySourceRequest = _reflection.GeneratedProtocolMessageType('UpdateRelaySourceRequest', (_message.Message,), {

  'RelaySourceParamsEntry' : _reflection.GeneratedProtocolMessageType('RelaySourceParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATERELAYSOURCEREQUEST_RELAYSOURCEPARAMSENTRY,
    '__module__' : 'live.request.request_live_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.UpdateRelaySourceRequest.RelaySourceParamsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATERELAYSOURCEREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.UpdateRelaySourceRequest)
  })
_sym_db.RegisterMessage(UpdateRelaySourceRequest)
_sym_db.RegisterMessage(UpdateRelaySourceRequest.RelaySourceParamsEntry)

CreateLiveStreamRecordIndexFilesRequest = _reflection.GeneratedProtocolMessageType('CreateLiveStreamRecordIndexFilesRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELIVESTREAMRECORDINDEXFILESREQUEST,
  '__module__' : 'live.request.request_live_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Request.CreateLiveStreamRecordIndexFilesRequest)
  })
_sym_db.RegisterMessage(CreateLiveStreamRecordIndexFilesRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.live.model.requestB\013LiveRequestP\001ZAgithub.com/volcengine/volc-sdk-golang/service/live/models/request\240\001\001\330\001\001\312\002 Volc\\Service\\Live\\Models\\Request\342\002$Volc\\Service\\Live\\Models\\GPBMetadata'
  _UPDATERELAYSOURCEREQUEST_RELAYSOURCEPARAMSENTRY._options = None
  _UPDATERELAYSOURCEREQUEST_RELAYSOURCEPARAMSENTRY._serialized_options = b'8\001'
  _CREATEDOMAINREQUEST._serialized_start=100
  _CREATEDOMAINREQUEST._serialized_end=167
  _LISTDOMAINDETAILREQUEST._serialized_start=170
  _LISTDOMAINDETAILREQUEST._serialized_end=349
  _DISABLEDOMAINREQUEST._serialized_start=351
  _DISABLEDOMAINREQUEST._serialized_end=389
  _ENABLEDOMAINREQUEST._serialized_start=391
  _ENABLEDOMAINREQUEST._serialized_end=428
  _DELETEDOMAINREQUEST._serialized_start=430
  _DELETEDOMAINREQUEST._serialized_end=467
  _DESCRIBEDOMAINREQUEST._serialized_start=469
  _DESCRIBEDOMAINREQUEST._serialized_end=512
  _MANAGERPULLPUSHDOMAINBINDREQUEST._serialized_start=514
  _MANAGERPULLPUSHDOMAINBINDREQUEST._serialized_end=588
  _DESCRIBERECORDTASKFILEHISTORYREQUEST._serialized_start=591
  _DESCRIBERECORDTASKFILEHISTORYREQUEST._serialized_end=756
  _DESCRIBECDNSNAPSHOTHISTORYREQUEST._serialized_start=759
  _DESCRIBECDNSNAPSHOTHISTORYREQUEST._serialized_end=921
  _DESCRIBELIVESTREAMINFOBYPAGEREQUEST._serialized_start=924
  _DESCRIBELIVESTREAMINFOBYPAGEREQUEST._serialized_end=1094
  _DESCRIBECLOSEDSTREAMINFOBYPAGEREQUEST._serialized_start=1097
  _DESCRIBECLOSEDSTREAMINFOBYPAGEREQUEST._serialized_end=1285
  _DESCRIBEFORBIDDENSTREAMINFOBYPAGEREQUEST._serialized_start=1288
  _DESCRIBEFORBIDDENSTREAMINFOBYPAGEREQUEST._serialized_end=1423
  _DESCRIBELIVESTREAMSTATEREQUEST._serialized_start=1425
  _DESCRIBELIVESTREAMSTATEREQUEST._serialized_end=1517
  _RESUMESTREAMREQUEST._serialized_start=1519
  _RESUMESTREAMREQUEST._serialized_end=1600
  _KILLSTREAMREQUEST._serialized_start=1602
  _KILLSTREAMREQUEST._serialized_end=1665
  _FORBIDSTREAMREQUEST._serialized_start=1667
  _FORBIDSTREAMREQUEST._serialized_end=1765
  _DELETERELAYSOURCEREQUEST._serialized_start=1767
  _DELETERELAYSOURCEREQUEST._serialized_end=1821
  _DESCRIBERELAYSOURCEREQUEST._serialized_start=1823
  _DESCRIBERELAYSOURCEREQUEST._serialized_end=1866
  _CREATEVQSCORETASKREQUEST._serialized_start=1868
  _CREATEVQSCORETASKREQUEST._serialized_end=1994
  _DESCRIBEVQSCORETASKREQUEST._serialized_start=1996
  _DESCRIBEVQSCORETASKREQUEST._serialized_end=2036
  _LISTVQSCORETASKREQUEST._serialized_start=2038
  _LISTVQSCORETASKREQUEST._serialized_end=2149
  _GENERATEPLAYURLREQUEST._serialized_start=2152
  _GENERATEPLAYURLREQUEST._serialized_end=2310
  _GENERATEPUSHURLREQUEST._serialized_start=2313
  _GENERATEPUSHURLREQUEST._serialized_end=2441
  _CREATEPULLTOPUSHTASKREQUEST._serialized_start=2444
  _CREATEPULLTOPUSHTASKREQUEST._serialized_end=2630
  _LISTPULLTOPUSHTASKREQUEST._serialized_start=2632
  _LISTPULLTOPUSHTASKREQUEST._serialized_end=2702
  _UPDATEPULLTOPUSHTASKREQUEST._serialized_start=2705
  _UPDATEPULLTOPUSHTASKREQUEST._serialized_end=2907
  _RESTARTPULLTOPUSHTASKREQUEST._serialized_start=2909
  _RESTARTPULLTOPUSHTASKREQUEST._serialized_end=2955
  _STOPPULLTOPUSHTASKREQUEST._serialized_start=2957
  _STOPPULLTOPUSHTASKREQUEST._serialized_end=3000
  _DELETEPULLTOPUSHTASKREQUEST._serialized_start=3002
  _DELETEPULLTOPUSHTASKREQUEST._serialized_end=3047
  _UPDATEDENYCONFIGREQUEST._serialized_start=3050
  _UPDATEDENYCONFIGREQUEST._serialized_end=3194
  _DESCRIBEDENYCONFIGREQUEST._serialized_start=3196
  _DESCRIBEDENYCONFIGREQUEST._serialized_end=3267
  _DELETEDENYCONFIGREQUEST._serialized_start=3269
  _DELETEDENYCONFIGREQUEST._serialized_end=3338
  _UPDATERELAYSOURCEREQUEST._serialized_start=3341
  _UPDATERELAYSOURCEREQUEST._serialized_end=3621
  _UPDATERELAYSOURCEREQUEST_RELAYSOURCEPARAMSENTRY._serialized_start=3565
  _UPDATERELAYSOURCEREQUEST_RELAYSOURCEPARAMSENTRY._serialized_end=3621
  _CREATELIVESTREAMRECORDINDEXFILESREQUEST._serialized_start=3624
  _CREATELIVESTREAMRECORDINDEXFILESREQUEST._serialized_end=3790
# @@protoc_insertion_point(module_scope)
