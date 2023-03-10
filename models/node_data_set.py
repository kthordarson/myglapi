

from pprint import pformat

import re
class NodeDataSet(object):
    def __init__(self, jvm=None, timestamp=None, version=None, node_id=None, cluster_id=None, node_stats=None, node_info=None, report_interval_ms=None, host_info=None, host_stats=None):
        """
        NodeDataSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'jvm': 'object', 'timestamp': 'int', 'version': 'str', 'node_id': 'str', 'cluster_id': 'str', 'node_stats': 'object', 'node_info': 'object', 'report_interval_ms': 'int', 'host_info': 'object', 'host_stats': 'object'}

        self.attribute_map = {'jvm': 'jvm', 'timestamp': 'timestamp', 'version': 'version', 'node_id': 'node_id', 'cluster_id': 'cluster_id', 'node_stats': 'node_stats', 'node_info': 'node_info', 'report_interval_ms': 'report_interval_ms', 'host_info': 'host_info', 'host_stats': 'host_stats'}

        self._jvm = jvm
        self._timestamp = timestamp
        self._version = version
        self._node_id = node_id
        self._cluster_id = cluster_id
        self._node_stats = node_stats
        self._node_info = node_info
        self._report_interval_ms = report_interval_ms
        self._host_info = host_info
        self._host_stats = host_stats

    @property
    def jvm(self):
        """
        Gets the jvm of this NodeDataSet. :return: The jvm of this NodeDataSet.
        :rtype: object
        """
        return self._jvm

    @jvm.setter
    def jvm(self, jvm):
        """
        Sets the jvm of this NodeDataSet. :param jvm: The jvm of this NodeDataSet.
        :type: object
        """

        self._jvm = jvm

    @property
    def timestamp(self):
        """
        Gets the timestamp of this NodeDataSet. :return: The timestamp of this NodeDataSet.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this NodeDataSet. :param timestamp: The timestamp of this NodeDataSet.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def version(self):
        """
        Gets the version of this NodeDataSet. :return: The version of this NodeDataSet.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NodeDataSet. :param version: The version of this NodeDataSet.
        :type: str
        """

        self._version = version

    @property
    def node_id(self):
        """
        Gets the node_id of this NodeDataSet. :return: The node_id of this NodeDataSet.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this NodeDataSet. :param node_id: The node_id of this NodeDataSet.
        :type: str
        """

        self._node_id = node_id

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this NodeDataSet. :return: The cluster_id of this NodeDataSet.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this NodeDataSet. :param cluster_id: The cluster_id of this NodeDataSet.
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def node_stats(self):
        """
        Gets the node_stats of this NodeDataSet. :return: The node_stats of this NodeDataSet.
        :rtype: object
        """
        return self._node_stats

    @node_stats.setter
    def node_stats(self, node_stats):
        """
        Sets the node_stats of this NodeDataSet. :param node_stats: The node_stats of this NodeDataSet.
        :type: object
        """

        self._node_stats = node_stats

    @property
    def node_info(self):
        """
        Gets the node_info of this NodeDataSet. :return: The node_info of this NodeDataSet.
        :rtype: object
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """
        Sets the node_info of this NodeDataSet. :param node_info: The node_info of this NodeDataSet.
        :type: object
        """

        self._node_info = node_info

    @property
    def report_interval_ms(self):
        """
        Gets the report_interval_ms of this NodeDataSet. :return: The report_interval_ms of this NodeDataSet.
        :rtype: int
        """
        return self._report_interval_ms

    @report_interval_ms.setter
    def report_interval_ms(self, report_interval_ms):
        """
        Sets the report_interval_ms of this NodeDataSet. :param report_interval_ms: The report_interval_ms of this NodeDataSet.
        :type: int
        """

        self._report_interval_ms = report_interval_ms

    @property
    def host_info(self):
        """
        Gets the host_info of this NodeDataSet. :return: The host_info of this NodeDataSet.
        :rtype: object
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info):
        """
        Sets the host_info of this NodeDataSet. :param host_info: The host_info of this NodeDataSet.
        :type: object
        """

        self._host_info = host_info

    @property
    def host_stats(self):
        """
        Gets the host_stats of this NodeDataSet. :return: The host_stats of this NodeDataSet.
        :rtype: object
        """
        return self._host_stats

    @host_stats.setter
    def host_stats(self, host_stats):
        """
        Sets the host_stats of this NodeDataSet. :param host_stats: The host_stats of this NodeDataSet.
        :type: object
        """

        self._host_stats = host_stats

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
