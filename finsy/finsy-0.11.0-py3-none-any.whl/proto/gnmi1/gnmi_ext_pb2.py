# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gnmi1/gnmi_ext.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gnmi1/gnmi_ext.proto\x12\x08gnmi_ext\"\xac\x01\n\tExtension\x12\x37\n\x0eregistered_ext\x18\x01 \x01(\x0b\x32\x1d.gnmi_ext.RegisteredExtensionH\x00\x12\x39\n\x12master_arbitration\x18\x02 \x01(\x0b\x32\x1b.gnmi_ext.MasterArbitrationH\x00\x12$\n\x07history\x18\x03 \x01(\x0b\x32\x11.gnmi_ext.HistoryH\x00\x42\x05\n\x03\x65xt\"E\n\x13RegisteredExtension\x12!\n\x02id\x18\x01 \x01(\x0e\x32\x15.gnmi_ext.ExtensionID\x12\x0b\n\x03msg\x18\x02 \x01(\x0c\"Y\n\x11MasterArbitration\x12\x1c\n\x04role\x18\x01 \x01(\x0b\x32\x0e.gnmi_ext.Role\x12&\n\x0b\x65lection_id\x18\x02 \x01(\x0b\x32\x11.gnmi_ext.Uint128\"$\n\x07Uint128\x12\x0c\n\x04high\x18\x01 \x01(\x04\x12\x0b\n\x03low\x18\x02 \x01(\x04\"\x12\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\t\"S\n\x07History\x12\x17\n\rsnapshot_time\x18\x01 \x01(\x03H\x00\x12$\n\x05range\x18\x02 \x01(\x0b\x32\x13.gnmi_ext.TimeRangeH\x00\x42\t\n\x07request\"\'\n\tTimeRange\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03*3\n\x0b\x45xtensionID\x12\r\n\tEID_UNSET\x10\x00\x12\x15\n\x10\x45ID_EXPERIMENTAL\x10\xe7\x07\x42+Z)github.com/openconfig/gnmi/proto/gnmi_extb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gnmi1.gnmi_ext_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/openconfig/gnmi/proto/gnmi_ext'
  _EXTENSIONID._serialized_start=555
  _EXTENSIONID._serialized_end=606
  _EXTENSION._serialized_start=35
  _EXTENSION._serialized_end=207
  _REGISTEREDEXTENSION._serialized_start=209
  _REGISTEREDEXTENSION._serialized_end=278
  _MASTERARBITRATION._serialized_start=280
  _MASTERARBITRATION._serialized_end=369
  _UINT128._serialized_start=371
  _UINT128._serialized_end=407
  _ROLE._serialized_start=409
  _ROLE._serialized_end=427
  _HISTORY._serialized_start=429
  _HISTORY._serialized_end=512
  _TIMERANGE._serialized_start=514
  _TIMERANGE._serialized_end=553
# @@protoc_insertion_point(module_scope)
