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
 * Autogenerated by Thrift Compiler (0.9.3)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef job_model_TYPES_H
#define job_model_TYPES_H

#include <iosfwd>

#include <thrift/Thrift.h>
#include <thrift/TApplicationException.h>
#include <thrift/protocol/TProtocol.h>
#include <thrift/transport/TTransport.h>

#include <thrift/cxxfunctional.h>
#include "status_models_types.h"


namespace apache { namespace airavata { namespace model { namespace job {

class JobModel;

typedef struct _JobModel__isset {
  _JobModel__isset() : creationTime(false), jobStatus(false), computeResourceConsumed(false), jobName(false), workingDir(false), stdOut(false), stdErr(false), exitCode(false) {}
  bool creationTime :1;
  bool jobStatus :1;
  bool computeResourceConsumed :1;
  bool jobName :1;
  bool workingDir :1;
  bool stdOut :1;
  bool stdErr :1;
  bool exitCode :1;
} _JobModel__isset;

class JobModel {
 public:

  JobModel(const JobModel&);
  JobModel& operator=(const JobModel&);
  JobModel() : jobId(), taskId(), processId(), jobDescription(), creationTime(0), computeResourceConsumed(), jobName(), workingDir(), stdOut(), stdErr(), exitCode(0) {
  }

  virtual ~JobModel() throw();
  std::string jobId;
  std::string taskId;
  std::string processId;
  std::string jobDescription;
  int64_t creationTime;
  std::vector< ::apache::airavata::model::status::JobStatus>  jobStatus;
  std::string computeResourceConsumed;
  std::string jobName;
  std::string workingDir;
  std::string stdOut;
  std::string stdErr;
  int32_t exitCode;

  _JobModel__isset __isset;

  void __set_jobId(const std::string& val);

  void __set_taskId(const std::string& val);

  void __set_processId(const std::string& val);

  void __set_jobDescription(const std::string& val);

  void __set_creationTime(const int64_t val);

  void __set_jobStatus(const std::vector< ::apache::airavata::model::status::JobStatus> & val);

  void __set_computeResourceConsumed(const std::string& val);

  void __set_jobName(const std::string& val);

  void __set_workingDir(const std::string& val);

  void __set_stdOut(const std::string& val);

  void __set_stdErr(const std::string& val);

  void __set_exitCode(const int32_t val);

  bool operator == (const JobModel & rhs) const
  {
    if (!(jobId == rhs.jobId))
      return false;
    if (!(taskId == rhs.taskId))
      return false;
    if (!(processId == rhs.processId))
      return false;
    if (!(jobDescription == rhs.jobDescription))
      return false;
    if (__isset.creationTime != rhs.__isset.creationTime)
      return false;
    else if (__isset.creationTime && !(creationTime == rhs.creationTime))
      return false;
    if (__isset.jobStatus != rhs.__isset.jobStatus)
      return false;
    else if (__isset.jobStatus && !(jobStatus == rhs.jobStatus))
      return false;
    if (__isset.computeResourceConsumed != rhs.__isset.computeResourceConsumed)
      return false;
    else if (__isset.computeResourceConsumed && !(computeResourceConsumed == rhs.computeResourceConsumed))
      return false;
    if (__isset.jobName != rhs.__isset.jobName)
      return false;
    else if (__isset.jobName && !(jobName == rhs.jobName))
      return false;
    if (__isset.workingDir != rhs.__isset.workingDir)
      return false;
    else if (__isset.workingDir && !(workingDir == rhs.workingDir))
      return false;
    if (__isset.stdOut != rhs.__isset.stdOut)
      return false;
    else if (__isset.stdOut && !(stdOut == rhs.stdOut))
      return false;
    if (__isset.stdErr != rhs.__isset.stdErr)
      return false;
    else if (__isset.stdErr && !(stdErr == rhs.stdErr))
      return false;
    if (__isset.exitCode != rhs.__isset.exitCode)
      return false;
    else if (__isset.exitCode && !(exitCode == rhs.exitCode))
      return false;
    return true;
  }
  bool operator != (const JobModel &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const JobModel & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  virtual void printTo(std::ostream& out) const;
};

void swap(JobModel &a, JobModel &b);

inline std::ostream& operator<<(std::ostream& out, const JobModel& obj)
{
  obj.printTo(out);
  return out;
}

}}}} // namespace

#endif
