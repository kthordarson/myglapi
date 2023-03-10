

from pprint import pformat

import re
class InputTypesSummary(object):
    def __init__(self, types=None):
        """
        InputTypesSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'types': 'object'}

        self.attribute_map = {'types': 'types'}

        self._types = types

    @property
    def types(self):
        """
        Gets the types of this InputTypesSummary. :return: The types of this InputTypesSummary.
        :rtype: object
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this InputTypesSummary. :param types: The types of this InputTypesSummary.
        :type: object
        """

        self._types = types

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
