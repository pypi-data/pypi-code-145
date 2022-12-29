# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fsai_grpc_api/protos/mission_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from fsai_grpc_api.protos import utils_pb2 as fsai__grpc__api_dot_protos_dot_utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fsai_grpc_api/protos/mission_api.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&fsai_grpc_api/protos/mission_api.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a fsai_grpc_api/protos/utils.proto\"\x98\x01\n\x07Mission\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"1\n\x14\x43reateMissionRequest\x12\x19\n\x07mission\x18\x01 \x01(\x0b\x32\x08.Mission\"T\n\x15\x43reateMissionResponse\x12 \n\x0b\x63hange_type\x18\x01 \x01(\x0e\x32\x0b.ChangeType\x12\x19\n\x07mission\x18\x02 \x01(\x0b\x32\x08.Mission\"0\n\x13ListMissionsRequest\x12\x19\n\x07mission\x18\x01 \x01(\x0b\x32\x08.Mission\"T\n\x14ListMissionsResponse\x12 \n\x0b\x63hange_type\x18\x01 \x01(\x0e\x32\x0b.ChangeType\x12\x1a\n\x08missions\x18\x02 \x03(\x0b\x32\x08.Mission\"2\n\x15GetMissionByIdRequest\x12\x19\n\x07mission\x18\x01 \x01(\x0b\x32\x08.Mission\"U\n\x16GetMissionByIdResponse\x12 \n\x0b\x63hange_type\x18\x01 \x01(\x0e\x32\x0b.ChangeType\x12\x19\n\x07mission\x18\x02 \x01(\x0b\x32\x08.Mission2\xcc\x01\n\nMissionApi\x12>\n\rCreateMission\x12\x15.CreateMissionRequest\x1a\x16.CreateMissionResponse\x12;\n\x0cListMissions\x12\x14.ListMissionsRequest\x1a\x15.ListMissionsResponse\x12\x41\n\x0eGetMissionById\x12\x16.GetMissionByIdRequest\x1a\x17.GetMissionByIdResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,fsai__grpc__api_dot_protos_dot_utils__pb2.DESCRIPTOR,])




_MISSION = _descriptor.Descriptor(
  name='Mission',
  full_name='Mission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Mission.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Mission.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='Mission.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='Mission.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='Mission.updated_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=262,
)


_CREATEMISSIONREQUEST = _descriptor.Descriptor(
  name='CreateMissionRequest',
  full_name='CreateMissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mission', full_name='CreateMissionRequest.mission', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=313,
)


_CREATEMISSIONRESPONSE = _descriptor.Descriptor(
  name='CreateMissionResponse',
  full_name='CreateMissionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='CreateMissionResponse.change_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mission', full_name='CreateMissionResponse.mission', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=399,
)


_LISTMISSIONSREQUEST = _descriptor.Descriptor(
  name='ListMissionsRequest',
  full_name='ListMissionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mission', full_name='ListMissionsRequest.mission', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=449,
)


_LISTMISSIONSRESPONSE = _descriptor.Descriptor(
  name='ListMissionsResponse',
  full_name='ListMissionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='ListMissionsResponse.change_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missions', full_name='ListMissionsResponse.missions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=535,
)


_GETMISSIONBYIDREQUEST = _descriptor.Descriptor(
  name='GetMissionByIdRequest',
  full_name='GetMissionByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mission', full_name='GetMissionByIdRequest.mission', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=537,
  serialized_end=587,
)


_GETMISSIONBYIDRESPONSE = _descriptor.Descriptor(
  name='GetMissionByIdResponse',
  full_name='GetMissionByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='GetMissionByIdResponse.change_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mission', full_name='GetMissionByIdResponse.mission', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=674,
)

