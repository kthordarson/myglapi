

from pprint import pformat
from six import iteritems
import re
class NetworkStats(object):
    def __init__(self, interfaces=None, tcp=None, primary_interface=None):
        """
        NetworkStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interfaces': 'object', 'tcp': 'object', 'primary_interface': 'str'
        }

        self.attribute_map = {
            'interfaces': 'interfaces', 'tcp': 'tcp', 'primary_interface': 'primary_interface'
        }

        self._interfaces = interfaces
        self._tcp = tcp
        self._primary_interface = primary_interface

    @property
    def interfaces(self):
        """
        Gets the interfaces of this NetworkStats.        :return: The interfaces of this NetworkStats.
        :rtype: object
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this NetworkStats.        :param interfaces: The interfaces of this NetworkStats.
        :type: object
        """

        self._interfaces = interfaces

    @property
    def tcp(self):
        """
        Gets the tcp of this NetworkStats.        :return: The tcp of this NetworkStats.
        :rtype: object
        """
        return self._tcp

    @tcp.setter
    def tcp(self, tcp):
        """
        Sets the tcp of this NetworkStats.        :param tcp: The tcp of this NetworkStats.
        :type: object
        """

        self._tcp = tcp

    @property
    def primary_interface(self):
        """
        Gets the primary_interface of this NetworkStats.        :return: The primary_interface of this NetworkStats.
        :rtype: str
        """
        return self._primary_interface

    @primary_interface.setter
    def primary_interface(self, primary_interface):
        """
        Sets the primary_interface of this NetworkStats.        :param primary_interface: The primary_interface of this NetworkStats.
        :type: str
        """

        self._primary_interface = primary_interface

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
