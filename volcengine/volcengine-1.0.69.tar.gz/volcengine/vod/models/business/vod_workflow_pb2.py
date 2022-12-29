# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_workflow.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fvod/business/vod_workflow.proto\x12\x1eVolcengine.Vod.Models.Business\x1a\x1fgoogle/protobuf/timestamp.proto\"\'\n\x16VodStartWorkflowResult\x12\r\n\x05RunId\x18\x01 \x01(\t\"\xdc\x01\n\x0eWorkflowParams\x12\x46\n\x0eOverrideParams\x18\x01 \x01(\x0b\x32..Volcengine.Vod.Models.Business.OverrideParams\x12P\n\tCondition\x18\x02 \x03(\x0b\x32=.Volcengine.Vod.Models.Business.WorkflowParams.ConditionEntry\x1a\x30\n\x0e\x43onditionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xb0\x02\n\x0eOverrideParams\x12:\n\x04Logo\x18\x01 \x03(\x0b\x32,.Volcengine.Vod.Models.Business.LogoOverride\x12N\n\x0eTranscodeVideo\x18\x02 \x03(\x0b\x32\x36.Volcengine.Vod.Models.Business.TranscodeVideoOverride\x12N\n\x0eTranscodeAudio\x18\x03 \x03(\x0b\x32\x36.Volcengine.Vod.Models.Business.TranscodeAudioOverride\x12\x42\n\x08Snapshot\x18\x04 \x03(\x0b\x32\x30.Volcengine.Vod.Models.Business.SnapshotOverride\"\x95\x01\n\x0cLogoOverride\x12\x12\n\nTemplateId\x18\x01 \x01(\t\x12\x44\n\x04Vars\x18\x02 \x03(\x0b\x32\x36.Volcengine.Vod.Models.Business.LogoOverride.VarsEntry\x1a+\n\tVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x16TranscodeVideoOverride\x12\x12\n\nTemplateId\x18\x01 \x03(\t\x12\x32\n\x04\x43lip\x18\x02 \x01(\x0b\x32$.Volcengine.Vod.Models.Business.Clip\x12\x13\n\x0bOutputIndex\x18\x03 \x03(\x05\x12\x10\n\x08\x46ileName\x18\x04 \x01(\t\"*\n\x04\x43lip\x12\x11\n\tStartTime\x18\x01 \x01(\x05\x12\x0f\n\x07\x45ndTime\x18\x02 \x01(\x05\"r\n\x16TranscodeAudioOverride\x12\x12\n\nTemplateId\x18\x01 \x03(\t\x12\x32\n\x04\x43lip\x18\x02 \x01(\x0b\x32$.Volcengine.Vod.Models.Business.Clip\x12\x10\n\x08\x46ileName\x18\x03 \x01(\t\"R\n\x10SnapshotOverride\x12\x12\n\nTemplateId\x18\x01 \x03(\t\x12\x12\n\nOffsetTime\x18\x02 \x01(\x05\x12\x16\n\x0eOffsetTimeList\x18\x03 \x03(\x05\"\xa5\x01\n\x0fTranscodeResult\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12>\n\nInspection\x18\x02 \x01(\x0b\x32*.Volcengine.Vod.Models.Business.Inspection\x12\x45\n\x0c\x43\x61tegoryTags\x18\x03 \x03(\x0b\x32/.Volcengine.Vod.Models.Business.CategoryTagInfo\"\x82\x01\n\nInspection\x12\x38\n\x07Quality\x18\x01 \x01(\x0b\x32\'.Volcengine.Vod.Models.Business.Quality\x12:\n\x06\x44\x65Logo\x18\x02 \x03(\x0b\x32*.Volcengine.Vod.Models.Business.DeLogoInfo\"\x88\x01\n\x07Quality\x12=\n\x06Visual\x18\x01 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VisualQuality\x12>\n\nVolumeInfo\x18\x02 \x01(\x0b\x32*.Volcengine.Vod.Models.Business.VolumeInfo\"q\n\nDeLogoInfo\x12\x13\n\x0b\x41nchorWidth\x18\x01 \x01(\x03\x12\x14\n\x0c\x41nchorHeight\x18\x02 \x01(\x03\x12\x0c\n\x04PosX\x18\x03 \x01(\x03\x12\x0c\n\x04PosY\x18\x04 \x01(\x03\x12\r\n\x05SizeX\x18\x05 \x01(\x03\x12\r\n\x05SizeY\x18\x06 \x01(\x03\"|\n\rVisualQuality\x12\x0f\n\x07VQScore\x18\x01 \x01(\x01\x12\x10\n\x08\x43ontrast\x18\x02 \x01(\x01\x12\x14\n\x0c\x43olorfulness\x18\x03 \x01(\x01\x12\x12\n\nBrightness\x18\x04 \x01(\x01\x12\x0f\n\x07Texture\x18\x05 \x01(\x01\x12\r\n\x05Noise\x18\x06 \x01(\x01\"S\n\nVolumeInfo\x12\x10\n\x08Loudness\x18\x01 \x01(\x01\x12\x0c\n\x04Peak\x18\x02 \x01(\x01\x12\x12\n\nMeanVolume\x18\x03 \x01(\x01\x12\x11\n\tMaxVolume\x18\x04 \x01(\x01\"\xd6\x01\n\x0f\x43\x61tegoryTagInfo\x12\r\n\x05TagId\x18\x01 \x01(\x03\x12\x0c\n\x04Prob\x18\x02 \x01(\x01\x12\x0f\n\x07TagName\x18\x03 \x01(\t\x12\r\n\x05Level\x18\x04 \x01(\x03\x12S\n\nParentInfo\x18\x05 \x03(\x0b\x32?.Volcengine.Vod.Models.Business.CategoryTagInfo.ParentInfoEntry\x1a\x31\n\x0fParentInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x97\x01\n\x1eVodListWorkflowExecutionResult\x12?\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.WorkflowExecution\x12\x12\n\nTotalCount\x18\x02 \x01(\x05\x12\x10\n\x08PageSize\x18\x03 \x01(\x05\x12\x0e\n\x06Offset\x18\x04 \x01(\x05\"\xb1\x03\n\x11WorkflowExecution\x12\r\n\x05RunId\x18\x01 \x01(\t\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x12\n\nTemplateId\x18\x03 \x01(\t\x12\x14\n\x0cTemplateName\x18\x04 \x01(\t\x12\x11\n\tSpaceName\x18\x05 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\t\x12\x12\n\nTaskListId\x18\x07 \x01(\t\x12\x19\n\x11\x45nableLowPriority\x18\x08 \x01(\x08\x12\x11\n\tJobSource\x18\t \x01(\t\x12.\n\nCreateTime\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tStartTime\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x45ndTime\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12=\n\x05Input\x18\r \x01(\x0b\x32..Volcengine.Vod.Models.Business.WorkflowParams\x12\x10\n\x08Priority\x18\x0e \x01(\x05\x12\x14\n\x0c\x43\x61llbackArgs\x18\x0f \x01(\t\"\x86\x03\n#VodGetWorkflowExecutionDetailResult\x12\r\n\x05RunId\x18\x01 \x01(\t\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x12\n\nTemplateId\x18\x03 \x01(\t\x12\x11\n\tSpaceName\x18\x04 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\t\x12\x12\n\nTaskListId\x18\x07 \x01(\t\x12\x19\n\x11\x45nableLowPriority\x18\x08 \x01(\x08\x12\x11\n\tJobSource\x18\t \x01(\t\x12>\n\x06Stages\x18\n \x03(\x0b\x32..Volcengine.Vod.Models.Business.ExecutionStage\x12.\n\nCreateTime\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tStartTime\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x45ndTime\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc3\x01\n\x0e\x45xecutionStage\x12\x13\n\x0b\x44isplayName\x18\x01 \x01(\t\x12@\n\x0bStageDetail\x18\x02 \x03(\x0b\x32+.Volcengine.Vod.Models.Business.StageDetail\x12-\n\tStartTime\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x45ndTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8d\x02\n\x0bStageDetail\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x13\n\x0b\x44isplayName\x18\x02 \x01(\t\x12\x0c\n\x04Type\x18\x03 \x01(\t\x12\x12\n\nTemplateId\x18\x04 \x01(\t\x12;\n\x06Status\x18\x05 \x01(\x0e\x32+.Volcengine.Vod.Models.Business.StageStatus\x12\x11\n\tErrorCode\x18\x06 \x01(\x03\x12\x0f\n\x07Message\x18\x07 \x01(\t\x12-\n\tStartTime\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x45ndTime\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp*z\n\x0bStageStatus\x12\x0b\n\x07Unknown\x10\x00\x12\r\n\tScheduled\x10\x01\x12\x0b\n\x07Running\x10\x02\x12\x0c\n\x08\x43\x61nceled\x10\x03\x12\x0c\n\x08TimedOut\x10\x04\x12\x0b\n\x07Skipped\x10\x05\x12\r\n\tCompleted\x10\x06\x12\n\n\x06\x46\x61iled\x10\x07\x42\xcc\x01\n)com.volcengine.service.vod.model.businessB\x0bVodWorkflowP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')

