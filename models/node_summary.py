

from pprint import pformat

import re
class NodeSummary(object):
    def __init__(self, cluster_id=None, node_id=None, type=None, is_master=None, transport_address=None, last_seen=None, short_node_id=None, hostname=None):
        """
        NodeSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'cluster_id': 'str', 'node_id': 'str', 'type': 'str', 'is_master': 'bool', 'transport_address': 'str', 'last_seen': 'str', 'short_node_id': 'str', 'hostname': 'str'}

        self.attribute_map = {'cluster_id': 'cluster_id', 'node_id': 'node_id', 'type': 'type', 'is_master': 'is_master', 'transport_address': 'transport_address', 'last_seen': 'last_seen', 'short_node_id': 'short_node_id', 'hostname': 'hostname'}

        self._cluster_id = cluster_id
        self._node_id = node_id
        self._type = type
        self._is_master = is_master
        self._transport_address = transport_address
        self._last_seen = last_seen
        self._short_node_id = short_node_id
        self._hostname = hostname

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this NodeSummary. :return: The cluster_id of this NodeSummary.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this NodeSummary. :param cluster_id: The cluster_id of this NodeSummary.
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def node_id(self):
        """
        Gets the node_id of this NodeSummary. :return: The node_id of this NodeSummary.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this NodeSummary. :param node_id: The node_id of this NodeSummary.
        :type: str
        """

        self._node_id = node_id

    @property
    def type(self):
        """
        Gets the type of this NodeSummary. :return: The type of this NodeSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NodeSummary. :param type: The type of this NodeSummary.
        :type: str
        """

        self._type = type

    @property
    def is_master(self):
        """
        Gets the is_master of this NodeSummary. :return: The is_master of this NodeSummary.
        :rtype: bool
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """
        Sets the is_master of this NodeSummary. :param is_master: The is_master of this NodeSummary.
        :type: bool
        """

        self._is_master = is_master

    @property
    def transport_address(self):
        """
        Gets the transport_address of this NodeSummary. :return: The transport_address of this NodeSummary.
        :rtype: str
        """
        return self._transport_address

    @transport_address.setter
    def transport_address(self, transport_address):
        """
        Sets the transport_address of this NodeSummary. :param transport_address: The transport_address of this NodeSummary.
        :type: str
        """

        self._transport_address = transport_address

    @property
    def last_seen(self):
        """
        Gets the last_seen of this NodeSummary. :return: The last_seen of this NodeSummary.
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """
        Sets the last_seen of this NodeSummary. :param last_seen: The last_seen of this NodeSummary.
        :type: str
        """

        self._last_seen = last_seen

    @property
    def short_node_id(self):
        """
        Gets the short_node_id of this NodeSummary. :return: The short_node_id of this NodeSummary.
        :rtype: str
        """
        return self._short_node_id

    @short_node_id.setter
    def short_node_id(self, short_node_id):
        """
        Sets the short_node_id of this NodeSummary. :param short_node_id: The short_node_id of this NodeSummary.
        :type: str
        """

        self._short_node_id = short_node_id

    @property
    def hostname(self):
        """
        Gets the hostname of this NodeSummary. :return: The hostname of this NodeSummary.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this NodeSummary. :param hostname: The hostname of this NodeSummary.
        :type: str
        """

        self._hostname = hostname

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
