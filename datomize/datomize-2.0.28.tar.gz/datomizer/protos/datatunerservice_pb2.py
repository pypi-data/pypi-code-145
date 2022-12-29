# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datatunerservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x64\x61tatunerservice.proto\x12\x08\x64\x61takube\"6\n\x0c\x44\x61taTunerDTO\x12&\n\x08ruleSets\x18\x01 \x03(\x0b\x32\x14.datakube.RuleSetDTO\"A\n\nRuleSetDTO\x12\x11\n\ttableName\x18\x01 \x01(\t\x12 \n\x05rules\x18\x02 \x03(\x0b\x32\x11.datakube.RuleDTO\"\x7f\n\x07RuleDTO\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0boutputRatio\x18\x02 \x01(\x01\x12\x14\n\x0coutputAmount\x18\x03 \x01(\x05\x12$\n\x07\x63lauses\x18\x04 \x03(\x0b\x32\x13.datakube.ClauseDTO\x12\x17\n\x0fgeneratedAmount\x18\x05 \x01(\x05\"\xe4\x01\n\tClauseDTO\x12\x12\n\ncolumnName\x18\x01 \x01(\t\x12;\n\x11\x63\x61tegoricalClause\x18\x14 \x01(\x0b\x32\x1e.datakube.CategoricalClauseDTOH\x00\x12/\n\x0brangeClause\x18\x15 \x01(\x0b\x32\x18.datakube.RangeClauseDTOH\x00\x12G\n\x17numericNormalDistClause\x18\x16 \x01(\x0b\x32$.datakube.NumericNormalDistClauseDTOH\x00\x42\x0c\n\nClauseType\"-\n\x14\x43\x61tegoricalClauseDTO\x12\x15\n\rcategoryValue\x18\x01 \x01(\t\"4\n\x0eRangeClauseDTO\x12\x10\n\x08minValue\x18\x01 \x01(\t\x12\x10\n\x08maxValue\x18\x02 \x01(\t\"e\n\x1aNumericNormalDistClauseDTO\x12\x11\n\tmeanValue\x18\x01 \x01(\t\x12\x10\n\x08stdValue\x18\x02 \x01(\t\x12\x10\n\x08minValue\x18\x03 \x01(\t\x12\x10\n\x08maxValue\x18\x04 \x01(\t\"D\n\x11\x44TResultSchemaDTO\x12/\n\x0bresultTable\x18\x01 \x03(\x0b\x32\x1a.datakube.DTResultTableDTO\"\x97\x01\n\x10\x44TResultTableDTO\x12\x11\n\ttableName\x18\x01 \x01(\t\x12(\n\x05rules\x18\x02 \x03(\x0b\x32\x19.datakube.DTResultRuleDTO\x12\r\n\x05score\x18\x03 \x01(\x01\x12\x37\n\x0crealMetaData\x18\x04 \x01(\x0b\x32!.datakube.EffectedColHistMetaData\"\xa0\x03\n\x0f\x44TResultRuleDTO\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x0esynthHistogram\x18\x02 \x03(\x0b\x32\x1e.datakube.DTResultHistogramDTO\x12:\n\x12originalHistograms\x18\x03 \x03(\x0b\x32\x1e.datakube.DTResultHistogramDTO\x12\r\n\x05score\x18\x04 \x01(\x01\x12\x14\n\x0coutputAmount\x18\x06 \x01(\x05\x12\x43\n\x12numEffectedColHist\x18\x07 \x01(\x0b\x32\'.datakube.DTEffectedColumnsHistogramDTO\x12@\n\x0f\x65\x66\x66\x65\x63tedColHist\x18\x08 \x01(\x0b\x32\'.datakube.DTEffectedColumnsHistogramDTO\x12$\n\x07\x63lauses\x18\t \x03(\x0b\x32\x13.datakube.ClauseDTO\x12;\n\x12ifColumnHypothesis\x18\n \x03(\x0b\x32\x1f.datakube.IfColumnHypothesisDTO\"~\n\x14\x44TResultHistogramDTO\x12\x31\n\thistogram\x18\x01 \x03(\x0b\x32\x1e.datakube.DTColumnHistogramDTO\x12\r\n\x05score\x18\x02 \x01(\x01\x12$\n\x07\x63lauses\x18\x03 \x03(\x0b\x32\x13.datakube.ClauseDTO\"e\n\x14\x44TColumnHistogramDTO\x12\x12\n\ncolumnName\x18\x01 \x01(\t\x12\x13\n\x0bxTickLabels\x18\x02 \x03(\t\x12\r\n\x05yData\x18\x03 \x03(\x01\x12\x15\n\risCategorical\x18\x04 \x01(\x08\"x\n\x1d\x44TEffectedColumnsHistogramDTO\x12\x10\n\x08xColName\x18\x01 \x03(\t\x12\r\n\x05yData\x18\x02 \x03(\x01\x12\x36\n\x0bsynMetaData\x18\x07 \x01(\x0b\x32!.datakube.EffectedColHistMetaData\"\x87\x01\n\x17\x45\x66\x66\x65\x63tedColHistMetaData\x12\x13\n\x0b\x63olumnNames\x18\x01 \x03(\t\x12\x0c\n\x04mean\x18\x02 \x03(\x01\x12\x0b\n\x03std\x18\x03 \x03(\x01\x12\x0b\n\x03min\x18\x04 \x03(\x01\x12\x0b\n\x03max\x18\x05 \x03(\x01\x12\n\n\x02q1\x18\x06 \x03(\x01\x12\n\n\x02q2\x18\x07 \x03(\x01\x12\n\n\x02q3\x18\x08 \x03(\x01\"C\n\x0eWhatIfTunerDTO\x12\x31\n\rhypothesisSet\x18\x01 \x03(\x0b\x32\x1a.datakube.HypothesisSetDTO\"\x7f\n\x10HypothesisSetDTO\x12\x11\n\ttableName\x18\x01 \x01(\t\x12\x14\n\x0cgivenColumns\x18\x02 \x03(\t\x12\x13\n\x0bwhatColumns\x18\x03 \x03(\t\x12-\n\nhypothesis\x18\x04 \x03(\x0b\x32\x19.datakube.IfHypothesisDTO\"s\n\x0fIfHypothesisDTO\x12\n\n\x02id\x18\x01 \x01(\x05\x12;\n\x12ifColumnHypothesis\x18\x02 \x03(\x0b\x32\x1f.datakube.IfColumnHypothesisDTO\x12\x17\n\x0fgeneratedAmount\x18\x03 \x01(\x05\"\x8e\x03\n\x15IfColumnHypothesisDTO\x12\x12\n\ncolumnName\x18\x01 \x01(\t\x12I\n\x18\x63\x61tegoricalMapHypothesis\x18\x14 \x01(\x0b\x32%.datakube.CategoricalHypothesisMapDTOH\x00\x12M\n\x1a\x63\x61tegoricalConstHypothesis\x18\x15 \x01(\x0b\x32\'.datakube.CategoricalHypothesisConstDTOH\x00\x12=\n\x11numericHypothesis\x18\x16 \x01(\x0b\x32 .datakube.NumericalHypothesisDTOH\x00\x12\x35\n\x0e\x64\x61teHypothesis\x18\x17 \x01(\x0b\x32\x1b.datakube.DateHypothesisDTOH\x00\x12?\n\x13\x64\x61teConstHypothesis\x18\x18 \x01(\x0b\x32 .datakube.DateConstHypothesisDTOH\x00\x42\x10\n\x0eHypothesisType\".\n\x1d\x43\x61tegoricalHypothesisConstDTO\x12\r\n\x05value\x18\x01 \x01(\t\"L\n\x1b\x43\x61tegoricalHypothesisMapDTO\x12-\n\x0b\x63\x61tegoryMap\x18\x01 \x03(\x0b\x32\x18.datakube.CategoryMapDTO\"I\n\x0e\x43\x61tegoryMapDTO\x12\x1d\n\x15originalCategoryValue\x18\x01 \x01(\t\x12\x18\n\x10newCategoryValue\x18\x02 \x01(\t\"|\n\x16NumericalHypothesisDTO\x12\r\n\x05value\x18\x01 \x01(\x01\x12/\n\tnumericOp\x18\x02 \x01(\x0e\x32\x1c.datakube.NumericalOperation\x12\x10\n\x08minValue\x18\x03 \x01(\x01\x12\x10\n\x08maxValue\x18\x04 \x01(\x01\":\n\x11\x44\x61teHypothesisDTO\x12%\n\x07\x64\x61teMap\x18\x01 \x03(\x0b\x32\x14.datakube.DateMapDTO\"A\n\nDateMapDTO\x12\r\n\x05value\x18\x01 \x01(\x01\x12$\n\x08\x64\x61teUnit\x18\x02 \x01(\x0e\x32\x12.datakube.DateUnit\"\'\n\x16\x44\x61teConstHypothesisDTO\x12\r\n\x05value\x18\x01 \x01(\t*D\n\x12NumericalOperation\x12\x0c\n\x08\x41\x44\x44ITION\x10\x00\x12\x12\n\x0eMULTIPLICATION\x10\x01\x12\x0c\n\x08\x43ONSTANT\x10\x02*9\n\x08\x44\x61teUnit\x12\x08\n\x04\x44\x41YS\x10\x00\x12\t\n\x05HOURS\x10\x01\x12\x0b\n\x07MINUTES\x10\x02\x12\x0b\n\x07SECONDS\x10\x03\x42\x63\nIcom.datomize.datomizer.backend.components.management.dto.datatunerserviceB\x16\x44\x61taTunerServiceProtosb\x06proto3')

