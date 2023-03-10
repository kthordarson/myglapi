

from pprint import pformat

import re
class DeflectorSummary(object):
    def __init__(self, is_up=None, current_target=None):
        """
        DeflectorSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'is_up': 'bool', 'current_target': 'str'}

        self.attribute_map = {'is_up': 'is_up', 'current_target': 'current_target'}

        self._is_up = is_up
        self._current_target = current_target

    @property
    def is_up(self):
        """
        Gets the is_up of this DeflectorSummary. :return: The is_up of this DeflectorSummary.
        :rtype: bool
        """
        return self._is_up

    @is_up.setter
    def is_up(self, is_up):
        """
        Sets the is_up of this DeflectorSummary. :param is_up: The is_up of this DeflectorSummary.
        :type: bool
        """

        self._is_up = is_up

    @property
    def current_target(self):
        """
        Gets the current_target of this DeflectorSummary. :return: The current_target of this DeflectorSummary.
        :rtype: str
        """
        return self._current_target

    @current_target.setter
    def current_target(self, current_target):
        """
        Sets the current_target of this DeflectorSummary. :param current_target: The current_target of this DeflectorSummary.
        :type: str
        """

        self._current_target = current_target

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
