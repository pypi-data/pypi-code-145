# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: live/business/relay_source.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n live/business/relay_source.proto\x12\x1fVolcengine.Live.Models.Business\"\xf9\x01\n\x16RelaySourceGroupItemV2\x12\x1d\n\x15RelaySourceDomainList\x18\x01 \x03(\t\x12i\n\x11RelaySourceParams\x18\x02 \x03(\x0b\x32N.Volcengine.Live.Models.Business.RelaySourceGroupItemV2.RelaySourceParamsEntry\x12\x1b\n\x13RelaySourceProtocol\x18\x03 \x01(\t\x1a\x38\n\x16RelaySourceParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"{\n\x11RelaySourceConfig\x12\r\n\x05Vhost\x18\x01 \x01(\t\x12\x0b\n\x03\x41pp\x18\x02 \x01(\t\x12J\n\tGroupList\x18\x03 \x03(\x0b\x32\x37.Volcengine.Live.Models.Business.RelaySourceGroupItemV2\"f\n\x15RelaySourceConfigList\x12M\n\x11RelaySourceConfig\x18\x01 \x03(\x0b\x32\x32.Volcengine.Live.Models.Business.RelaySourceConfigB\xd3\x01\n*com.volcengine.service.live.model.businessB\x0bRelaySourceP\x01ZBgithub.com/volcengine/volc-sdk-golang/service/live/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02!Volc\\Service\\Live\\Models\\Business\xe2\x02$Volc\\Service\\Live\\Models\\GPBMetadatab\x06proto3')



_RELAYSOURCEGROUPITEMV2 = DESCRIPTOR.message_types_by_name['RelaySourceGroupItemV2']
_RELAYSOURCEGROUPITEMV2_RELAYSOURCEPARAMSENTRY = _RELAYSOURCEGROUPITEMV2.nested_types_by_name['RelaySourceParamsEntry']
_RELAYSOURCECONFIG = DESCRIPTOR.message_types_by_name['RelaySourceConfig']
_RELAYSOURCECONFIGLIST = DESCRIPTOR.message_types_by_name['RelaySourceConfigList']
RelaySourceGroupItemV2 = _reflection.GeneratedProtocolMessageType('RelaySourceGroupItemV2', (_message.Message,), {

  'RelaySourceParamsEntry' : _reflection.GeneratedProtocolMessageType('RelaySourceParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RELAYSOURCEGROUPITEMV2_RELAYSOURCEPARAMSENTRY,
    '__module__' : 'live.business.relay_source_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.RelaySourceGroupItemV2.RelaySourceParamsEntry)
    })
  ,
  'DESCRIPTOR' : _RELAYSOURCEGROUPITEMV2,
  '__module__' : 'live.business.relay_source_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.RelaySourceGroupItemV2)
  })
_sym_db.RegisterMessage(RelaySourceGroupItemV2)
_sym_db.RegisterMessage(RelaySourceGroupItemV2.RelaySourceParamsEntry)

RelaySourceConfig = _reflection.GeneratedProtocolMessageType('RelaySourceConfig', (_message.Message,), {
  'DESCRIPTOR' : _RELAYSOURCECONFIG,
  '__module__' : 'live.business.relay_source_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.RelaySourceConfig)
  })
_sym_db.RegisterMessage(RelaySourceConfig)

RelaySourceConfigList = _reflection.GeneratedProtocolMessageType('RelaySourceConfigList', (_message.Message,), {
  'DESCRIPTOR' : _RELAYSOURCECONFIGLIST,
  '__module__' : 'live.business.relay_source_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.RelaySourceConfigList)
  })
_sym_db.RegisterMessage(RelaySourceConfigList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.volcengine.service.live.model.businessB\013RelaySourceP\001ZBgithub.com/volcengine/volc-sdk-golang/service/live/models/business\240\001\001\330\001\001\302\002\000\312\002!Volc\\Service\\Live\\Models\\Business\342\002$Volc\\Service\\Live\\Models\\GPBMetadata'
  _RELAYSOURCEGROUPITEMV2_RELAYSOURCEPARAMSENTRY._options = None
  _RELAYSOURCEGROUPITEMV2_RELAYSOURCEPARAMSENTRY._serialized_options = b'8\001'
  _RELAYSOURCEGROUPITEMV2._serialized_start=70
  _RELAYSOURCEGROUPITEMV2._serialized_end=319
  _RELAYSOURCEGROUPITEMV2_RELAYSOURCEPARAMSENTRY._serialized_start=263
  _RELAYSOURCEGROUPITEMV2_RELAYSOURCEPARAMSENTRY._serialized_end=319
  _RELAYSOURCECONFIG._serialized_start=321
  _RELAYSOURCECONFIG._serialized_end=444
  _RELAYSOURCECONFIGLIST._serialized_start=446
  _RELAYSOURCECONFIGLIST._serialized_end=548
# @@protoc_insertion_point(module_scope)