_MISSION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MISSION.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEMISSIONREQUEST.fields_by_name['mission'].message_type = _MISSION
_CREATEMISSIONRESPONSE.fields_by_name['change_type'].enum_type = fsai__grpc__api_dot_protos_dot_utils__pb2._CHANGETYPE
_CREATEMISSIONRESPONSE.fields_by_name['mission'].message_type = _MISSION
_LISTMISSIONSREQUEST.fields_by_name['mission'].message_type = _MISSION
_LISTMISSIONSRESPONSE.fields_by_name['change_type'].enum_type = fsai__grpc__api_dot_protos_dot_utils__pb2._CHANGETYPE
_LISTMISSIONSRESPONSE.fields_by_name['missions'].message_type = _MISSION
_GETMISSIONBYIDREQUEST.fields_by_name['mission'].message_type = _MISSION
_GETMISSIONBYIDRESPONSE.fields_by_name['change_type'].enum_type = fsai__grpc__api_dot_protos_dot_utils__pb2._CHANGETYPE
_GETMISSIONBYIDRESPONSE.fields_by_name['mission'].message_type = _MISSION
DESCRIPTOR.message_types_by_name['Mission'] = _MISSION
DESCRIPTOR.message_types_by_name['CreateMissionRequest'] = _CREATEMISSIONREQUEST
DESCRIPTOR.message_types_by_name['CreateMissionResponse'] = _CREATEMISSIONRESPONSE
DESCRIPTOR.message_types_by_name['ListMissionsRequest'] = _LISTMISSIONSREQUEST
DESCRIPTOR.message_types_by_name['ListMissionsResponse'] = _LISTMISSIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetMissionByIdRequest'] = _GETMISSIONBYIDREQUEST
DESCRIPTOR.message_types_by_name['GetMissionByIdResponse'] = _GETMISSIONBYIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mission = _reflection.GeneratedProtocolMessageType('Mission', (_message.Message,), {
  'DESCRIPTOR' : _MISSION,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:Mission)
  })
_sym_db.RegisterMessage(Mission)

CreateMissionRequest = _reflection.GeneratedProtocolMessageType('CreateMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMISSIONREQUEST,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:CreateMissionRequest)
  })
_sym_db.RegisterMessage(CreateMissionRequest)

CreateMissionResponse = _reflection.GeneratedProtocolMessageType('CreateMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMISSIONRESPONSE,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:CreateMissionResponse)
  })
_sym_db.RegisterMessage(CreateMissionResponse)

ListMissionsRequest = _reflection.GeneratedProtocolMessageType('ListMissionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMISSIONSREQUEST,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:ListMissionsRequest)
  })
_sym_db.RegisterMessage(ListMissionsRequest)

ListMissionsResponse = _reflection.GeneratedProtocolMessageType('ListMissionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMISSIONSRESPONSE,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:ListMissionsResponse)
  })
_sym_db.RegisterMessage(ListMissionsResponse)

GetMissionByIdRequest = _reflection.GeneratedProtocolMessageType('GetMissionByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMISSIONBYIDREQUEST,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:GetMissionByIdRequest)
  })
_sym_db.RegisterMessage(GetMissionByIdRequest)

GetMissionByIdResponse = _reflection.GeneratedProtocolMessageType('GetMissionByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMISSIONBYIDRESPONSE,
  '__module__' : 'fsai_grpc_api.protos.mission_api_pb2'
  # @@protoc_insertion_point(class_scope:GetMissionByIdResponse)
  })
_sym_db.RegisterMessage(GetMissionByIdResponse)



_MISSIONAPI = _descriptor.ServiceDescriptor(
  name='MissionApi',
  full_name='MissionApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=677,
  serialized_end=881,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateMission',
    full_name='MissionApi.CreateMission',
    index=0,
    containing_service=None,
    input_type=_CREATEMISSIONREQUEST,
    output_type=_CREATEMISSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListMissions',
    full_name='MissionApi.ListMissions',
    index=1,
    containing_service=None,
    input_type=_LISTMISSIONSREQUEST,
    output_type=_LISTMISSIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMissionById',
    full_name='MissionApi.GetMissionById',
    index=2,
    containing_service=None,
    input_type=_GETMISSIONBYIDREQUEST,
    output_type=_GETMISSIONBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MISSIONAPI)

DESCRIPTOR.services_by_name['MissionApi'] = _MISSIONAPI

# @@protoc_insertion_point(module_scope)
