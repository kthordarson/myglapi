

from pprint import pformat

import re
class SystemJVMResponse(object):
    def __init__(self, free_memory=None, max_memory=None, total_memory=None, used_memory=None, node_id=None, pid=None, info=None):
        """
        SystemJVMResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'free_memory': 'object', 'max_memory': 'object', 'total_memory': 'object', 'used_memory': 'object', 'node_id': 'str', 'pid': 'str', 'info': 'str'}

        self.attribute_map = {'free_memory': 'free_memory', 'max_memory': 'max_memory', 'total_memory': 'total_memory', 'used_memory': 'used_memory', 'node_id': 'node_id', 'pid': 'pid', 'info': 'info'}

        self._free_memory = free_memory
        self._max_memory = max_memory
        self._total_memory = total_memory
        self._used_memory = used_memory
        self._node_id = node_id
        self._pid = pid
        self._info = info

    @property
    def free_memory(self):
        """
        Gets the free_memory of this SystemJVMResponse. :return: The free_memory of this SystemJVMResponse.
        :rtype: object
        """
        return self._free_memory

    @free_memory.setter
    def free_memory(self, free_memory):
        """
        Sets the free_memory of this SystemJVMResponse. :param free_memory: The free_memory of this SystemJVMResponse.
        :type: object
        """

        self._free_memory = free_memory

    @property
    def max_memory(self):
        """
        Gets the max_memory of this SystemJVMResponse. :return: The max_memory of this SystemJVMResponse.
        :rtype: object
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """
        Sets the max_memory of this SystemJVMResponse. :param max_memory: The max_memory of this SystemJVMResponse.
        :type: object
        """

        self._max_memory = max_memory

    @property
    def total_memory(self):
        """
        Gets the total_memory of this SystemJVMResponse. :return: The total_memory of this SystemJVMResponse.
        :rtype: object
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """
        Sets the total_memory of this SystemJVMResponse. :param total_memory: The total_memory of this SystemJVMResponse.
        :type: object
        """

        self._total_memory = total_memory

    @property
    def used_memory(self):
        """
        Gets the used_memory of this SystemJVMResponse. :return: The used_memory of this SystemJVMResponse.
        :rtype: object
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        """
        Sets the used_memory of this SystemJVMResponse. :param used_memory: The used_memory of this SystemJVMResponse.
        :type: object
        """

        self._used_memory = used_memory

    @property
    def node_id(self):
        """
        Gets the node_id of this SystemJVMResponse. :return: The node_id of this SystemJVMResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this SystemJVMResponse. :param node_id: The node_id of this SystemJVMResponse.
        :type: str
        """

        self._node_id = node_id

    @property
    def pid(self):
        """
        Gets the pid of this SystemJVMResponse. :return: The pid of this SystemJVMResponse.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this SystemJVMResponse. :param pid: The pid of this SystemJVMResponse.
        :type: str
        """

        self._pid = pid

    @property
    def info(self):
        """
        Gets the info of this SystemJVMResponse. :return: The info of this SystemJVMResponse.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this SystemJVMResponse. :param info: The info of this SystemJVMResponse.
        :type: str
        """

        self._info = info

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
