

from pprint import pformat
from six import iteritems
import re
class SystemThreadDumpResponse(object):
    def __init__(self, threaddump=None):
        """
        SystemThreadDumpResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'threaddump': 'str'
        }

        self.attribute_map = {
            'threaddump': 'threaddump'
        }

        self._threaddump = threaddump

    @property
    def threaddump(self):
        """
        Gets the threaddump of this SystemThreadDumpResponse.        :return: The threaddump of this SystemThreadDumpResponse.
        :rtype: str
        """
        return self._threaddump

    @threaddump.setter
    def threaddump(self, threaddump):
        """
        Sets the threaddump of this SystemThreadDumpResponse.        :param threaddump: The threaddump of this SystemThreadDumpResponse.
        :type: str
        """

        self._threaddump = threaddump

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
