# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Echo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Echo.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nEcho.proto\"\x1c\n\x0b\x45\x63hoRequest\x12\r\n\x05words\x18\x01 \x01(\t\"\x1a\n\tEchoReply\x12\r\n\x05words\x18\x01 \x01(\t21\n\x0b\x45\x63hoService\x12\"\n\x04\x65\x63ho\x12\x0c.EchoRequest\x1a\n.EchoReply\"\x00\x62\x06proto3')
)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='EchoRequest.words', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=42,
)


_ECHOREPLY = _descriptor.Descriptor(
  name='EchoReply',
  full_name='EchoReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='EchoReply.words', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoReply'] = _ECHOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoReply = _reflection.GeneratedProtocolMessageType('EchoReply', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREPLY,
  __module__ = 'Echo_pb2'
  # @@protoc_insertion_point(class_scope:EchoReply)
  ))
_sym_db.RegisterMessage(EchoReply)



_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='EchoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=72,
  serialized_end=121,
  methods=[
  _descriptor.MethodDescriptor(
    name='echo',
    full_name='EchoService.echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHOREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHOSERVICE)

DESCRIPTOR.services_by_name['EchoService'] = _ECHOSERVICE

# @@protoc_insertion_point(module_scope)
