

from pprint import pformat

import re
class ProcessStats(object):
    def __init__(self, pid=None, cpu=None, open_file_descriptors=None, memory=None, max_file_descriptors=None):
        """
        ProcessStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'pid': 'int', 'cpu': 'object', 'open_file_descriptors': 'int', 'memory': 'object', 'max_file_descriptors': 'int'}

        self.attribute_map = {'pid': 'pid', 'cpu': 'cpu', 'open_file_descriptors': 'open_file_descriptors', 'memory': 'memory', 'max_file_descriptors': 'max_file_descriptors'}

        self._pid = pid
        self._cpu = cpu
        self._open_file_descriptors = open_file_descriptors
        self._memory = memory
        self._max_file_descriptors = max_file_descriptors

    @property
    def pid(self):
        """
        Gets the pid of this ProcessStats. :return: The pid of this ProcessStats.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this ProcessStats. :param pid: The pid of this ProcessStats.
        :type: int
        """

        self._pid = pid

    @property
    def cpu(self):
        """
        Gets the cpu of this ProcessStats. :return: The cpu of this ProcessStats.
        :rtype: object
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this ProcessStats. :param cpu: The cpu of this ProcessStats.
        :type: object
        """

        self._cpu = cpu

    @property
    def open_file_descriptors(self):
        """
        Gets the open_file_descriptors of this ProcessStats. :return: The open_file_descriptors of this ProcessStats.
        :rtype: int
        """
        return self._open_file_descriptors

    @open_file_descriptors.setter
    def open_file_descriptors(self, open_file_descriptors):
        """
        Sets the open_file_descriptors of this ProcessStats. :param open_file_descriptors: The open_file_descriptors of this ProcessStats.
        :type: int
        """

        self._open_file_descriptors = open_file_descriptors

    @property
    def memory(self):
        """
        Gets the memory of this ProcessStats. :return: The memory of this ProcessStats.
        :rtype: object
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this ProcessStats. :param memory: The memory of this ProcessStats.
        :type: object
        """

        self._memory = memory

    @property
    def max_file_descriptors(self):
        """
        Gets the max_file_descriptors of this ProcessStats. :return: The max_file_descriptors of this ProcessStats.
        :rtype: int
        """
        return self._max_file_descriptors

    @max_file_descriptors.setter
    def max_file_descriptors(self, max_file_descriptors):
        """
        Sets the max_file_descriptors of this ProcessStats. :param max_file_descriptors: The max_file_descriptors of this ProcessStats.
        :type: int
        """

        self._max_file_descriptors = max_file_descriptors

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