_NUMERICALOPERATION = DESCRIPTOR.enum_types_by_name['NumericalOperation']
NumericalOperation = enum_type_wrapper.EnumTypeWrapper(_NUMERICALOPERATION)
_DATEUNIT = DESCRIPTOR.enum_types_by_name['DateUnit']
DateUnit = enum_type_wrapper.EnumTypeWrapper(_DATEUNIT)
ADDITION = 0
MULTIPLICATION = 1
CONSTANT = 2
DAYS = 0
HOURS = 1
MINUTES = 2
SECONDS = 3


_DATATUNERDTO = DESCRIPTOR.message_types_by_name['DataTunerDTO']
_RULESETDTO = DESCRIPTOR.message_types_by_name['RuleSetDTO']
_RULEDTO = DESCRIPTOR.message_types_by_name['RuleDTO']
_CLAUSEDTO = DESCRIPTOR.message_types_by_name['ClauseDTO']
_CATEGORICALCLAUSEDTO = DESCRIPTOR.message_types_by_name['CategoricalClauseDTO']
_RANGECLAUSEDTO = DESCRIPTOR.message_types_by_name['RangeClauseDTO']
_NUMERICNORMALDISTCLAUSEDTO = DESCRIPTOR.message_types_by_name['NumericNormalDistClauseDTO']
_DTRESULTSCHEMADTO = DESCRIPTOR.message_types_by_name['DTResultSchemaDTO']
_DTRESULTTABLEDTO = DESCRIPTOR.message_types_by_name['DTResultTableDTO']
_DTRESULTRULEDTO = DESCRIPTOR.message_types_by_name['DTResultRuleDTO']
_DTRESULTHISTOGRAMDTO = DESCRIPTOR.message_types_by_name['DTResultHistogramDTO']
_DTCOLUMNHISTOGRAMDTO = DESCRIPTOR.message_types_by_name['DTColumnHistogramDTO']
_DTEFFECTEDCOLUMNSHISTOGRAMDTO = DESCRIPTOR.message_types_by_name['DTEffectedColumnsHistogramDTO']
_EFFECTEDCOLHISTMETADATA = DESCRIPTOR.message_types_by_name['EffectedColHistMetaData']
_WHATIFTUNERDTO = DESCRIPTOR.message_types_by_name['WhatIfTunerDTO']
_HYPOTHESISSETDTO = DESCRIPTOR.message_types_by_name['HypothesisSetDTO']
_IFHYPOTHESISDTO = DESCRIPTOR.message_types_by_name['IfHypothesisDTO']
_IFCOLUMNHYPOTHESISDTO = DESCRIPTOR.message_types_by_name['IfColumnHypothesisDTO']
_CATEGORICALHYPOTHESISCONSTDTO = DESCRIPTOR.message_types_by_name['CategoricalHypothesisConstDTO']
_CATEGORICALHYPOTHESISMAPDTO = DESCRIPTOR.message_types_by_name['CategoricalHypothesisMapDTO']
_CATEGORYMAPDTO = DESCRIPTOR.message_types_by_name['CategoryMapDTO']
_NUMERICALHYPOTHESISDTO = DESCRIPTOR.message_types_by_name['NumericalHypothesisDTO']
_DATEHYPOTHESISDTO = DESCRIPTOR.message_types_by_name['DateHypothesisDTO']
_DATEMAPDTO = DESCRIPTOR.message_types_by_name['DateMapDTO']
_DATECONSTHYPOTHESISDTO = DESCRIPTOR.message_types_by_name['DateConstHypothesisDTO']
DataTunerDTO = _reflection.GeneratedProtocolMessageType('DataTunerDTO', (_message.Message,), {
  'DESCRIPTOR' : _DATATUNERDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DataTunerDTO)
  })
