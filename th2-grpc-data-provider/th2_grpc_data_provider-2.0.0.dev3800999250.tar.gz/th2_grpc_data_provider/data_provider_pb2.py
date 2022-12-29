# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: th2_grpc_data_provider/data_provider.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from th2_grpc_common import common_pb2 as th2__grpc__common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*th2_grpc_data_provider/data_provider.proto\x12\x11th2.data_provider\x1a\x1cth2_grpc_common/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xfc\x01\n\x1a\x43radleMessageGroupsRequest\x12\x33\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\rmessage_group\x18\x03 \x03(\x0b\x32\x18.th2.data_provider.Group\x12\x1b\n\x13\x65xternal_user_queue\x18\x04 \x01(\t\x12(\n\x04sort\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x1a\n\nEventScope\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x16\n\x06\x42ookId\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xf7\x01\n\x11MessageStreamInfo\x12\x15\n\rsession_alias\x18\x01 \x01(\t\x12\x1d\n\tdirection\x18\x02 \x01(\x0e\x32\n.Direction\x12\x1a\n\x12number_of_messages\x18\x03 \x01(\x03\x12\x31\n\rmax_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rmin_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cmax_sequence\x18\x06 \x01(\x03\x12\x14\n\x0cmin_sequence\x18\x07 \x01(\x03\"\xba\x01\n\x13MessageIntervalInfo\x12\x33\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\rmessages_info\x18\x03 \x03(\x0b\x32$.th2.data_provider.MessageStreamInfo\"n\n\x1b\x43radleMessageGroupsResponse\x12G\n\x15message_interval_info\x18\x01 \x01(\x0b\x32&.th2.data_provider.MessageIntervalInfoH\x00\x42\x06\n\x04kind\"\x15\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xe2\x02\n\x1aMessageGroupsSearchRequest\x12\x33\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x07\x62ook_id\x18\x07 \x01(\x0b\x32\x19.th2.data_provider.BookId\x12J\n\rmessage_group\x18\x03 \x03(\x0b\x32\x33.th2.data_provider.MessageGroupsSearchRequest.Group\x12(\n\x04sort\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x10\n\x08raw_only\x18\x05 \x01(\x08\x12\x11\n\tkeep_open\x18\x06 \x01(\x08\x1a\x15\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\"C\n\x15MessageStreamsRequest\x12*\n\x07\x62ook_id\x18\x01 \x01(\x0b\x32\x19.th2.data_provider.BookId\"\x17\n\x15MessageFiltersRequest\"\x15\n\x13\x45ventFiltersRequest\"\xe3\x02\n\rEventResponse\x12\x1a\n\x08\x65vent_id\x18\x01 \x01(\x0b\x32\x08.EventID\x12!\n\x0fparent_event_id\x18\x02 \x01(\x0b\x32\x08.EventID\x12\x1a\n\x08\x62\x61tch_id\x18\x03 \x01(\x0b\x32\x08.EventID\x12\x12\n\nis_batched\x18\x04 \x01(\x08\x12\x33\n\x0fstart_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x06status\x18\x07 \x01(\x0e\x32\x0c.EventStatus\x12\x12\n\nevent_name\x18\x08 \x01(\t\x12\x12\n\nevent_type\x18\t \x01(\t\x12\x0c\n\x04\x62ody\x18\n \x01(\x0c\x12\'\n\x13\x61ttached_message_id\x18\x0b \x03(\x0b\x32\n.MessageID\"\xc9\x01\n\rEventMetadata\x12\x1a\n\x08\x65vent_id\x18\x01 \x01(\x0b\x32\x08.EventID\x12!\n\x0fparent_event_id\x18\x02 \x01(\x0b\x32\x08.EventID\x12\x33\n\x0fstart_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x06status\x18\x04 \x01(\x0e\x32\x0c.EventStatus\x12\x12\n\nevent_name\x18\x05 \x01(\t\x12\x12\n\nevent_type\x18\x06 \x01(\t\"(\n\x10\x42ulkEventRequest\x12\x14\n\x02id\x18\x01 \x03(\x0b\x32\x08.EventID\"D\n\x11\x42ulkEventResponse\x12/\n\x05\x65vent\x18\x01 \x03(\x0b\x32 .th2.data_provider.EventResponse\"<\n\x10MessageGroupItem\x12\x19\n\x07message\x18\x01 \x01(\x0b\x32\x08.Message\x12\r\n\x05match\x18\x02 \x01(\x08\"\xfd\x01\n\x14MessageGroupResponse\x12\x1e\n\nmessage_id\x18\x01 \x01(\x0b\x32\n.MessageID\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x08\x62ody_raw\x18\x03 \x01(\x0c\x42\x02\x18\x01\x12 \n\x0braw_message\x18\x06 \x01(\x0b\x32\x0b.RawMessage\x12#\n\x11\x61ttached_event_id\x18\x04 \x03(\x0b\x32\x08.EventID\x12\x39\n\x0cmessage_item\x18\x05 \x03(\x0b\x32#.th2.data_provider.MessageGroupItem\"G\n\x11\x46ilterInfoRequest\x12\x32\n\x0b\x66ilter_name\x18\x01 \x01(\x0b\x32\x1d.th2.data_provider.FilterName\"\x1a\n\nFilterName\x12\x0c\n\x04name\x18\x01 \x01(\t\"I\n\x13\x46ilterNamesResponse\x12\x32\n\x0b\x66ilter_name\x18\x01 \x03(\x0b\x32\x1d.th2.data_provider.FilterName\"\x90\x01\n\x0f\x46ilterParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.th2.data_provider.FilterParameterType\x12+\n\rdefault_value\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04hint\x18\x04 \x01(\t\"\x86\x01\n\x12\x46ilterInfoResponse\x12+\n\x04name\x18\x01 \x01(\x0b\x32\x1d.th2.data_provider.FilterName\x12\x0c\n\x04hint\x18\x02 \x01(\t\x12\x35\n\tparameter\x18\x03 \x03(\x0b\x32\".th2.data_provider.FilterParameter\"`\n\x13MessageMatchRequest\x12\x1e\n\nmessage_id\x18\x01 \x01(\x0b\x32\n.MessageID\x12)\n\x06\x66ilter\x18\x02 \x03(\x0b\x32\x19.th2.data_provider.Filter\"Z\n\x11\x45ventMatchRequest\x12\x1a\n\x08\x65vent_id\x18\x01 \x01(\x0b\x32\x08.EventID\x12)\n\x06\x66ilter\x18\x02 \x03(\x0b\x32\x19.th2.data_provider.Filter\"\x1e\n\rMatchResponse\x12\r\n\x05match\x18\x01 \x01(\x08\"h\n\x06\x46ilter\x12+\n\x04name\x18\x01 \x01(\x0b\x32\x1d.th2.data_provider.FilterName\x12\x10\n\x08negative\x18\x02 \x01(\x08\x12\r\n\x05value\x18\x03 \x03(\t\x12\x10\n\x08\x63onjunct\x18\x04 \x01(\x08\"\x87\x05\n\x12\x45ventSearchRequest\x12\x33\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x0cparent_event\x18\x03 \x01(\x0b\x32\x08.EventID\x12\x39\n\x10search_direction\x18\x04 \x01(\x0e\x32\x1f.th2.data_provider.TimeRelation\x12 \n\x0eresume_from_id\x18\x05 \x01(\x0b\x32\x08.EventID\x12\x37\n\x12result_count_limit\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\tkeep_open\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x10limit_for_parent\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\rmetadata_only\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x11\x61ttached_messages\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12)\n\x06\x66ilter\x18\x0b \x03(\x0b\x32\x19.th2.data_provider.Filter\x12*\n\x07\x62ook_id\x18\x0c \x01(\x0b\x32\x19.th2.data_provider.BookId\x12,\n\x05scope\x18\r \x01(\x0b\x32\x1d.th2.data_provider.EventScope\"\xd3\x01\n\x13\x45ventSearchResponse\x12\x31\n\x05\x65vent\x18\x01 \x01(\x0b\x32 .th2.data_provider.EventResponseH\x00\x12:\n\x0e\x65vent_metadata\x18\x02 \x01(\x0b\x32 .th2.data_provider.EventMetadataH\x00\x12\x45\n\x14\x65vent_stream_pointer\x18\x03 \x01(\x0b\x32%.th2.data_provider.EventStreamPointerH\x00\x42\x06\n\x04\x64\x61ta\"W\n\x12\x45ventStreamPointer\x12\x13\n\x0bhas_started\x18\x01 \x01(\x08\x12\x11\n\thas_ended\x18\x02 \x01(\x08\x12\x19\n\x07last_id\x18\x03 \x01(\x0b\x32\x08.EventID\"\xba\x04\n\x14MessageSearchRequest\x12\x33\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x10search_direction\x18\x03 \x01(\x0e\x32\x1f.th2.data_provider.TimeRelation\x12\x37\n\x12result_count_limit\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x06stream\x18\x05 \x03(\x0b\x32 .th2.data_provider.MessageStream\x12-\n\tkeep_open\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0estream_pointer\x18\x07 \x03(\x0b\x32\'.th2.data_provider.MessageStreamPointer\x12)\n\x06\x66ilter\x18\x08 \x03(\x0b\x32\x19.th2.data_provider.Filter\x12\x33\n\x0f\x61ttached_events\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x18\n\x10response_formats\x18\n \x03(\t\x12*\n\x07\x62ook_id\x18\x0b \x01(\x0b\x32\x19.th2.data_provider.BookId\"\xbb\x01\n\x1bMessageGroupsSearchResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\x31.th2.data_provider.MessageGroupCollectionResponseH\x00\x12K\n\x17message_stream_pointers\x18\x02 \x01(\x0b\x32(.th2.data_provider.MessageStreamPointersH\x00\x42\x06\n\x04\x64\x61ta\"[\n\x1eMessageGroupCollectionResponse\x12\x39\n\x08messages\x18\x01 \x03(\x0b\x32\'.th2.data_provider.MessageGroupResponse\"\xa8\x01\n\x15MessageSearchResponse\x12:\n\x07message\x18\x01 \x01(\x0b\x32\'.th2.data_provider.MessageGroupResponseH\x00\x12K\n\x17message_stream_pointers\x18\x02 \x01(\x0b\x32(.th2.data_provider.MessageStreamPointersH\x00\x42\x06\n\x04\x64\x61ta\"`\n\x15MessageStreamPointers\x12G\n\x16message_stream_pointer\x18\x01 \x03(\x0b\x32\'.th2.data_provider.MessageStreamPointer\"\x95\x01\n\x14MessageStreamPointer\x12\x38\n\x0emessage_stream\x18\x01 \x01(\x0b\x32 .th2.data_provider.MessageStream\x12\x13\n\x0bhas_started\x18\x02 \x01(\x08\x12\x11\n\thas_ended\x18\x03 \x01(\x08\x12\x1b\n\x07last_id\x18\x04 \x01(\x0b\x32\n.MessageID\"<\n\rMessageStream\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\tdirection\x18\x02 \x01(\x0e\x32\n.Direction\"R\n\x16MessageStreamsResponse\x12\x38\n\x0emessage_stream\x18\x01 \x03(\x0b\x32 .th2.data_provider.MessageStream\"\x0e\n\x0c\x42ooksRequest\"<\n\rBooksResponse\x12+\n\x08\x62ook_ids\x18\x01 \x03(\x0b\x32\x19.th2.data_provider.BookId*K\n\x13\x46ilterParameterType\x12\n\n\x06NUMBER\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0f\n\x0bSTRING_LIST\x10\x03*&\n\x0cTimeRelation\x12\x08\n\x04NEXT\x10\x00\x12\x0c\n\x08PREVIOUS\x10\x01\x32\xb0\x0b\n\x0c\x44\x61taProvider\x12\x38\n\x08getEvent\x12\x08.EventID\x1a .th2.data_provider.EventResponse\"\x00\x12X\n\tgetEvents\x12#.th2.data_provider.BulkEventRequest\x1a$.th2.data_provider.BulkEventResponse\"\x00\x12\x43\n\ngetMessage\x12\n.MessageID\x1a\'.th2.data_provider.MessageGroupResponse\"\x00\x12j\n\x11getMessageStreams\x12(.th2.data_provider.MessageStreamsRequest\x1a).th2.data_provider.MessageStreamsResponse\"\x00\x12O\n\x08getBooks\x12\x1f.th2.data_provider.BooksRequest\x1a .th2.data_provider.BooksResponse\"\x00\x12g\n\x0esearchMessages\x12\'.th2.data_provider.MessageSearchRequest\x1a(.th2.data_provider.MessageSearchResponse\"\x00\x30\x01\x12\x61\n\x0csearchEvents\x12%.th2.data_provider.EventSearchRequest\x1a&.th2.data_provider.EventSearchResponse\"\x00\x30\x01\x12z\n\x17loadCradleMessageGroups\x12-.th2.data_provider.CradleMessageGroupsRequest\x1a..th2.data_provider.CradleMessageGroupsResponse\"\x00\x12r\n\x13searchMessageGroups\x12-.th2.data_provider.MessageGroupsSearchRequest\x1a(.th2.data_provider.MessageSearchResponse\"\x00\x30\x01\x12h\n\x12getMessagesFilters\x12(.th2.data_provider.MessageFiltersRequest\x1a&.th2.data_provider.FilterNamesResponse\"\x00\x12\x64\n\x10getEventsFilters\x12&.th2.data_provider.EventFiltersRequest\x1a&.th2.data_provider.FilterNamesResponse\"\x00\x12\x63\n\x12getEventFilterInfo\x12$.th2.data_provider.FilterInfoRequest\x1a%.th2.data_provider.FilterInfoResponse\"\x00\x12\x65\n\x14getMessageFilterInfo\x12$.th2.data_provider.FilterInfoRequest\x1a%.th2.data_provider.FilterInfoResponse\"\x00\x12V\n\nmatchEvent\x12$.th2.data_provider.EventMatchRequest\x1a .th2.data_provider.MatchResponse\"\x00\x12Z\n\x0cmatchMessage\x12&.th2.data_provider.MessageMatchRequest\x1a .th2.data_provider.MatchResponse\"\x00\x42&\n\"com.exactpro.th2.dataprovider.grpcP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'th2_grpc_data_provider.data_provider_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.exactpro.th2.dataprovider.grpcP\001'
  _MESSAGEGROUPRESPONSE.fields_by_name['body_raw']._options = None
  _MESSAGEGROUPRESPONSE.fields_by_name['body_raw']._serialized_options = b'\030\001'
  _FILTERPARAMETERTYPE._serialized_start=5776
  _FILTERPARAMETERTYPE._serialized_end=5851
  _TIMERELATION._serialized_start=5853
  _TIMERELATION._serialized_end=5891
  _CRADLEMESSAGEGROUPSREQUEST._serialized_start=188
  _CRADLEMESSAGEGROUPSREQUEST._serialized_end=440
  _EVENTSCOPE._serialized_start=442
  _EVENTSCOPE._serialized_end=468
  _BOOKID._serialized_start=470
  _BOOKID._serialized_end=492
  _MESSAGESTREAMINFO._serialized_start=495
  _MESSAGESTREAMINFO._serialized_end=742
  _MESSAGEINTERVALINFO._serialized_start=745
  _MESSAGEINTERVALINFO._serialized_end=931
  _CRADLEMESSAGEGROUPSRESPONSE._serialized_start=933
  _CRADLEMESSAGEGROUPSRESPONSE._serialized_end=1043
  _GROUP._serialized_start=1045
  _GROUP._serialized_end=1066
  _MESSAGEGROUPSSEARCHREQUEST._serialized_start=1069
  _MESSAGEGROUPSSEARCHREQUEST._serialized_end=1423
  _MESSAGEGROUPSSEARCHREQUEST_GROUP._serialized_start=1045
  _MESSAGEGROUPSSEARCHREQUEST_GROUP._serialized_end=1066
  _MESSAGESTREAMSREQUEST._serialized_start=1425
  _MESSAGESTREAMSREQUEST._serialized_end=1492
  _MESSAGEFILTERSREQUEST._serialized_start=1494
  _MESSAGEFILTERSREQUEST._serialized_end=1517
  _EVENTFILTERSREQUEST._serialized_start=1519
  _EVENTFILTERSREQUEST._serialized_end=1540
  _EVENTRESPONSE._serialized_start=1543
  _EVENTRESPONSE._serialized_end=1898
  _EVENTMETADATA._serialized_start=1901
  _EVENTMETADATA._serialized_end=2102
  _BULKEVENTREQUEST._serialized_start=2104
  _BULKEVENTREQUEST._serialized_end=2144
  _BULKEVENTRESPONSE._serialized_start=2146
  _BULKEVENTRESPONSE._serialized_end=2214
  _MESSAGEGROUPITEM._serialized_start=2216
  _MESSAGEGROUPITEM._serialized_end=2276
  _MESSAGEGROUPRESPONSE._serialized_start=2279
  _MESSAGEGROUPRESPONSE._serialized_end=2532
  _FILTERINFOREQUEST._serialized_start=2534
  _FILTERINFOREQUEST._serialized_end=2605
  _FILTERNAME._serialized_start=2607
  _FILTERNAME._serialized_end=2633
  _FILTERNAMESRESPONSE._serialized_start=2635
  _FILTERNAMESRESPONSE._serialized_end=2708
  _FILTERPARAMETER._serialized_start=2711
  _FILTERPARAMETER._serialized_end=2855
  _FILTERINFORESPONSE._serialized_start=2858
  _FILTERINFORESPONSE._serialized_end=2992
  _MESSAGEMATCHREQUEST._serialized_start=2994
  _MESSAGEMATCHREQUEST._serialized_end=3090
  _EVENTMATCHREQUEST._serialized_start=3092
  _EVENTMATCHREQUEST._serialized_end=3182
  _MATCHRESPONSE._serialized_start=3184
  _MATCHRESPONSE._serialized_end=3214
  _FILTER._serialized_start=3216
  _FILTER._serialized_end=3320
  _EVENTSEARCHREQUEST._serialized_start=3323
  _EVENTSEARCHREQUEST._serialized_end=3970
  _EVENTSEARCHRESPONSE._serialized_start=3973
  _EVENTSEARCHRESPONSE._serialized_end=4184
  _EVENTSTREAMPOINTER._serialized_start=4186
  _EVENTSTREAMPOINTER._serialized_end=4273
  _MESSAGESEARCHREQUEST._serialized_start=4276
  _MESSAGESEARCHREQUEST._serialized_end=4846
  _MESSAGEGROUPSSEARCHRESPONSE._serialized_start=4849
  _MESSAGEGROUPSSEARCHRESPONSE._serialized_end=5036
  _MESSAGEGROUPCOLLECTIONRESPONSE._serialized_start=5038
  _MESSAGEGROUPCOLLECTIONRESPONSE._serialized_end=5129
  _MESSAGESEARCHRESPONSE._serialized_start=5132
  _MESSAGESEARCHRESPONSE._serialized_end=5300
  _MESSAGESTREAMPOINTERS._serialized_start=5302
  _MESSAGESTREAMPOINTERS._serialized_end=5398
  _MESSAGESTREAMPOINTER._serialized_start=5401
  _MESSAGESTREAMPOINTER._serialized_end=5550
  _MESSAGESTREAM._serialized_start=5552
  _MESSAGESTREAM._serialized_end=5612
  _MESSAGESTREAMSRESPONSE._serialized_start=5614
  _MESSAGESTREAMSRESPONSE._serialized_end=5696
  _BOOKSREQUEST._serialized_start=5698
  _BOOKSREQUEST._serialized_end=5712
  _BOOKSRESPONSE._serialized_start=5714
  _BOOKSRESPONSE._serialized_end=5774
  _DATAPROVIDER._serialized_start=5894
  _DATAPROVIDER._serialized_end=7350
# @@protoc_insertion_point(module_scope)
