# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enhancemlresults.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x65nhancemlresults.proto\x12\tenhanceml\"m\n\x13\x45nhanceMLResultsDTO\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.enhanceml.AlgorithmType\x12.\n\x0bmetricScore\x18\x02 \x03(\x0b\x32\x19.enhanceml.MetricScoreDTO\"s\n\x0eMetricScoreDTO\x12)\n\nmetricName\x18\x01 \x01(\x0e\x32\x15.enhanceml.MetricName\x12\x36\n\x0f\x61lgorithmResult\x18\x02 \x03(\x0b\x32\x1d.enhanceml.AlgorithmResultDTO\"\x82\x01\n\x12\x41lgorithmResultDTO\x12/\n\ralgorithmName\x18\x01 \x01(\x0e\x32\x18.enhanceml.AlgorithmName\x12\r\n\x05score\x18\x02 \x01(\x01\x12\x12\n\nsynthScore\x18\x03 \x01(\x01\x12\x18\n\x10improvementScore\x18\x04 \x01(\x01*6\n\rAlgorithmType\x12\n\n\x06\x42INARY\x10\x00\x12\t\n\x05MULTI\x10\x01\x12\x0e\n\nREGRESSION\x10\x02*\xa1\x01\n\nMetricName\x12\x07\n\x03\x41\x43\x43\x10\x00\x12\x10\n\x0c\x42\x41LANCED_ACC\x10\x01\x12\r\n\tPRECISION\x10\x02\x12\n\n\x06RECALL\x10\x03\x12\x06\n\x02\x46\x31\x10\x04\x12\x07\n\x03\x41UC\x10\x05\x12\x0b\n\x07ROC_AUC\x10\x06\x12\x07\n\x03MSE\x10\x07\x12\x08\n\x04RMSE\x10\x08\x12\x07\n\x03MAE\x10\t\x12\x0b\n\x07\x41VG_PRC\x10\n\x12\n\n\x06MAX_F1\x10\x0b\x12\n\n\x06PR_AUC\x10\x0c*\xd2\x01\n\rAlgorithmName\x12\x11\n\rRANDOM_FOREST\x10\x00\x12\x11\n\rDECISION_TREE\x10\x01\x12\x07\n\x03GBM\x10\x02\x12\x07\n\x03KNN\x10\x03\x12\x07\n\x03\x42GG\x10\x04\x12\x06\n\x02NB\x10\x05\x12\x06\n\x02NN\x10\x06\x12\x06\n\x02LR\x10\x07\x12\x07\n\x03SVM\x10\x08\x12\x0e\n\nLINEAR_SVM\x10\t\x12\x0c\n\x08POLY_SVM\x10\n\x12\x0c\n\x08\x41\x44\x41\x42OOST\x10\x0b\x12\x0e\n\nEXTRA_TREE\x10\x0c\x12\x0c\n\x08\x43\x41TBOOST\x10\r\x12\x08\n\x04LGBM\x10\x0e\x12\x0b\n\x07XGBOOST\x10\x0f\x42]\nIcom.datomize.datomizer.backend.components.management.dto.enhancemlresultsB\x10\x65nhancemlresultsb\x06proto3')

_ALGORITHMTYPE = DESCRIPTOR.enum_types_by_name['AlgorithmType']
AlgorithmType = enum_type_wrapper.EnumTypeWrapper(_ALGORITHMTYPE)
_METRICNAME = DESCRIPTOR.enum_types_by_name['MetricName']
MetricName = enum_type_wrapper.EnumTypeWrapper(_METRICNAME)
_ALGORITHMNAME = DESCRIPTOR.enum_types_by_name['AlgorithmName']
AlgorithmName = enum_type_wrapper.EnumTypeWrapper(_ALGORITHMNAME)
BINARY = 0
MULTI = 1
REGRESSION = 2
ACC = 0
BALANCED_ACC = 1
PRECISION = 2
RECALL = 3
F1 = 4
AUC = 5
ROC_AUC = 6
MSE = 7
RMSE = 8
MAE = 9
AVG_PRC = 10
MAX_F1 = 11
PR_AUC = 12
RANDOM_FOREST = 0
DECISION_TREE = 1
GBM = 2
KNN = 3
BGG = 4
NB = 5
NN = 6
LR = 7
SVM = 8
LINEAR_SVM = 9
POLY_SVM = 10
ADABOOST = 11
EXTRA_TREE = 12
CATBOOST = 13
LGBM = 14
XGBOOST = 15


_ENHANCEMLRESULTSDTO = DESCRIPTOR.message_types_by_name['EnhanceMLResultsDTO']
_METRICSCOREDTO = DESCRIPTOR.message_types_by_name['MetricScoreDTO']
_ALGORITHMRESULTDTO = DESCRIPTOR.message_types_by_name['AlgorithmResultDTO']
EnhanceMLResultsDTO = _reflection.GeneratedProtocolMessageType('EnhanceMLResultsDTO', (_message.Message,), {
  'DESCRIPTOR' : _ENHANCEMLRESULTSDTO,
  '__module__' : 'enhancemlresults_pb2'
  # @@protoc_insertion_point(class_scope:enhanceml.EnhanceMLResultsDTO)
  })
_sym_db.RegisterMessage(EnhanceMLResultsDTO)

MetricScoreDTO = _reflection.GeneratedProtocolMessageType('MetricScoreDTO', (_message.Message,), {
  'DESCRIPTOR' : _METRICSCOREDTO,
  '__module__' : 'enhancemlresults_pb2'
  # @@protoc_insertion_point(class_scope:enhanceml.MetricScoreDTO)
  })
_sym_db.RegisterMessage(MetricScoreDTO)

AlgorithmResultDTO = _reflection.GeneratedProtocolMessageType('AlgorithmResultDTO', (_message.Message,), {
  'DESCRIPTOR' : _ALGORITHMRESULTDTO,
  '__module__' : 'enhancemlresults_pb2'
  # @@protoc_insertion_point(class_scope:enhanceml.AlgorithmResultDTO)
  })
_sym_db.RegisterMessage(AlgorithmResultDTO)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nIcom.datomize.datomizer.backend.components.management.dto.enhancemlresultsB\020enhancemlresults'
  _ALGORITHMTYPE._serialized_start=398
  _ALGORITHMTYPE._serialized_end=452
  _METRICNAME._serialized_start=455
  _METRICNAME._serialized_end=616
  _ALGORITHMNAME._serialized_start=619
  _ALGORITHMNAME._serialized_end=829
  _ENHANCEMLRESULTSDTO._serialized_start=37
  _ENHANCEMLRESULTSDTO._serialized_end=146
  _METRICSCOREDTO._serialized_start=148
  _METRICSCOREDTO._serialized_end=263
  _ALGORITHMRESULTDTO._serialized_start=266
  _ALGORITHMRESULTDTO._serialized_end=396
# @@protoc_insertion_point(module_scope)
