

from pprint import pformat

import re
class ClosedIndices(object):
    def __init__(self, indices=None, total=None):
        """
        ClosedIndices - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'indices': 'list[str]', 'total': 'int'}

        self.attribute_map = {'indices': 'indices', 'total': 'total'}

        self._indices = indices
        self._total = total

    @property
    def indices(self):
        """
        Gets the indices of this ClosedIndices.        :return: The indices of this ClosedIndices.
        :rtype: list[str]
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """
        Sets the indices of this ClosedIndices.        :param indices: The indices of this ClosedIndices.
        :type: list[str]
        """

        self._indices = indices

    @property
    def total(self):
        """
        Gets the total of this ClosedIndices.        :return: The total of this ClosedIndices.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ClosedIndices.        :param total: The total of this ClosedIndices.
        :type: int
        """

        self._total = total

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