_STAGESTATUS = DESCRIPTOR.enum_types_by_name['StageStatus']
StageStatus = enum_type_wrapper.EnumTypeWrapper(_STAGESTATUS)
Unknown = 0
Scheduled = 1
Running = 2
Canceled = 3
TimedOut = 4
Skipped = 5
Completed = 6
Failed = 7


_VODSTARTWORKFLOWRESULT = DESCRIPTOR.message_types_by_name['VodStartWorkflowResult']
_WORKFLOWPARAMS = DESCRIPTOR.message_types_by_name['WorkflowParams']
_WORKFLOWPARAMS_CONDITIONENTRY = _WORKFLOWPARAMS.nested_types_by_name['ConditionEntry']
_OVERRIDEPARAMS = DESCRIPTOR.message_types_by_name['OverrideParams']
_LOGOOVERRIDE = DESCRIPTOR.message_types_by_name['LogoOverride']
_LOGOOVERRIDE_VARSENTRY = _LOGOOVERRIDE.nested_types_by_name['VarsEntry']
_TRANSCODEVIDEOOVERRIDE = DESCRIPTOR.message_types_by_name['TranscodeVideoOverride']
_CLIP = DESCRIPTOR.message_types_by_name['Clip']
_TRANSCODEAUDIOOVERRIDE = DESCRIPTOR.message_types_by_name['TranscodeAudioOverride']
_SNAPSHOTOVERRIDE = DESCRIPTOR.message_types_by_name['SnapshotOverride']
_TRANSCODERESULT = DESCRIPTOR.message_types_by_name['TranscodeResult']
_INSPECTION = DESCRIPTOR.message_types_by_name['Inspection']
_QUALITY = DESCRIPTOR.message_types_by_name['Quality']
_DELOGOINFO = DESCRIPTOR.message_types_by_name['DeLogoInfo']
_VISUALQUALITY = DESCRIPTOR.message_types_by_name['VisualQuality']
_VOLUMEINFO = DESCRIPTOR.message_types_by_name['VolumeInfo']
_CATEGORYTAGINFO = DESCRIPTOR.message_types_by_name['CategoryTagInfo']
_CATEGORYTAGINFO_PARENTINFOENTRY = _CATEGORYTAGINFO.nested_types_by_name['ParentInfoEntry']
_VODLISTWORKFLOWEXECUTIONRESULT = DESCRIPTOR.message_types_by_name['VodListWorkflowExecutionResult']
_WORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name['WorkflowExecution']
_VODGETWORKFLOWEXECUTIONDETAILRESULT = DESCRIPTOR.message_types_by_name['VodGetWorkflowExecutionDetailResult']
_EXECUTIONSTAGE = DESCRIPTOR.message_types_by_name['ExecutionStage']
_STAGEDETAIL = DESCRIPTOR.message_types_by_name['StageDetail']
VodStartWorkflowResult = _reflection.GeneratedProtocolMessageType('VodStartWorkflowResult', (_message.Message,), {
  'DESCRIPTOR' : _VODSTARTWORKFLOWRESULT,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodStartWorkflowResult)
  })
