/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Autogenerated by Thrift Compiler (0.9.2)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef task_model_TYPES_H
#define task_model_TYPES_H

#include <iosfwd>

#include <thrift/Thrift.h>
#include <thrift/TApplicationException.h>
#include <thrift/protocol/TProtocol.h>
#include <thrift/transport/TTransport.h>

#include <thrift/cxxfunctional.h>
#include "airavata_commons_types.h"
#include "status_models_types.h"


namespace apache { namespace airavata { namespace model { namespace task {

struct TaskTypes {
  enum type {
    ENV_SETUP = 0,
    DATA_STAGING = 1,
    JOB_SUBMISSION = 2,
    ENV_CLEANUP = 3,
    MONITORING = 4
  };
};

extern const std::map<int, const char*> _TaskTypes_VALUES_TO_NAMES;

class TaskModel;

class DataStagingTaskModel;

typedef struct _TaskModel__isset {
  _TaskModel__isset() : taskDetail(false), subTaskModel(false), taskError(false) {}
  bool taskDetail :1;
  bool subTaskModel :1;
  bool taskError :1;
} _TaskModel__isset;

class TaskModel {
 public:

  static const char* ascii_fingerprint; // = "CE3A1BEFC350140F2B4D2EF1424A7C4F";
  static const uint8_t binary_fingerprint[16]; // = {0xCE,0x3A,0x1B,0xEF,0xC3,0x50,0x14,0x0F,0x2B,0x4D,0x2E,0xF1,0x42,0x4A,0x7C,0x4F};

  TaskModel(const TaskModel&);
  TaskModel& operator=(const TaskModel&);
  TaskModel() : taskId("DO_NOT_SET_AT_CLIENTS"), taskType((TaskTypes::type)0), parentProcessId(), creationTime(0), lastUpdateTime(0), taskDetail(), subTaskModel() {
  }

  virtual ~TaskModel() throw();
  std::string taskId;
  TaskTypes::type taskType;
  std::string parentProcessId;
  int64_t creationTime;
  int64_t lastUpdateTime;
   ::apache::airavata::model::status::TaskStatus taskStatus;
  std::string taskDetail;
  std::string subTaskModel;
   ::apache::airavata::model::commons::ErrorModel taskError;

  _TaskModel__isset __isset;

  void __set_taskId(const std::string& val);

  void __set_taskType(const TaskTypes::type val);

  void __set_parentProcessId(const std::string& val);

  void __set_creationTime(const int64_t val);

  void __set_lastUpdateTime(const int64_t val);

  void __set_taskStatus(const  ::apache::airavata::model::status::TaskStatus& val);

  void __set_taskDetail(const std::string& val);

  void __set_subTaskModel(const std::string& val);

  void __set_taskError(const  ::apache::airavata::model::commons::ErrorModel& val);

  bool operator == (const TaskModel & rhs) const
  {
    if (!(taskId == rhs.taskId))
      return false;
    if (!(taskType == rhs.taskType))
      return false;
    if (!(parentProcessId == rhs.parentProcessId))
      return false;
    if (!(creationTime == rhs.creationTime))
      return false;
    if (!(lastUpdateTime == rhs.lastUpdateTime))
      return false;
    if (!(taskStatus == rhs.taskStatus))
      return false;
    if (__isset.taskDetail != rhs.__isset.taskDetail)
      return false;
    else if (__isset.taskDetail && !(taskDetail == rhs.taskDetail))
      return false;
    if (__isset.subTaskModel != rhs.__isset.subTaskModel)
      return false;
    else if (__isset.subTaskModel && !(subTaskModel == rhs.subTaskModel))
      return false;
    if (__isset.taskError != rhs.__isset.taskError)
      return false;
    else if (__isset.taskError && !(taskError == rhs.taskError))
      return false;
    return true;
  }
  bool operator != (const TaskModel &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const TaskModel & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  friend std::ostream& operator<<(std::ostream& out, const TaskModel& obj);
};

void swap(TaskModel &a, TaskModel &b);

typedef struct _DataStagingTaskModel__isset {
  _DataStagingTaskModel__isset() : transferStartTime(false), transferEndTime(false), transferRate(false) {}
  bool transferStartTime :1;
  bool transferEndTime :1;
  bool transferRate :1;
} _DataStagingTaskModel__isset;

class DataStagingTaskModel {
 public:

  static const char* ascii_fingerprint; // = "3224DD8D1EC3134AB6350703A4B92D60";
  static const uint8_t binary_fingerprint[16]; // = {0x32,0x24,0xDD,0x8D,0x1E,0xC3,0x13,0x4A,0xB6,0x35,0x07,0x03,0xA4,0xB9,0x2D,0x60};

  DataStagingTaskModel(const DataStagingTaskModel&);
  DataStagingTaskModel& operator=(const DataStagingTaskModel&);
  DataStagingTaskModel() : source(), destination(), transferStartTime(0), transferEndTime(0), transferRate() {
  }

  virtual ~DataStagingTaskModel() throw();
  std::string source;
  std::string destination;
  int64_t transferStartTime;
  int64_t transferEndTime;
  std::string transferRate;

  _DataStagingTaskModel__isset __isset;

  void __set_source(const std::string& val);

  void __set_destination(const std::string& val);

  void __set_transferStartTime(const int64_t val);

  void __set_transferEndTime(const int64_t val);

  void __set_transferRate(const std::string& val);

  bool operator == (const DataStagingTaskModel & rhs) const
  {
    if (!(source == rhs.source))
      return false;
    if (!(destination == rhs.destination))
      return false;
    if (__isset.transferStartTime != rhs.__isset.transferStartTime)
      return false;
    else if (__isset.transferStartTime && !(transferStartTime == rhs.transferStartTime))
      return false;
    if (__isset.transferEndTime != rhs.__isset.transferEndTime)
      return false;
    else if (__isset.transferEndTime && !(transferEndTime == rhs.transferEndTime))
      return false;
    if (__isset.transferRate != rhs.__isset.transferRate)
      return false;
    else if (__isset.transferRate && !(transferRate == rhs.transferRate))
      return false;
    return true;
  }
  bool operator != (const DataStagingTaskModel &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const DataStagingTaskModel & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  friend std::ostream& operator<<(std::ostream& out, const DataStagingTaskModel& obj);
};

void swap(DataStagingTaskModel &a, DataStagingTaskModel &b);

}}}} // namespace

#endif
