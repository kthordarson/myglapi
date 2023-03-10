

from pprint import pformat

import re
class ElasticsearchStats(object):
    def __init__(self, status=None, cluster_name=None, nodes_stats=None, cluster_health=None, indices_stats=None):
        """
        ElasticsearchStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'status': 'str', 'cluster_name': 'str', 'nodes_stats': 'object', 'cluster_health': 'object', 'indices_stats': 'object'}

        self.attribute_map = {'status': 'status', 'cluster_name': 'cluster_name', 'nodes_stats': 'nodes_stats', 'cluster_health': 'cluster_health', 'indices_stats': 'indices_stats'}

        self._status = status
        self._cluster_name = cluster_name
        self._nodes_stats = nodes_stats
        self._cluster_health = cluster_health
        self._indices_stats = indices_stats

    @property
    def status(self):
        """
        Gets the status of this ElasticsearchStats. :return: The status of this ElasticsearchStats.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ElasticsearchStats. :param status: The status of this ElasticsearchStats.
        :type: str
        """
        allowed_values = ["GREEN", "YELLOW", "RED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this ElasticsearchStats. :return: The cluster_name of this ElasticsearchStats.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this ElasticsearchStats. :param cluster_name: The cluster_name of this ElasticsearchStats.
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def nodes_stats(self):
        """
        Gets the nodes_stats of this ElasticsearchStats. :return: The nodes_stats of this ElasticsearchStats.
        :rtype: object
        """
        return self._nodes_stats

    @nodes_stats.setter
    def nodes_stats(self, nodes_stats):
        """
        Sets the nodes_stats of this ElasticsearchStats. :param nodes_stats: The nodes_stats of this ElasticsearchStats.
        :type: object
        """

        self._nodes_stats = nodes_stats

    @property
    def cluster_health(self):
        """
        Gets the cluster_health of this ElasticsearchStats. :return: The cluster_health of this ElasticsearchStats.
        :rtype: object
        """
        return self._cluster_health

    @cluster_health.setter
    def cluster_health(self, cluster_health):
        """
        Sets the cluster_health of this ElasticsearchStats. :param cluster_health: The cluster_health of this ElasticsearchStats.
        :type: object
        """

        self._cluster_health = cluster_health

    @property
    def indices_stats(self):
        """
        Gets the indices_stats of this ElasticsearchStats. :return: The indices_stats of this ElasticsearchStats.
        :rtype: object
        """
        return self._indices_stats

    @indices_stats.setter
    def indices_stats(self, indices_stats):
        """
        Sets the indices_stats of this ElasticsearchStats. :param indices_stats: The indices_stats of this ElasticsearchStats.
        :type: object
        """

        self._indices_stats = indices_stats

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