_sym_db.RegisterMessage(DataTunerDTO)

RuleSetDTO = _reflection.GeneratedProtocolMessageType('RuleSetDTO', (_message.Message,), {
  'DESCRIPTOR' : _RULESETDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.RuleSetDTO)
  })
_sym_db.RegisterMessage(RuleSetDTO)

RuleDTO = _reflection.GeneratedProtocolMessageType('RuleDTO', (_message.Message,), {
  'DESCRIPTOR' : _RULEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.RuleDTO)
  })
_sym_db.RegisterMessage(RuleDTO)

ClauseDTO = _reflection.GeneratedProtocolMessageType('ClauseDTO', (_message.Message,), {
  'DESCRIPTOR' : _CLAUSEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.ClauseDTO)
  })
_sym_db.RegisterMessage(ClauseDTO)

CategoricalClauseDTO = _reflection.GeneratedProtocolMessageType('CategoricalClauseDTO', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORICALCLAUSEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.CategoricalClauseDTO)
  })
_sym_db.RegisterMessage(CategoricalClauseDTO)

RangeClauseDTO = _reflection.GeneratedProtocolMessageType('RangeClauseDTO', (_message.Message,), {
  'DESCRIPTOR' : _RANGECLAUSEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.RangeClauseDTO)
  })
