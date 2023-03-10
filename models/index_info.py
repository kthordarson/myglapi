

from pprint import pformat

import re
class IndexInfo(object):
    def __init__(self, primary_shards=None, all_shards=None, routing=None, reopened=None):
        """
        IndexInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'primary_shards': 'object', 'all_shards': 'object', 'routing': 'list[object]', 'reopened': 'bool'}

        self.attribute_map = {'primary_shards': 'primary_shards', 'all_shards': 'all_shards', 'routing': 'routing', 'reopened': 'reopened'}

        self._primary_shards = primary_shards
        self._all_shards = all_shards
        self._routing = routing
        self._reopened = reopened

    @property
    def primary_shards(self):
        """
        Gets the primary_shards of this IndexInfo. :return: The primary_shards of this IndexInfo.
        :rtype: object
        """
        return self._primary_shards

    @primary_shards.setter
    def primary_shards(self, primary_shards):
        """
        Sets the primary_shards of this IndexInfo. :param primary_shards: The primary_shards of this IndexInfo.
        :type: object
        """

        self._primary_shards = primary_shards

    @property
    def all_shards(self):
        """
        Gets the all_shards of this IndexInfo. :return: The all_shards of this IndexInfo.
        :rtype: object
        """
        return self._all_shards

    @all_shards.setter
    def all_shards(self, all_shards):
        """
        Sets the all_shards of this IndexInfo. :param all_shards: The all_shards of this IndexInfo.
        :type: object
        """

        self._all_shards = all_shards

    @property
    def routing(self):
        """
        Gets the routing of this IndexInfo. :return: The routing of this IndexInfo.
        :rtype: list[object]
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """
        Sets the routing of this IndexInfo. :param routing: The routing of this IndexInfo.
        :type: list[object]
        """

        self._routing = routing

    @property
    def reopened(self):
        """
        Gets the reopened of this IndexInfo. :return: The reopened of this IndexInfo.
        :rtype: bool
        """
        return self._reopened

    @reopened.setter
    def reopened(self, reopened):
        """
        Sets the reopened of this IndexInfo. :param reopened: The reopened of this IndexInfo.
        :type: bool
        """

        self._reopened = reopened

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
