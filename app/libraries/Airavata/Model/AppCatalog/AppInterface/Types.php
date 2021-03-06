<?php
namespace Airavata\Model\AppCatalog\AppInterface;

/**
 * Autogenerated by Thrift Compiler (0.9.3)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
use Thrift\Base\TBase;
use Thrift\Type\TType;
use Thrift\Type\TMessageType;
use Thrift\Exception\TException;
use Thrift\Exception\TProtocolException;
use Thrift\Protocol\TProtocol;
use Thrift\Protocol\TBinaryProtocolAccelerated;
use Thrift\Exception\TApplicationException;


/**
 * Application Interface Description
 * 
 * applicationModules:
 *   Associate all application modules with versions which interface is applicable to.
 * 
 * applicationInputs:
 *   Inputs to be passed to the application
 * 
 * applicationOutputs:
 *   Outputs generated from the application
 * 
 */
class ApplicationInterfaceDescription {
  static $_TSPEC;

  /**
   * @var string
   */
  public $applicationInterfaceId = "DO_NOT_SET_AT_CLIENTS";
  /**
   * @var string
   */
  public $applicationName = null;
  /**
   * @var string
   */
  public $applicationDescription = null;
  /**
   * @var string[]
   */
  public $applicationModules = null;
  /**
   * @var \Airavata\Model\Application\Io\InputDataObjectType[]
   */
  public $applicationInputs = null;
  /**
   * @var \Airavata\Model\Application\Io\OutputDataObjectType[]
   */
  public $applicationOutputs = null;
  /**
   * @var bool
   */
  public $archiveWorkingDirectory = false;
  /**
   * @var bool
   */
  public $hasOptionalFileInputs = null;

  public function __construct($vals=null) {
    if (!isset(self::$_TSPEC)) {
      self::$_TSPEC = array(
        1 => array(
          'var' => 'applicationInterfaceId',
          'type' => TType::STRING,
          ),
        2 => array(
          'var' => 'applicationName',
          'type' => TType::STRING,
          ),
        3 => array(
          'var' => 'applicationDescription',
          'type' => TType::STRING,
          ),
        4 => array(
          'var' => 'applicationModules',
          'type' => TType::LST,
          'etype' => TType::STRING,
          'elem' => array(
            'type' => TType::STRING,
            ),
          ),
        5 => array(
          'var' => 'applicationInputs',
          'type' => TType::LST,
          'etype' => TType::STRUCT,
          'elem' => array(
            'type' => TType::STRUCT,
            'class' => '\Airavata\Model\Application\Io\InputDataObjectType',
            ),
          ),
        6 => array(
          'var' => 'applicationOutputs',
          'type' => TType::LST,
          'etype' => TType::STRUCT,
          'elem' => array(
            'type' => TType::STRUCT,
            'class' => '\Airavata\Model\Application\Io\OutputDataObjectType',
            ),
          ),
        7 => array(
          'var' => 'archiveWorkingDirectory',
          'type' => TType::BOOL,
          ),
        8 => array(
          'var' => 'hasOptionalFileInputs',
          'type' => TType::BOOL,
          ),
        );
    }
    if (is_array($vals)) {
      if (isset($vals['applicationInterfaceId'])) {
        $this->applicationInterfaceId = $vals['applicationInterfaceId'];
      }
      if (isset($vals['applicationName'])) {
        $this->applicationName = $vals['applicationName'];
      }
      if (isset($vals['applicationDescription'])) {
        $this->applicationDescription = $vals['applicationDescription'];
      }
      if (isset($vals['applicationModules'])) {
        $this->applicationModules = $vals['applicationModules'];
      }
      if (isset($vals['applicationInputs'])) {
        $this->applicationInputs = $vals['applicationInputs'];
      }
      if (isset($vals['applicationOutputs'])) {
        $this->applicationOutputs = $vals['applicationOutputs'];
      }
      if (isset($vals['archiveWorkingDirectory'])) {
        $this->archiveWorkingDirectory = $vals['archiveWorkingDirectory'];
      }
      if (isset($vals['hasOptionalFileInputs'])) {
        $this->hasOptionalFileInputs = $vals['hasOptionalFileInputs'];
      }
    }
  }

  public function getName() {
    return 'ApplicationInterfaceDescription';
  }

