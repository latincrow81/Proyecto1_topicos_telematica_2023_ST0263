# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mom.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tmom.proto\"?\n\x0cQueueRequest\x12\x12\n\nqueue_name\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\n\n\x02op\x18\x03 \x01(\t\"?\n\x0cTopicRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\n\n\x02op\x18\x03 \x01(\t\"\x1f\n\rTopicResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1f\n\rQueueResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\"\n\x0fMessageResponse\x12\x0f\n\x07payload\x18\x01 \x01(\t2\xcc\x01\n\x0cMessageQueue\x12.\n\x0bPushMessage\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12\x30\n\x0bPullMessage\x12\r.QueueRequest\x1a\x10.MessageResponse\"\x00\x12,\n\tPushTopic\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12,\n\tPullTopic\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mom_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUEUEREQUEST._serialized_start=13
  _QUEUEREQUEST._serialized_end=76
  _TOPICREQUEST._serialized_start=78
  _TOPICREQUEST._serialized_end=141
  _TOPICRESPONSE._serialized_start=143
  _TOPICRESPONSE._serialized_end=174
  _QUEUERESPONSE._serialized_start=176
  _QUEUERESPONSE._serialized_end=207
  _MESSAGERESPONSE._serialized_start=209
  _MESSAGERESPONSE._serialized_end=243
  _MESSAGEQUEUE._serialized_start=246
  _MESSAGEQUEUE._serialized_end=450
# @@protoc_insertion_point(module_scope)