_sym_db.RegisterMessage(VodStartWorkflowResult)

WorkflowParams = _reflection.GeneratedProtocolMessageType('WorkflowParams', (_message.Message,), {

  'ConditionEntry' : _reflection.GeneratedProtocolMessageType('ConditionEntry', (_message.Message,), {
    'DESCRIPTOR' : _WORKFLOWPARAMS_CONDITIONENTRY,
    '__module__' : 'vod.business.vod_workflow_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.WorkflowParams.ConditionEntry)
    })
  ,
  'DESCRIPTOR' : _WORKFLOWPARAMS,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.WorkflowParams)
  })
_sym_db.RegisterMessage(WorkflowParams)
_sym_db.RegisterMessage(WorkflowParams.ConditionEntry)

OverrideParams = _reflection.GeneratedProtocolMessageType('OverrideParams', (_message.Message,), {
  'DESCRIPTOR' : _OVERRIDEPARAMS,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.OverrideParams)
  })
_sym_db.RegisterMessage(OverrideParams)

LogoOverride = _reflection.GeneratedProtocolMessageType('LogoOverride', (_message.Message,), {

  'VarsEntry' : _reflection.GeneratedProtocolMessageType('VarsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOGOOVERRIDE_VARSENTRY,
    '__module__' : 'vod.business.vod_workflow_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.LogoOverride.VarsEntry)
    })
  ,
  'DESCRIPTOR' : _LOGOOVERRIDE,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.LogoOverride)
  })