  public function read($input)
  {
    $xfer = 0;
    $fname = null;
    $ftype = 0;
    $fid = 0;
    $xfer += $input->readStructBegin($fname);
    while (true)
    {
      $xfer += $input->readFieldBegin($fname, $ftype, $fid);
      if ($ftype == TType::STOP) {
        break;
      }
      switch ($fid)
      {
        case 1:
          if ($ftype == TType::STRING) {
            $xfer += $input->readString($this->applicationInterfaceId);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 2:
          if ($ftype == TType::STRING) {
            $xfer += $input->readString($this->applicationName);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 3:
          if ($ftype == TType::STRING) {
            $xfer += $input->readString($this->applicationDescription);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 4:
          if ($ftype == TType::LST) {
            $this->applicationModules = array();
            $_size0 = 0;
            $_etype3 = 0;
            $xfer += $input->readListBegin($_etype3, $_size0);
            for ($_i4 = 0; $_i4 < $_size0; ++$_i4)
            {
              $elem5 = null;
              $xfer += $input->readString($elem5);
              $this->applicationModules []= $elem5;
            }
            $xfer += $input->readListEnd();
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 5:
          if ($ftype == TType::LST) {
            $this->applicationInputs = array();
            $_size6 = 0;
            $_etype9 = 0;
            $xfer += $input->readListBegin($_etype9, $_size6);
            for ($_i10 = 0; $_i10 < $_size6; ++$_i10)
            {
              $elem11 = null;
              $elem11 = new \Airavata\Model\Application\Io\InputDataObjectType();
              $xfer += $elem11->read($input);
              $this->applicationInputs []= $elem11;
            }
            $xfer += $input->readListEnd();
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 6:
          if ($ftype == TType::LST) {
            $this->applicationOutputs = array();
            $_size12 = 0;
            $_etype15 = 0;
            $xfer += $input->readListBegin($_etype15, $_size12);
            for ($_i16 = 0; $_i16 < $_size12; ++$_i16)
            {
              $elem17 = null;
              $elem17 = new \Airavata\Model\Application\Io\OutputDataObjectType();
              $xfer += $elem17->read($input);
              $this->applicationOutputs []= $elem17;
            }
            $xfer += $input->readListEnd();
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 7:
          if ($ftype == TType::BOOL) {
            $xfer += $input->readBool($this->archiveWorkingDirectory);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 8:
          if ($ftype == TType::BOOL) {
            $xfer += $input->readBool($this->hasOptionalFileInputs);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        default:
          $xfer += $input->skip($ftype);
          break;
      }
      $xfer += $input->readFieldEnd();
    }
    $xfer += $input->readStructEnd();
    return $xfer;
  }

  public function write($output) {
    $xfer = 0;
    $xfer += $output->writeStructBegin('ApplicationInterfaceDescription');
    if ($this->applicationInterfaceId !== null) {
      $xfer += $output->writeFieldBegin('applicationInterfaceId', TType::STRING, 1);
      $xfer += $output->writeString($this->applicationInterfaceId);
      $xfer += $output->writeFieldEnd();
    }
    if ($this->applicationName !== null) {
      $xfer += $output->writeFieldBegin('applicationName', TType::STRING, 2);
      $xfer += $output->writeString($this->applicationName);
      $xfer += $output->writeFieldEnd();
    }
    if ($this->applicationDescription !== null) {
      $xfer += $output->writeFieldBegin('applicationDescription', TType::STRING, 3);
      $xfer += $output->writeString($this->applicationDescription);
      $xfer += $output->writeFieldEnd();
    }
    if ($this->applicationModules !== null) {
      if (!is_array($this->applicationModules)) {
        throw new TProtocolException('Bad type in structure.', TProtocolException::INVALID_DATA);
      }
      $xfer += $output->writeFieldBegin('applicationModules', TType::LST, 4);
      {
        $output->writeListBegin(TType::STRING, count($this->applicationModules));
        {
          foreach ($this->applicationModules as $iter18)
          {
            $xfer += $output->writeString($iter18);
          }
        }
        $output->writeListEnd();
      }
      $xfer += $output->writeFieldEnd();
    }
    if ($this->applicationInputs !== null) {
      if (!is_array($this->applicationInputs)) {
        throw new TProtocolException('Bad type in structure.', TProtocolException::INVALID_DATA);
      }
      $xfer += $output->writeFieldBegin('applicationInputs', TType::LST, 5);
      {
        $output->writeListBegin(TType::STRUCT, count($this->applicationInputs));
        {
          foreach ($this->applicationInputs as $iter19)
          {
            $xfer += $iter19->write($output);
          }
        }
        $output->writeListEnd();
      }
      $xfer += $output->writeFieldEnd();
    }
    if ($this->applicationOutputs !== null) {
      if (!is_array($this->applicationOutputs)) {
        throw new TProtocolException('Bad type in structure.', TProtocolException::INVALID_DATA);
      }
      $xfer += $output->writeFieldBegin('applicationOutputs', TType::LST, 6);
      {
        $output->writeListBegin(TType::STRUCT, count($this->applicationOutputs));
        {
          foreach ($this->applicationOutputs as $iter20)
          {
            $xfer += $iter20->write($output);
          }
        }
        $output->writeListEnd();
      }
      $xfer += $output->writeFieldEnd();
    }
    if ($this->archiveWorkingDirectory !== null) {
      $xfer += $output->writeFieldBegin('archiveWorkingDirectory', TType::BOOL, 7);
      $xfer += $output->writeBool($this->archiveWorkingDirectory);
      $xfer += $output->writeFieldEnd();
    }
    if ($this->hasOptionalFileInputs !== null) {
      $xfer += $output->writeFieldBegin('hasOptionalFileInputs', TType::BOOL, 8);
      $xfer += $output->writeBool($this->hasOptionalFileInputs);
      $xfer += $output->writeFieldEnd();
    }
    $xfer += $output->writeFieldStop();
    $xfer += $output->writeStructEnd();
    return $xfer;
  }

}


