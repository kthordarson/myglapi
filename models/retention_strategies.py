

from pprint import pformat
from six import iteritems
import re
class RetentionStrategies(object):
    def __init__(self, total=None, strategies=None):
        """
        RetentionStrategies - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int', 'strategies': 'list[object]'
        }

        self.attribute_map = {
            'total': 'total', 'strategies': 'strategies'
        }

        self._total = total
        self._strategies = strategies

    @property
    def total(self):
        """
        Gets the total of this RetentionStrategies.        :return: The total of this RetentionStrategies.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this RetentionStrategies.        :param total: The total of this RetentionStrategies.
        :type: int
        """

        self._total = total

    @property
    def strategies(self):
        """
        Gets the strategies of this RetentionStrategies.        :return: The strategies of this RetentionStrategies.
        :rtype: list[object]
        """
        return self._strategies

    @strategies.setter
    def strategies(self, strategies):
        """
        Sets the strategies of this RetentionStrategies.        :param strategies: The strategies of this RetentionStrategies.
        :type: list[object]
        """

        self._strategies = strategies

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
