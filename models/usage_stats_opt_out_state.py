

from pprint import pformat

import re
class UsageStatsOptOutState(object):
    def __init__(self, opt_out=None):
        """
        UsageStatsOptOutState - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'opt_out': 'bool'}

        self.attribute_map = {'opt_out': 'opt_out'}

        self._opt_out = opt_out

    @property
    def opt_out(self):
        """
        Gets the opt_out of this UsageStatsOptOutState.        :return: The opt_out of this UsageStatsOptOutState.
        :rtype: bool
        """
        return self._opt_out

    @opt_out.setter
    def opt_out(self, opt_out):
        """
        Sets the opt_out of this UsageStatsOptOutState.        :param opt_out: The opt_out of this UsageStatsOptOutState.
        :type: bool
        """

        self._opt_out = opt_out

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