_sym_db.RegisterMessage(LogoOverride)
_sym_db.RegisterMessage(LogoOverride.VarsEntry)

TranscodeVideoOverride = _reflection.GeneratedProtocolMessageType('TranscodeVideoOverride', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCODEVIDEOOVERRIDE,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.TranscodeVideoOverride)
  })
_sym_db.RegisterMessage(TranscodeVideoOverride)

Clip = _reflection.GeneratedProtocolMessageType('Clip', (_message.Message,), {
  'DESCRIPTOR' : _CLIP,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.Clip)
  })
_sym_db.RegisterMessage(Clip)

TranscodeAudioOverride = _reflection.GeneratedProtocolMessageType('TranscodeAudioOverride', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCODEAUDIOOVERRIDE,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.TranscodeAudioOverride)
  })
_sym_db.RegisterMessage(TranscodeAudioOverride)

SnapshotOverride = _reflection.GeneratedProtocolMessageType('SnapshotOverride', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTOVERRIDE,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.SnapshotOverride)
  })
_sym_db.RegisterMessage(SnapshotOverride)

TranscodeResult = _reflection.GeneratedProtocolMessageType('TranscodeResult', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCODERESULT,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.TranscodeResult)
  })
_sym_db.RegisterMessage(TranscodeResult)

Inspection = _reflection.GeneratedProtocolMessageType('Inspection', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTION,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.Inspection)
  })
_sym_db.RegisterMessage(Inspection)

Quality = _reflection.GeneratedProtocolMessageType('Quality', (_message.Message,), {
  'DESCRIPTOR' : _QUALITY,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.Quality)
  })
_sym_db.RegisterMessage(Quality)

DeLogoInfo = _reflection.GeneratedProtocolMessageType('DeLogoInfo', (_message.Message,), {
  'DESCRIPTOR' : _DELOGOINFO,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.DeLogoInfo)
  })
_sym_db.RegisterMessage(DeLogoInfo)

VisualQuality = _reflection.GeneratedProtocolMessageType('VisualQuality', (_message.Message,), {
  'DESCRIPTOR' : _VISUALQUALITY,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VisualQuality)
  })
_sym_db.RegisterMessage(VisualQuality)

VolumeInfo = _reflection.GeneratedProtocolMessageType('VolumeInfo', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMEINFO,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VolumeInfo)
  })
_sym_db.RegisterMessage(VolumeInfo)

CategoryTagInfo = _reflection.GeneratedProtocolMessageType('CategoryTagInfo', (_message.Message,), {

  'ParentInfoEntry' : _reflection.GeneratedProtocolMessageType('ParentInfoEntry', (_message.Message,), {
    'DESCRIPTOR' : _CATEGORYTAGINFO_PARENTINFOENTRY,
    '__module__' : 'vod.business.vod_workflow_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CategoryTagInfo.ParentInfoEntry)
    })
  ,
  'DESCRIPTOR' : _CATEGORYTAGINFO,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CategoryTagInfo)
  })
_sym_db.RegisterMessage(CategoryTagInfo)
_sym_db.RegisterMessage(CategoryTagInfo.ParentInfoEntry)

VodListWorkflowExecutionResult = _reflection.GeneratedProtocolMessageType('VodListWorkflowExecutionResult', (_message.Message,), {
  'DESCRIPTOR' : _VODLISTWORKFLOWEXECUTIONRESULT,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodListWorkflowExecutionResult)
  })
_sym_db.RegisterMessage(VodListWorkflowExecutionResult)

WorkflowExecution = _reflection.GeneratedProtocolMessageType('WorkflowExecution', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWEXECUTION,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.WorkflowExecution)
  })
_sym_db.RegisterMessage(WorkflowExecution)

