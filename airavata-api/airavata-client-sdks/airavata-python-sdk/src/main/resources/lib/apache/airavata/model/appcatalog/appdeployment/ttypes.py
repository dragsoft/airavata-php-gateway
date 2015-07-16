#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import apache.airavata.model.commons.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ApplicationParallelismType:
  """
  Enumeration of application parallelism supported by Airavata

  SERIAL:
   Single processor applications without any parallelization.

  MPI:
   Messaging Passing Interface.

  OPENMP:
   Shared Memory Implementtaion.

  OPENMP_MPI:
   Hybrid Applications.

  """
  SERIAL = 0
  MPI = 1
  OPENMP = 2
  OPENMP_MPI = 3

  _VALUES_TO_NAMES = {
    0: "SERIAL",
    1: "MPI",
    2: "OPENMP",
    3: "OPENMP_MPI",
  }

  _NAMES_TO_VALUES = {
    "SERIAL": 0,
    "MPI": 1,
    "OPENMP": 2,
    "OPENMP_MPI": 3,
  }


class SetEnvPaths:
  """
  Key Value pairs to be used to set environments

  name:
    Name of the environment variable such as PATH, LD_LIBRARY_PATH, NETCDF_HOME.

  value:
    Value of the environment variable to set

  Attributes:
   - name
   - value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'value', None, None, ), # 2
  )

  def __init__(self, name=None, value=None,):
    self.name = name
    self.value = value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SetEnvPaths')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 2)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.value is None:
      raise TProtocol.TProtocolException(message='Required field value is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.value)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ApplicationModule:
  """
  Application Module Information. A module has to be registered before registering a deployment.

  appModuleId: Airavata Internal Unique Job ID. This is set by the registry.

  appModuleName:
    Name of the application module.

  appModuleVersion:
    Version of the application.

  appModuleDescription:
     Descriprion of the Module


  Attributes:
   - appModuleId
   - appModuleName
   - appModuleVersion
   - appModuleDescription
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'appModuleId', None, "DO_NOT_SET_AT_CLIENTS", ), # 1
    (2, TType.STRING, 'appModuleName', None, None, ), # 2
    (3, TType.STRING, 'appModuleVersion', None, None, ), # 3
    (4, TType.STRING, 'appModuleDescription', None, None, ), # 4
  )

  def __init__(self, appModuleId=thrift_spec[1][4], appModuleName=None, appModuleVersion=None, appModuleDescription=None,):
    self.appModuleId = appModuleId
    self.appModuleName = appModuleName
    self.appModuleVersion = appModuleVersion
    self.appModuleDescription = appModuleDescription

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.appModuleId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.appModuleName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.appModuleVersion = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.appModuleDescription = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ApplicationModule')
    if self.appModuleId is not None:
      oprot.writeFieldBegin('appModuleId', TType.STRING, 1)
      oprot.writeString(self.appModuleId)
      oprot.writeFieldEnd()
    if self.appModuleName is not None:
      oprot.writeFieldBegin('appModuleName', TType.STRING, 2)
      oprot.writeString(self.appModuleName)
      oprot.writeFieldEnd()
    if self.appModuleVersion is not None:
      oprot.writeFieldBegin('appModuleVersion', TType.STRING, 3)
      oprot.writeString(self.appModuleVersion)
      oprot.writeFieldEnd()
    if self.appModuleDescription is not None:
      oprot.writeFieldBegin('appModuleDescription', TType.STRING, 4)
      oprot.writeString(self.appModuleDescription)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.appModuleId is None:
      raise TProtocol.TProtocolException(message='Required field appModuleId is unset!')
    if self.appModuleName is None:
      raise TProtocol.TProtocolException(message='Required field appModuleName is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appModuleId)
    value = (value * 31) ^ hash(self.appModuleName)
    value = (value * 31) ^ hash(self.appModuleVersion)
    value = (value * 31) ^ hash(self.appModuleDescription)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ApplicationDeploymentDescription:
  """
  Application Deployment Description

  appDeploymentId: Airavata Internal Unique Job ID. This is set by the registry.

  appModuleName:
    Application Module Name. This has to be precise describing the binary.

  computeHostId:
    This ID maps application deployment to a particular resource previously described within Airavata.
    Example: Stampede is first registered and refered when registering WRF.

  moduleLoadCmd:
   Command string to load modules. This will be placed in the job submisison
   Ex: module load amber

  libPrependPaths:
   prepend to a path variable the value

  libAppendPaths:
   append to a path variable the value

  setEnvironment:
   assigns to the environment variable "NAME" the value


  Attributes:
   - appDeploymentId
   - appModuleId
   - computeHostId
   - executablePath
   - parallelism
   - appDeploymentDescription
   - moduleLoadCmds
   - libPrependPaths
   - libAppendPaths
   - setEnvironment
   - preJobCommands
   - postJobCommands
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'appDeploymentId', None, "DO_NOT_SET_AT_CLIENTS", ), # 1
    (2, TType.STRING, 'appModuleId', None, None, ), # 2
    (3, TType.STRING, 'computeHostId', None, None, ), # 3
    (4, TType.STRING, 'executablePath', None, None, ), # 4
    (5, TType.I32, 'parallelism', None,     0, ), # 5
    (6, TType.STRING, 'appDeploymentDescription', None, None, ), # 6
    (7, TType.LIST, 'moduleLoadCmds', (TType.STRING,None), None, ), # 7
    (8, TType.LIST, 'libPrependPaths', (TType.STRUCT,(SetEnvPaths, SetEnvPaths.thrift_spec)), None, ), # 8
    (9, TType.LIST, 'libAppendPaths', (TType.STRUCT,(SetEnvPaths, SetEnvPaths.thrift_spec)), None, ), # 9
    (10, TType.LIST, 'setEnvironment', (TType.STRUCT,(SetEnvPaths, SetEnvPaths.thrift_spec)), None, ), # 10
    (11, TType.LIST, 'preJobCommands', (TType.STRING,None), None, ), # 11
    (12, TType.LIST, 'postJobCommands', (TType.STRING,None), None, ), # 12
  )

  def __init__(self, appDeploymentId=thrift_spec[1][4], appModuleId=None, computeHostId=None, executablePath=None, parallelism=thrift_spec[5][4], appDeploymentDescription=None, moduleLoadCmds=None, libPrependPaths=None, libAppendPaths=None, setEnvironment=None, preJobCommands=None, postJobCommands=None,):
    self.appDeploymentId = appDeploymentId
    self.appModuleId = appModuleId
    self.computeHostId = computeHostId
    self.executablePath = executablePath
    self.parallelism = parallelism
    self.appDeploymentDescription = appDeploymentDescription
    self.moduleLoadCmds = moduleLoadCmds
    self.libPrependPaths = libPrependPaths
    self.libAppendPaths = libAppendPaths
    self.setEnvironment = setEnvironment
    self.preJobCommands = preJobCommands
    self.postJobCommands = postJobCommands

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.appDeploymentId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.appModuleId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.computeHostId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.executablePath = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.parallelism = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.appDeploymentDescription = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.moduleLoadCmds = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.moduleLoadCmds.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.libPrependPaths = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = SetEnvPaths()
            _elem11.read(iprot)
            self.libPrependPaths.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.libAppendPaths = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = SetEnvPaths()
            _elem17.read(iprot)
            self.libAppendPaths.append(_elem17)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.LIST:
          self.setEnvironment = []
          (_etype21, _size18) = iprot.readListBegin()
          for _i22 in xrange(_size18):
            _elem23 = SetEnvPaths()
            _elem23.read(iprot)
            self.setEnvironment.append(_elem23)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.LIST:
          self.preJobCommands = []
          (_etype27, _size24) = iprot.readListBegin()
          for _i28 in xrange(_size24):
            _elem29 = iprot.readString();
            self.preJobCommands.append(_elem29)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.LIST:
          self.postJobCommands = []
          (_etype33, _size30) = iprot.readListBegin()
          for _i34 in xrange(_size30):
            _elem35 = iprot.readString();
            self.postJobCommands.append(_elem35)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ApplicationDeploymentDescription')
    if self.appDeploymentId is not None:
      oprot.writeFieldBegin('appDeploymentId', TType.STRING, 1)
      oprot.writeString(self.appDeploymentId)
      oprot.writeFieldEnd()
    if self.appModuleId is not None:
      oprot.writeFieldBegin('appModuleId', TType.STRING, 2)
      oprot.writeString(self.appModuleId)
      oprot.writeFieldEnd()
    if self.computeHostId is not None:
      oprot.writeFieldBegin('computeHostId', TType.STRING, 3)
      oprot.writeString(self.computeHostId)
      oprot.writeFieldEnd()
    if self.executablePath is not None:
      oprot.writeFieldBegin('executablePath', TType.STRING, 4)
      oprot.writeString(self.executablePath)
      oprot.writeFieldEnd()
    if self.parallelism is not None:
      oprot.writeFieldBegin('parallelism', TType.I32, 5)
      oprot.writeI32(self.parallelism)
      oprot.writeFieldEnd()
    if self.appDeploymentDescription is not None:
      oprot.writeFieldBegin('appDeploymentDescription', TType.STRING, 6)
      oprot.writeString(self.appDeploymentDescription)
      oprot.writeFieldEnd()
    if self.moduleLoadCmds is not None:
      oprot.writeFieldBegin('moduleLoadCmds', TType.LIST, 7)
      oprot.writeListBegin(TType.STRING, len(self.moduleLoadCmds))
      for iter36 in self.moduleLoadCmds:
        oprot.writeString(iter36)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.libPrependPaths is not None:
      oprot.writeFieldBegin('libPrependPaths', TType.LIST, 8)
      oprot.writeListBegin(TType.STRUCT, len(self.libPrependPaths))
      for iter37 in self.libPrependPaths:
        iter37.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.libAppendPaths is not None:
      oprot.writeFieldBegin('libAppendPaths', TType.LIST, 9)
      oprot.writeListBegin(TType.STRUCT, len(self.libAppendPaths))
      for iter38 in self.libAppendPaths:
        iter38.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.setEnvironment is not None:
      oprot.writeFieldBegin('setEnvironment', TType.LIST, 10)
      oprot.writeListBegin(TType.STRUCT, len(self.setEnvironment))
      for iter39 in self.setEnvironment:
        iter39.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.preJobCommands is not None:
      oprot.writeFieldBegin('preJobCommands', TType.LIST, 11)
      oprot.writeListBegin(TType.STRING, len(self.preJobCommands))
      for iter40 in self.preJobCommands:
        oprot.writeString(iter40)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.postJobCommands is not None:
      oprot.writeFieldBegin('postJobCommands', TType.LIST, 12)
      oprot.writeListBegin(TType.STRING, len(self.postJobCommands))
      for iter41 in self.postJobCommands:
        oprot.writeString(iter41)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.appDeploymentId is None:
      raise TProtocol.TProtocolException(message='Required field appDeploymentId is unset!')
    if self.appModuleId is None:
      raise TProtocol.TProtocolException(message='Required field appModuleId is unset!')
    if self.computeHostId is None:
      raise TProtocol.TProtocolException(message='Required field computeHostId is unset!')
    if self.executablePath is None:
      raise TProtocol.TProtocolException(message='Required field executablePath is unset!')
    if self.parallelism is None:
      raise TProtocol.TProtocolException(message='Required field parallelism is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appDeploymentId)
    value = (value * 31) ^ hash(self.appModuleId)
    value = (value * 31) ^ hash(self.computeHostId)
    value = (value * 31) ^ hash(self.executablePath)
    value = (value * 31) ^ hash(self.parallelism)
    value = (value * 31) ^ hash(self.appDeploymentDescription)
    value = (value * 31) ^ hash(self.moduleLoadCmds)
    value = (value * 31) ^ hash(self.libPrependPaths)
    value = (value * 31) ^ hash(self.libAppendPaths)
    value = (value * 31) ^ hash(self.setEnvironment)
    value = (value * 31) ^ hash(self.preJobCommands)
    value = (value * 31) ^ hash(self.postJobCommands)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
