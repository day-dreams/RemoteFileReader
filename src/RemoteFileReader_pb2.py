# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RemoteFileReader.proto

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
  name='RemoteFileReader.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x16RemoteFileReader.proto\"\x18\n\x08\x46ileLine\x12\x0c\n\x04line\x18\x01 \x01(\t\"Z\n\nFileStatus\x12\x12\n\nfile_exits\x18\x01 \x01(\x08\x12\x1a\n\x12last_modified_time\x18\x03 \x01(\t\x12\x16\n\x0elogic_filename\x18\x04 \x01(\tJ\x04\x08\x02\x10\x03\"$\n\x04\x46ile\x12\x16\n\x0elogic_filename\x18\x02 \x01(\tJ\x04\x08\x01\x10\x02\"\x0e\n\x0c\x45mptyRequest2\x88\x01\n\x18RemoteFileRreaderService\x12\x1c\n\x06\x65xists\x12\x05.File\x1a\x0b.FileStatus\x12\x1a\n\x04read\x12\x05.File\x1a\t.FileLine0\x01\x12\x32\n\x12get_all_filestatus\x12\r.EmptyRequest\x1a\x0b.FileStatus0\x01\x62\x06proto3')
)




_FILELINE = _descriptor.Descriptor(
  name='FileLine',
  full_name='FileLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='FileLine.line', index=0,
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
  serialized_start=26,
  serialized_end=50,
)


_FILESTATUS = _descriptor.Descriptor(
  name='FileStatus',
  full_name='FileStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_exits', full_name='FileStatus.file_exits', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_modified_time', full_name='FileStatus.last_modified_time', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logic_filename', full_name='FileStatus.logic_filename', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=52,
  serialized_end=142,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logic_filename', full_name='File.logic_filename', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=144,
  serialized_end=180,
)


_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=182,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['FileLine'] = _FILELINE
DESCRIPTOR.message_types_by_name['FileStatus'] = _FILESTATUS
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileLine = _reflection.GeneratedProtocolMessageType('FileLine', (_message.Message,), dict(
  DESCRIPTOR = _FILELINE,
  __module__ = 'RemoteFileReader_pb2'
  # @@protoc_insertion_point(class_scope:FileLine)
  ))
_sym_db.RegisterMessage(FileLine)

FileStatus = _reflection.GeneratedProtocolMessageType('FileStatus', (_message.Message,), dict(
  DESCRIPTOR = _FILESTATUS,
  __module__ = 'RemoteFileReader_pb2'
  # @@protoc_insertion_point(class_scope:FileStatus)
  ))
_sym_db.RegisterMessage(FileStatus)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'RemoteFileReader_pb2'
  # @@protoc_insertion_point(class_scope:File)
  ))
_sym_db.RegisterMessage(File)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'RemoteFileReader_pb2'
  # @@protoc_insertion_point(class_scope:EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)



_REMOTEFILERREADERSERVICE = _descriptor.ServiceDescriptor(
  name='RemoteFileRreaderService',
  full_name='RemoteFileRreaderService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=199,
  serialized_end=335,
  methods=[
  _descriptor.MethodDescriptor(
    name='exists',
    full_name='RemoteFileRreaderService.exists',
    index=0,
    containing_service=None,
    input_type=_FILE,
    output_type=_FILESTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='read',
    full_name='RemoteFileRreaderService.read',
    index=1,
    containing_service=None,
    input_type=_FILE,
    output_type=_FILELINE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_all_filestatus',
    full_name='RemoteFileRreaderService.get_all_filestatus',
    index=2,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_FILESTATUS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REMOTEFILERREADERSERVICE)

DESCRIPTOR.services_by_name['RemoteFileRreaderService'] = _REMOTEFILERREADERSERVICE

# @@protoc_insertion_point(module_scope)