VodGetWorkflowExecutionDetailResult = _reflection.GeneratedProtocolMessageType('VodGetWorkflowExecutionDetailResult', (_message.Message,), {
  'DESCRIPTOR' : _VODGETWORKFLOWEXECUTIONDETAILRESULT,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodGetWorkflowExecutionDetailResult)
  })
_sym_db.RegisterMessage(VodGetWorkflowExecutionDetailResult)

ExecutionStage = _reflection.GeneratedProtocolMessageType('ExecutionStage', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONSTAGE,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ExecutionStage)
  })
_sym_db.RegisterMessage(ExecutionStage)

StageDetail = _reflection.GeneratedProtocolMessageType('StageDetail', (_message.Message,), {
  'DESCRIPTOR' : _STAGEDETAIL,
  '__module__' : 'vod.business.vod_workflow_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.StageDetail)
  })
_sym_db.RegisterMessage(StageDetail)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\013VodWorkflowP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _WORKFLOWPARAMS_CONDITIONENTRY._options = None
  _WORKFLOWPARAMS_CONDITIONENTRY._serialized_options = b'8\001'
  _LOGOOVERRIDE_VARSENTRY._options = None
  _LOGOOVERRIDE_VARSENTRY._serialized_options = b'8\001'
  _CATEGORYTAGINFO_PARENTINFOENTRY._options = None
  _CATEGORYTAGINFO_PARENTINFOENTRY._serialized_options = b'8\001'
  _STAGESTATUS._serialized_start=3641
  _STAGESTATUS._serialized_end=3763
  _VODSTARTWORKFLOWRESULT._serialized_start=100
  _VODSTARTWORKFLOWRESULT._serialized_end=139
  _WORKFLOWPARAMS._serialized_start=142
  _WORKFLOWPARAMS._serialized_end=362
  _WORKFLOWPARAMS_CONDITIONENTRY._serialized_start=314
  _WORKFLOWPARAMS_CONDITIONENTRY._serialized_end=362
  _OVERRIDEPARAMS._serialized_start=365
  _OVERRIDEPARAMS._serialized_end=669
  _LOGOOVERRIDE._serialized_start=672
  _LOGOOVERRIDE._serialized_end=821
  _LOGOOVERRIDE_VARSENTRY._serialized_start=778
  _LOGOOVERRIDE_VARSENTRY._serialized_end=821
  _TRANSCODEVIDEOOVERRIDE._serialized_start=824
  _TRANSCODEVIDEOOVERRIDE._serialized_end=959
  _CLIP._serialized_start=961
  _CLIP._serialized_end=1003
  _TRANSCODEAUDIOOVERRIDE._serialized_start=1005
  _TRANSCODEAUDIOOVERRIDE._serialized_end=1119
  _SNAPSHOTOVERRIDE._serialized_start=1121
  _SNAPSHOTOVERRIDE._serialized_end=1203
  _TRANSCODERESULT._serialized_start=1206
  _TRANSCODERESULT._serialized_end=1371
  _INSPECTION._serialized_start=1374
  _INSPECTION._serialized_end=1504
  _QUALITY._serialized_start=1507
  _QUALITY._serialized_end=1643
  _DELOGOINFO._serialized_start=1645
  _DELOGOINFO._serialized_end=1758
  _VISUALQUALITY._serialized_start=1760
  _VISUALQUALITY._serialized_end=1884
  _VOLUMEINFO._serialized_start=1886
  _VOLUMEINFO._serialized_end=1969
  _CATEGORYTAGINFO._serialized_start=1972
  _CATEGORYTAGINFO._serialized_end=2186
  _CATEGORYTAGINFO_PARENTINFOENTRY._serialized_start=2137
  _CATEGORYTAGINFO_PARENTINFOENTRY._serialized_end=2186
  _VODLISTWORKFLOWEXECUTIONRESULT._serialized_start=2189
  _VODLISTWORKFLOWEXECUTIONRESULT._serialized_end=2340
  _WORKFLOWEXECUTION._serialized_start=2343
  _WORKFLOWEXECUTION._serialized_end=2776
  _VODGETWORKFLOWEXECUTIONDETAILRESULT._serialized_start=2779
  _VODGETWORKFLOWEXECUTIONDETAILRESULT._serialized_end=3169
  _EXECUTIONSTAGE._serialized_start=3172
  _EXECUTIONSTAGE._serialized_end=3367
  _STAGEDETAIL._serialized_start=3370
  _STAGEDETAIL._serialized_end=3639
# @@protoc_insertion_point(module_scope)
