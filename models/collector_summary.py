

from pprint import pformat

import re
class CollectorSummary(object):
    def __init__(self, id=None, node_id=None, node_details=None, last_seen=None, collector_version=None, active=None):
        """
        CollectorSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'node_id': 'str', 'node_details': 'object', 'last_seen': 'datetime', 'collector_version': 'str', 'active': 'bool'}

        self.attribute_map = {'id': 'id', 'node_id': 'node_id', 'node_details': 'node_details', 'last_seen': 'last_seen', 'collector_version': 'collector_version', 'active': 'active'}

        self._id = id
        self._node_id = node_id
        self._node_details = node_details
        self._last_seen = last_seen
        self._collector_version = collector_version
        self._active = active

    @property
    def id(self):
        """
        Gets the id of this CollectorSummary. :return: The id of this CollectorSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CollectorSummary. :param id: The id of this CollectorSummary.
        :type: str
        """

        self._id = id

    @property
    def node_id(self):
        """
        Gets the node_id of this CollectorSummary. :return: The node_id of this CollectorSummary.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this CollectorSummary. :param node_id: The node_id of this CollectorSummary.
        :type: str
        """

        self._node_id = node_id

    @property
    def node_details(self):
        """
        Gets the node_details of this CollectorSummary. :return: The node_details of this CollectorSummary.
        :rtype: object
        """
        return self._node_details

    @node_details.setter
    def node_details(self, node_details):
        """
        Sets the node_details of this CollectorSummary. :param node_details: The node_details of this CollectorSummary.
        :type: object
        """

        self._node_details = node_details

    @property
    def last_seen(self):
        """
        Gets the last_seen of this CollectorSummary. :return: The last_seen of this CollectorSummary.
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """
        Sets the last_seen of this CollectorSummary. :param last_seen: The last_seen of this CollectorSummary.
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def collector_version(self):
        """
        Gets the collector_version of this CollectorSummary. :return: The collector_version of this CollectorSummary.
        :rtype: str
        """
        return self._collector_version

    @collector_version.setter
    def collector_version(self, collector_version):
        """
        Sets the collector_version of this CollectorSummary. :param collector_version: The collector_version of this CollectorSummary.
        :type: str
        """

        self._collector_version = collector_version

    @property
    def active(self):
        """
        Gets the active of this CollectorSummary. :return: The active of this CollectorSummary.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CollectorSummary. :param active: The active of this CollectorSummary.
        :type: bool
        """

        self._active = active

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
