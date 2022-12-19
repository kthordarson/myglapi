

from pprint import pformat
from six import iteritems
import re
class OsStats(object):
    def __init__(self, swap=None, processor=None, load_average=None, uptime=None, memory=None):
        """
        OsStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'swap': 'object', 'processor': 'object', 'load_average': 'list[float]', 'uptime': 'int', 'memory': 'object'
        }

        self.attribute_map = {
            'swap': 'swap', 'processor': 'processor', 'load_average': 'load_average', 'uptime': 'uptime', 'memory': 'memory'
        }

        self._swap = swap
        self._processor = processor
        self._load_average = load_average
        self._uptime = uptime
        self._memory = memory

    @property
    def swap(self):
        """
        Gets the swap of this OsStats.        :return: The swap of this OsStats.
        :rtype: object
        """
        return self._swap

    @swap.setter
    def swap(self, swap):
        """
        Sets the swap of this OsStats.        :param swap: The swap of this OsStats.
        :type: object
        """

        self._swap = swap

    @property
    def processor(self):
        """
        Gets the processor of this OsStats.        :return: The processor of this OsStats.
        :rtype: object
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """
        Sets the processor of this OsStats.        :param processor: The processor of this OsStats.
        :type: object
        """

        self._processor = processor

    @property
    def load_average(self):
        """
        Gets the load_average of this OsStats.        :return: The load_average of this OsStats.
        :rtype: list[float]
        """
        return self._load_average

    @load_average.setter
    def load_average(self, load_average):
        """
        Sets the load_average of this OsStats.        :param load_average: The load_average of this OsStats.
        :type: list[float]
        """

        self._load_average = load_average

    @property
    def uptime(self):
        """
        Gets the uptime of this OsStats.        :return: The uptime of this OsStats.
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """
        Sets the uptime of this OsStats.        :param uptime: The uptime of this OsStats.
        :type: int
        """

        self._uptime = uptime

    @property
    def memory(self):
        """
        Gets the memory of this OsStats.        :return: The memory of this OsStats.
        :rtype: object
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this OsStats.        :param memory: The memory of this OsStats.
        :type: object
        """

        self._memory = memory

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