_sym_db.RegisterMessage(RangeClauseDTO)

NumericNormalDistClauseDTO = _reflection.GeneratedProtocolMessageType('NumericNormalDistClauseDTO', (_message.Message,), {
  'DESCRIPTOR' : _NUMERICNORMALDISTCLAUSEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.NumericNormalDistClauseDTO)
  })
_sym_db.RegisterMessage(NumericNormalDistClauseDTO)

DTResultSchemaDTO = _reflection.GeneratedProtocolMessageType('DTResultSchemaDTO', (_message.Message,), {
  'DESCRIPTOR' : _DTRESULTSCHEMADTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DTResultSchemaDTO)
  })
_sym_db.RegisterMessage(DTResultSchemaDTO)

DTResultTableDTO = _reflection.GeneratedProtocolMessageType('DTResultTableDTO', (_message.Message,), {
  'DESCRIPTOR' : _DTRESULTTABLEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DTResultTableDTO)
  })
_sym_db.RegisterMessage(DTResultTableDTO)

DTResultRuleDTO = _reflection.GeneratedProtocolMessageType('DTResultRuleDTO', (_message.Message,), {
  'DESCRIPTOR' : _DTRESULTRULEDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DTResultRuleDTO)
  })
_sym_db.RegisterMessage(DTResultRuleDTO)

DTResultHistogramDTO = _reflection.GeneratedProtocolMessageType('DTResultHistogramDTO', (_message.Message,), {
  'DESCRIPTOR' : _DTRESULTHISTOGRAMDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DTResultHistogramDTO)
  })
_sym_db.RegisterMessage(DTResultHistogramDTO)

