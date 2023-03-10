

from pprint import pformat

import re
class ClusterDataSet(object):
    def __init__(self, timestamp=None, version=None, cluster_id=None, report_interval_ms=None, cluster_stats=None):
        """
        ClusterDataSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'timestamp': 'int', 'version': 'str', 'cluster_id': 'str', 'report_interval_ms': 'int', 'cluster_stats': 'object'}

        self.attribute_map = {'timestamp': 'timestamp', 'version': 'version', 'cluster_id': 'cluster_id', 'report_interval_ms': 'report_interval_ms', 'cluster_stats': 'cluster_stats'}

        self._timestamp = timestamp
        self._version = version
        self._cluster_id = cluster_id
        self._report_interval_ms = report_interval_ms
        self._cluster_stats = cluster_stats

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ClusterDataSet. :return: The timestamp of this ClusterDataSet.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ClusterDataSet. :param timestamp: The timestamp of this ClusterDataSet.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def version(self):
        """
        Gets the version of this ClusterDataSet. :return: The version of this ClusterDataSet.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ClusterDataSet. :param version: The version of this ClusterDataSet.
        :type: str
        """

        self._version = version

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this ClusterDataSet. :return: The cluster_id of this ClusterDataSet.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this ClusterDataSet. :param cluster_id: The cluster_id of this ClusterDataSet.
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def report_interval_ms(self):
        """
        Gets the report_interval_ms of this ClusterDataSet. :return: The report_interval_ms of this ClusterDataSet.
        :rtype: int
        """
        return self._report_interval_ms

    @report_interval_ms.setter
    def report_interval_ms(self, report_interval_ms):
        """
        Sets the report_interval_ms of this ClusterDataSet. :param report_interval_ms: The report_interval_ms of this ClusterDataSet.
        :type: int
        """

        self._report_interval_ms = report_interval_ms

    @property
    def cluster_stats(self):
        """
        Gets the cluster_stats of this ClusterDataSet. :return: The cluster_stats of this ClusterDataSet.
        :rtype: object
        """
        return self._cluster_stats

    @cluster_stats.setter
    def cluster_stats(self, cluster_stats):
        """
        Sets the cluster_stats of this ClusterDataSet. :param cluster_stats: The cluster_stats of this ClusterDataSet.
        :type: object
        """

        self._cluster_stats = cluster_stats

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
