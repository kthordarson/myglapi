

from pprint import pformat

import re
class PluginList(object):
    def __init__(self, plugins=None, total=None):
        """
        PluginList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'plugins': 'list[object]', 'total': 'int'}

        self.attribute_map = {'plugins': 'plugins', 'total': 'total'}

        self._plugins = plugins
        self._total = total

    @property
    def plugins(self):
        """
        Gets the plugins of this PluginList. :return: The plugins of this PluginList.
        :rtype: list[object]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """
        Sets the plugins of this PluginList. :param plugins: The plugins of this PluginList.
        :type: list[object]
        """

        self._plugins = plugins

    @property
    def total(self):
        """
        Gets the total of this PluginList. :return: The total of this PluginList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this PluginList. :param total: The total of this PluginList.
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
