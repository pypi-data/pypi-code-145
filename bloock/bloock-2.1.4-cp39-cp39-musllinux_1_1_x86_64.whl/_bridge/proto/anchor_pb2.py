# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anchor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import shared_pb2 as shared__pb2
from . import config_pb2 as config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0c\x61nchor.proto\x12\x06\x62loock\x1a\x0cshared.proto\x1a\x0c\x63onfig.proto"p\n\x06\x41nchor\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x62lock_roots\x18\x02 \x03(\t\x12\'\n\x08networks\x18\x03 \x03(\x0b\x32\x15.bloock.AnchorNetwork\x12\x0c\n\x04root\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t"=\n\rAnchorNetwork\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0f\n\x07tx_hash\x18\x03 \x01(\t"N\n\x10GetAnchorRequest\x12\'\n\x0b\x63onfig_data\x18\x01 \x01(\x0b\x32\x12.bloock.ConfigData\x12\x11\n\tanchor_id\x18\x02 \x01(\x03"p\n\x11GetAnchorResponse\x12#\n\x06\x61nchor\x18\x01 \x01(\x0b\x32\x0e.bloock.AnchorH\x00\x88\x01\x01\x12!\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.bloock.ErrorH\x01\x88\x01\x01\x42\t\n\x07_anchorB\x08\n\x06_error"`\n\x11WaitAnchorRequest\x12\'\n\x0b\x63onfig_data\x18\x01 \x01(\x0b\x32\x12.bloock.ConfigData\x12\x11\n\tanchor_id\x18\x02 \x01(\x03\x12\x0f\n\x07timeout\x18\x03 \x01(\x03"q\n\x12WaitAnchorResponse\x12#\n\x06\x61nchor\x18\x01 \x01(\x0b\x32\x0e.bloock.AnchorH\x00\x88\x01\x01\x12!\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.bloock.ErrorH\x01\x88\x01\x01\x42\t\n\x07_anchorB\x08\n\x06_error2\x96\x01\n\rAnchorService\x12@\n\tGetAnchor\x12\x18.bloock.GetAnchorRequest\x1a\x19.bloock.GetAnchorResponse\x12\x43\n\nWaitAnchor\x12\x19.bloock.WaitAnchorRequest\x1a\x1a.bloock.WaitAnchorResponseBW\n\x1b\x63om.bloock.sdk.bridge.protoZ8github.com/bloock/bloock-sdk-go/v2/internal/bridge/protob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "anchor_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\033com.bloock.sdk.bridge.protoZ8github.com/bloock/bloock-sdk-go/v2/internal/bridge/proto"
    _ANCHOR._serialized_start = 52
    _ANCHOR._serialized_end = 164
    _ANCHORNETWORK._serialized_start = 166
    _ANCHORNETWORK._serialized_end = 227
    _GETANCHORREQUEST._serialized_start = 229
    _GETANCHORREQUEST._serialized_end = 307
    _GETANCHORRESPONSE._serialized_start = 309
    _GETANCHORRESPONSE._serialized_end = 421
    _WAITANCHORREQUEST._serialized_start = 423
    _WAITANCHORREQUEST._serialized_end = 519
    _WAITANCHORRESPONSE._serialized_start = 521
    _WAITANCHORRESPONSE._serialized_end = 634
    _ANCHORSERVICE._serialized_start = 637
    _ANCHORSERVICE._serialized_end = 787
# @@protoc_insertion_point(module_scope)
