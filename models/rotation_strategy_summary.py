

from pprint import pformat

import re
class RotationStrategySummary(object):
    def __init__(self, strategy=None, config=None):
        """
        RotationStrategySummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'strategy': 'str', 'config': 'object'}

        self.attribute_map = {'strategy': 'strategy', 'config': 'config'}

        self._strategy = strategy
        self._config = config

    @property
    def strategy(self):
        """
        Gets the strategy of this RotationStrategySummary. :return: The strategy of this RotationStrategySummary.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Sets the strategy of this RotationStrategySummary. :param strategy: The strategy of this RotationStrategySummary.
        :type: str
        """

        self._strategy = strategy

    @property
    def config(self):
        """
        Gets the config of this RotationStrategySummary. :return: The config of this RotationStrategySummary.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this RotationStrategySummary. :param config: The config of this RotationStrategySummary.
        :type: object
        """

        self._config = config

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
