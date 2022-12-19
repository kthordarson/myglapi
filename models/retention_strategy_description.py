

from pprint import pformat

import re
class RetentionStrategyDescription(object):
    def __init__(self, type=None, default_config=None, json_schema=None):
        """
        RetentionStrategyDescription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'type': 'str', 'default_config': 'object', 'json_schema': 'object'}

        self.attribute_map = {'type': 'type', 'default_config': 'default_config', 'json_schema': 'json_schema'}

        self._type = type
        self._default_config = default_config
        self._json_schema = json_schema

    @property
    def type(self):
        """
        Gets the type of this RetentionStrategyDescription.        :return: The type of this RetentionStrategyDescription.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RetentionStrategyDescription.        :param type: The type of this RetentionStrategyDescription.
        :type: str
        """

        self._type = type

    @property
    def default_config(self):
        """
        Gets the default_config of this RetentionStrategyDescription.        :return: The default_config of this RetentionStrategyDescription.
        :rtype: object
        """
        return self._default_config

    @default_config.setter
    def default_config(self, default_config):
        """
        Sets the default_config of this RetentionStrategyDescription.        :param default_config: The default_config of this RetentionStrategyDescription.
        :type: object
        """

        self._default_config = default_config

    @property
    def json_schema(self):
        """
        Gets the json_schema of this RetentionStrategyDescription.        :return: The json_schema of this RetentionStrategyDescription.
        :rtype: object
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        """
        Sets the json_schema of this RetentionStrategyDescription.        :param json_schema: The json_schema of this RetentionStrategyDescription.
        :type: object
        """

        self._json_schema = json_schema

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
