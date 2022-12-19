

from pprint import pformat

import re
class SystemStats(object):
    def __init__(self, os=None, jvm=None, process=None, network=None, fs=None):
        """
        SystemStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'os': 'object', 'jvm': 'object', 'process': 'object', 'network': 'object', 'fs': 'object'}

        self.attribute_map = {'os': 'os', 'jvm': 'jvm', 'process': 'process', 'network': 'network', 'fs': 'fs'}

        self._os = os
        self._jvm = jvm
        self._process = process
        self._network = network
        self._fs = fs

    @property
    def os(self):
        """
        Gets the os of this SystemStats.        :return: The os of this SystemStats.
        :rtype: object
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this SystemStats.        :param os: The os of this SystemStats.
        :type: object
        """

        self._os = os

    @property
    def jvm(self):
        """
        Gets the jvm of this SystemStats.        :return: The jvm of this SystemStats.
        :rtype: object
        """
        return self._jvm

    @jvm.setter
    def jvm(self, jvm):
        """
        Sets the jvm of this SystemStats.        :param jvm: The jvm of this SystemStats.
        :type: object
        """

        self._jvm = jvm

    @property
    def process(self):
        """
        Gets the process of this SystemStats.        :return: The process of this SystemStats.
        :rtype: object
        """
        return self._process

    @process.setter
    def process(self, process):
        """
        Sets the process of this SystemStats.        :param process: The process of this SystemStats.
        :type: object
        """

        self._process = process

    @property
    def network(self):
        """
        Gets the network of this SystemStats.        :return: The network of this SystemStats.
        :rtype: object
        """
        return self._network

    @network.setter
    def network(self, network):
        """
        Sets the network of this SystemStats.        :param network: The network of this SystemStats.
        :type: object
        """

        self._network = network

    @property
    def fs(self):
        """
        Gets the fs of this SystemStats.        :return: The fs of this SystemStats.
        :rtype: object
        """
        return self._fs

    @fs.setter
    def fs(self, fs):
        """
        Sets the fs of this SystemStats.        :param fs: The fs of this SystemStats.
        :type: object
        """

        self._fs = fs

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