DTColumnHistogramDTO = _reflection.GeneratedProtocolMessageType('DTColumnHistogramDTO', (_message.Message,), {
  'DESCRIPTOR' : _DTCOLUMNHISTOGRAMDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DTColumnHistogramDTO)
  })
_sym_db.RegisterMessage(DTColumnHistogramDTO)

DTEffectedColumnsHistogramDTO = _reflection.GeneratedProtocolMessageType('DTEffectedColumnsHistogramDTO', (_message.Message,), {
  'DESCRIPTOR' : _DTEFFECTEDCOLUMNSHISTOGRAMDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DTEffectedColumnsHistogramDTO)
  })
_sym_db.RegisterMessage(DTEffectedColumnsHistogramDTO)

EffectedColHistMetaData = _reflection.GeneratedProtocolMessageType('EffectedColHistMetaData', (_message.Message,), {
  'DESCRIPTOR' : _EFFECTEDCOLHISTMETADATA,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.EffectedColHistMetaData)
  })
_sym_db.RegisterMessage(EffectedColHistMetaData)

WhatIfTunerDTO = _reflection.GeneratedProtocolMessageType('WhatIfTunerDTO', (_message.Message,), {
  'DESCRIPTOR' : _WHATIFTUNERDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.WhatIfTunerDTO)
  })
_sym_db.RegisterMessage(WhatIfTunerDTO)

HypothesisSetDTO = _reflection.GeneratedProtocolMessageType('HypothesisSetDTO', (_message.Message,), {
  'DESCRIPTOR' : _HYPOTHESISSETDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.HypothesisSetDTO)
  })
_sym_db.RegisterMessage(HypothesisSetDTO)

IfHypothesisDTO = _reflection.GeneratedProtocolMessageType('IfHypothesisDTO', (_message.Message,), {
  'DESCRIPTOR' : _IFHYPOTHESISDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.IfHypothesisDTO)
  })
_sym_db.RegisterMessage(IfHypothesisDTO)

IfColumnHypothesisDTO = _reflection.GeneratedProtocolMessageType('IfColumnHypothesisDTO', (_message.Message,), {
  'DESCRIPTOR' : _IFCOLUMNHYPOTHESISDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.IfColumnHypothesisDTO)
  })
_sym_db.RegisterMessage(IfColumnHypothesisDTO)

CategoricalHypothesisConstDTO = _reflection.GeneratedProtocolMessageType('CategoricalHypothesisConstDTO', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORICALHYPOTHESISCONSTDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.CategoricalHypothesisConstDTO)
  })
_sym_db.RegisterMessage(CategoricalHypothesisConstDTO)

CategoricalHypothesisMapDTO = _reflection.GeneratedProtocolMessageType('CategoricalHypothesisMapDTO', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORICALHYPOTHESISMAPDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.CategoricalHypothesisMapDTO)
  })
_sym_db.RegisterMessage(CategoricalHypothesisMapDTO)

CategoryMapDTO = _reflection.GeneratedProtocolMessageType('CategoryMapDTO', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYMAPDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.CategoryMapDTO)
  })
_sym_db.RegisterMessage(CategoryMapDTO)

NumericalHypothesisDTO = _reflection.GeneratedProtocolMessageType('NumericalHypothesisDTO', (_message.Message,), {
  'DESCRIPTOR' : _NUMERICALHYPOTHESISDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.NumericalHypothesisDTO)
  })
_sym_db.RegisterMessage(NumericalHypothesisDTO)

DateHypothesisDTO = _reflection.GeneratedProtocolMessageType('DateHypothesisDTO', (_message.Message,), {
  'DESCRIPTOR' : _DATEHYPOTHESISDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DateHypothesisDTO)
  })
_sym_db.RegisterMessage(DateHypothesisDTO)

DateMapDTO = _reflection.GeneratedProtocolMessageType('DateMapDTO', (_message.Message,), {
  'DESCRIPTOR' : _DATEMAPDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DateMapDTO)
  })
_sym_db.RegisterMessage(DateMapDTO)

