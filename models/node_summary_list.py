

from pprint import pformat

import re
class NodeSummaryList(object):
    def __init__(self, nodes=None, total=None):
        """
        NodeSummaryList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'nodes': 'list[object]', 'total': 'int'}

        self.attribute_map = {'nodes': 'nodes', 'total': 'total'}

        self._nodes = nodes
        self._total = total

    @property
    def nodes(self):
        """
        Gets the nodes of this NodeSummaryList.        :return: The nodes of this NodeSummaryList.
        :rtype: list[object]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this NodeSummaryList.        :param nodes: The nodes of this NodeSummaryList.
        :type: list[object]
        """

        self._nodes = nodes

    @property
    def total(self):
        """
        Gets the total of this NodeSummaryList.        :return: The total of this NodeSummaryList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this NodeSummaryList.        :param total: The total of this NodeSummaryList.
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
