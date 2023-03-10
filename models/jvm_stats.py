

from pprint import pformat

import re
class JvmStats(object):
    def __init__(self, start_time=None, class_path=None, spec_version=None, spec_vendor=None, mem=None, boot_class_path=None, version=None, garbage_collectors=None, vm_name=None, vm_version=None, vm_vendor=None, input_arguments=None, system_properties=None, memory_pools=None, spec_name=None):
        """
        JvmStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'start_time': 'int', 'class_path': 'str', 'spec_version': 'str', 'spec_vendor': 'str', 'mem': 'object', 'boot_class_path': 'str', 'version': 'str', 'garbage_collectors': 'list[str]', 'vm_name': 'str', 'vm_version': 'str', 'vm_vendor': 'str', 'input_arguments': 'list[str]', 'system_properties': 'object', 'memory_pools': 'list[str]', 'spec_name': 'str'}

        self.attribute_map = {'start_time': 'start_time', 'class_path': 'class_path', 'spec_version': 'spec_version', 'spec_vendor': 'spec_vendor', 'mem': 'mem', 'boot_class_path': 'boot_class_path', 'version': 'version', 'garbage_collectors': 'garbage_collectors', 'vm_name': 'vm_name', 'vm_version': 'vm_version', 'vm_vendor': 'vm_vendor', 'input_arguments': 'input_arguments', 'system_properties': 'system_properties', 'memory_pools': 'memory_pools', 'spec_name': 'spec_name'}

        self._start_time = start_time
        self._class_path = class_path
        self._spec_version = spec_version
        self._spec_vendor = spec_vendor
        self._mem = mem
        self._boot_class_path = boot_class_path
        self._version = version
        self._garbage_collectors = garbage_collectors
        self._vm_name = vm_name
        self._vm_version = vm_version
        self._vm_vendor = vm_vendor
        self._input_arguments = input_arguments
        self._system_properties = system_properties
        self._memory_pools = memory_pools
        self._spec_name = spec_name

    @property
    def start_time(self):
        """
        Gets the start_time of this JvmStats. :return: The start_time of this JvmStats.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this JvmStats. :param start_time: The start_time of this JvmStats.
        :type: int
        """

        self._start_time = start_time

    @property
    def class_path(self):
        """
        Gets the class_path of this JvmStats. :return: The class_path of this JvmStats.
        :rtype: str
        """
        return self._class_path

    @class_path.setter
    def class_path(self, class_path):
        """
        Sets the class_path of this JvmStats. :param class_path: The class_path of this JvmStats.
        :type: str
        """

        self._class_path = class_path

    @property
    def spec_version(self):
        """
        Gets the spec_version of this JvmStats. :return: The spec_version of this JvmStats.
        :rtype: str
        """
        return self._spec_version

    @spec_version.setter
    def spec_version(self, spec_version):
        """
        Sets the spec_version of this JvmStats. :param spec_version: The spec_version of this JvmStats.
        :type: str
        """

        self._spec_version = spec_version

    @property
    def spec_vendor(self):
        """
        Gets the spec_vendor of this JvmStats. :return: The spec_vendor of this JvmStats.
        :rtype: str
        """
        return self._spec_vendor

    @spec_vendor.setter
    def spec_vendor(self, spec_vendor):
        """
        Sets the spec_vendor of this JvmStats. :param spec_vendor: The spec_vendor of this JvmStats.
        :type: str
        """

        self._spec_vendor = spec_vendor

    @property
    def mem(self):
        """
        Gets the mem of this JvmStats. :return: The mem of this JvmStats.
        :rtype: object
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """
        Sets the mem of this JvmStats. :param mem: The mem of this JvmStats.
        :type: object
        """

        self._mem = mem

    @property
    def boot_class_path(self):
        """
        Gets the boot_class_path of this JvmStats. :return: The boot_class_path of this JvmStats.
        :rtype: str
        """
        return self._boot_class_path

    @boot_class_path.setter
    def boot_class_path(self, boot_class_path):
        """
        Sets the boot_class_path of this JvmStats. :param boot_class_path: The boot_class_path of this JvmStats.
        :type: str
        """

        self._boot_class_path = boot_class_path

    @property
    def version(self):
        """
        Gets the version of this JvmStats. :return: The version of this JvmStats.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this JvmStats. :param version: The version of this JvmStats.
        :type: str
        """

        self._version = version

    @property
    def garbage_collectors(self):
        """
        Gets the garbage_collectors of this JvmStats. :return: The garbage_collectors of this JvmStats.
        :rtype: list[str]
        """
        return self._garbage_collectors

    @garbage_collectors.setter
    def garbage_collectors(self, garbage_collectors):
        """
        Sets the garbage_collectors of this JvmStats. :param garbage_collectors: The garbage_collectors of this JvmStats.
        :type: list[str]
        """

        self._garbage_collectors = garbage_collectors

    @property
    def vm_name(self):
        """
        Gets the vm_name of this JvmStats. :return: The vm_name of this JvmStats.
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """
        Sets the vm_name of this JvmStats. :param vm_name: The vm_name of this JvmStats.
        :type: str
        """

        self._vm_name = vm_name

    @property
    def vm_version(self):
        """
        Gets the vm_version of this JvmStats. :return: The vm_version of this JvmStats.
        :rtype: str
        """
        return self._vm_version

    @vm_version.setter
    def vm_version(self, vm_version):
        """
        Sets the vm_version of this JvmStats. :param vm_version: The vm_version of this JvmStats.
        :type: str
        """

        self._vm_version = vm_version

    @property
    def vm_vendor(self):
        """
        Gets the vm_vendor of this JvmStats. :return: The vm_vendor of this JvmStats.
        :rtype: str
        """
        return self._vm_vendor

    @vm_vendor.setter
    def vm_vendor(self, vm_vendor):
        """
        Sets the vm_vendor of this JvmStats. :param vm_vendor: The vm_vendor of this JvmStats.
        :type: str
        """

        self._vm_vendor = vm_vendor

    @property
    def input_arguments(self):
        """
        Gets the input_arguments of this JvmStats. :return: The input_arguments of this JvmStats.
        :rtype: list[str]
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments):
        """
        Sets the input_arguments of this JvmStats. :param input_arguments: The input_arguments of this JvmStats.
        :type: list[str]
        """

        self._input_arguments = input_arguments

    @property
    def system_properties(self):
        """
        Gets the system_properties of this JvmStats. :return: The system_properties of this JvmStats.
        :rtype: object
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        """
        Sets the system_properties of this JvmStats. :param system_properties: The system_properties of this JvmStats.
        :type: object
        """

        self._system_properties = system_properties

    @property
    def memory_pools(self):
        """
        Gets the memory_pools of this JvmStats. :return: The memory_pools of this JvmStats.
        :rtype: list[str]
        """
        return self._memory_pools

    @memory_pools.setter
    def memory_pools(self, memory_pools):
        """
        Sets the memory_pools of this JvmStats. :param memory_pools: The memory_pools of this JvmStats.
        :type: list[str]
        """

        self._memory_pools = memory_pools

    @property
    def spec_name(self):
        """
        Gets the spec_name of this JvmStats. :return: The spec_name of this JvmStats.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        """
        Sets the spec_name of this JvmStats. :param spec_name: The spec_name of this JvmStats.
        :type: str
        """

        self._spec_name = spec_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr in self.swagger_types:
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
