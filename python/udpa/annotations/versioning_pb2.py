# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: udpa/annotations/versioning.proto
# Protobuf Python Version: 5.29.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    1,
    '',
    'udpa/annotations/versioning.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!udpa/annotations/versioning.proto\x12\x10udpa.annotations\x1a google/protobuf/descriptor.proto\"5\n\x14VersioningAnnotation\x12\x1d\n\x15previous_message_type\x18\x01 \x01(\t:^\n\nversioning\x12\x1f.google.protobuf.MessageOptions\x18\xd3\x88\xe1\x03 \x01(\x0b\x32&.udpa.annotations.VersioningAnnotationB)Z\'github.com/cncf/xds/go/udpa/annotationsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'udpa.annotations.versioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/cncf/xds/go/udpa/annotations'
  _globals['_VERSIONINGANNOTATION']._serialized_start=89
  _globals['_VERSIONINGANNOTATION']._serialized_end=142
# @@protoc_insertion_point(module_scope)