DateConstHypothesisDTO = _reflection.GeneratedProtocolMessageType('DateConstHypothesisDTO', (_message.Message,), {
  'DESCRIPTOR' : _DATECONSTHYPOTHESISDTO,
  '__module__' : 'datatunerservice_pb2'
  # @@protoc_insertion_point(class_scope:datakube.DateConstHypothesisDTO)
  })
_sym_db.RegisterMessage(DateConstHypothesisDTO)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nIcom.datomize.datomizer.backend.components.management.dto.datatunerserviceB\026DataTunerServiceProtos'
  _NUMERICALOPERATION._serialized_start=3068
  _NUMERICALOPERATION._serialized_end=3136
  _DATEUNIT._serialized_start=3138
  _DATEUNIT._serialized_end=3195
  _DATATUNERDTO._serialized_start=36
  _DATATUNERDTO._serialized_end=90
  _RULESETDTO._serialized_start=92
  _RULESETDTO._serialized_end=157
  _RULEDTO._serialized_start=159
  _RULEDTO._serialized_end=286
  _CLAUSEDTO._serialized_start=289
  _CLAUSEDTO._serialized_end=517
  _CATEGORICALCLAUSEDTO._serialized_start=519
  _CATEGORICALCLAUSEDTO._serialized_end=564
  _RANGECLAUSEDTO._serialized_start=566
  _RANGECLAUSEDTO._serialized_end=618
  _NUMERICNORMALDISTCLAUSEDTO._serialized_start=620
  _NUMERICNORMALDISTCLAUSEDTO._serialized_end=721
  _DTRESULTSCHEMADTO._serialized_start=723
  _DTRESULTSCHEMADTO._serialized_end=791
  _DTRESULTTABLEDTO._serialized_start=794
  _DTRESULTTABLEDTO._serialized_end=945
  _DTRESULTRULEDTO._serialized_start=948
  _DTRESULTRULEDTO._serialized_end=1364
  _DTRESULTHISTOGRAMDTO._serialized_start=1366
  _DTRESULTHISTOGRAMDTO._serialized_end=1492
  _DTCOLUMNHISTOGRAMDTO._serialized_start=1494
  _DTCOLUMNHISTOGRAMDTO._serialized_end=1595
  _DTEFFECTEDCOLUMNSHISTOGRAMDTO._serialized_start=1597
  _DTEFFECTEDCOLUMNSHISTOGRAMDTO._serialized_end=1717
  _EFFECTEDCOLHISTMETADATA._serialized_start=1720
  _EFFECTEDCOLHISTMETADATA._serialized_end=1855
  _WHATIFTUNERDTO._serialized_start=1857
  _WHATIFTUNERDTO._serialized_end=1924
  _HYPOTHESISSETDTO._serialized_start=1926
  _HYPOTHESISSETDTO._serialized_end=2053
  _IFHYPOTHESISDTO._serialized_start=2055
  _IFHYPOTHESISDTO._serialized_end=2170
  _IFCOLUMNHYPOTHESISDTO._serialized_start=2173
  _IFCOLUMNHYPOTHESISDTO._serialized_end=2571
  _CATEGORICALHYPOTHESISCONSTDTO._serialized_start=2573
  _CATEGORICALHYPOTHESISCONSTDTO._serialized_end=2619
  _CATEGORICALHYPOTHESISMAPDTO._serialized_start=2621
  _CATEGORICALHYPOTHESISMAPDTO._serialized_end=2697
  _CATEGORYMAPDTO._serialized_start=2699
  _CATEGORYMAPDTO._serialized_end=2772
  _NUMERICALHYPOTHESISDTO._serialized_start=2774
  _NUMERICALHYPOTHESISDTO._serialized_end=2898
  _DATEHYPOTHESISDTO._serialized_start=2900
  _DATEHYPOTHESISDTO._serialized_end=2958
  _DATEMAPDTO._serialized_start=2960
  _DATEMAPDTO._serialized_end=3025
  _DATECONSTHYPOTHESISDTO._serialized_start=3027
  _DATECONSTHYPOTHESISDTO._serialized_end=3066
# @@protoc_insertion_point(module_scope)
