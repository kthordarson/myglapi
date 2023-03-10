

from pprint import pformat

import re
class SystemOverviewResponse(object):
    def __init__(self, facility=None, codename=None, node_id=None, cluster_id=None, version=None, started_at=None, is_processing=None, hostname=None, lifecycle=None, lb_status=None, timezone=None, operating_system=None):
        """
        SystemOverviewResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'facility': 'str', 'codename': 'str', 'node_id': 'str', 'cluster_id': 'str', 'version': 'str', 'started_at': 'str', 'is_processing': 'bool', 'hostname': 'str', 'lifecycle': 'str', 'lb_status': 'str', 'timezone': 'str', 'operating_system': 'str'}

        self.attribute_map = {'facility': 'facility', 'codename': 'codename', 'node_id': 'node_id', 'cluster_id': 'cluster_id', 'version': 'version', 'started_at': 'started_at', 'is_processing': 'is_processing', 'hostname': 'hostname', 'lifecycle': 'lifecycle', 'lb_status': 'lb_status', 'timezone': 'timezone', 'operating_system': 'operating_system'}

        self._facility = facility
        self._codename = codename
        self._node_id = node_id
        self._cluster_id = cluster_id
        self._version = version
        self._started_at = started_at
        self._is_processing = is_processing
        self._hostname = hostname
        self._lifecycle = lifecycle
        self._lb_status = lb_status
        self._timezone = timezone
        self._operating_system = operating_system

    @property
    def facility(self):
        """
        Gets the facility of this SystemOverviewResponse. :return: The facility of this SystemOverviewResponse.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """
        Sets the facility of this SystemOverviewResponse. :param facility: The facility of this SystemOverviewResponse.
        :type: str
        """

        self._facility = facility

    @property
    def codename(self):
        """
        Gets the codename of this SystemOverviewResponse. :return: The codename of this SystemOverviewResponse.
        :rtype: str
        """
        return self._codename

    @codename.setter
    def codename(self, codename):
        """
        Sets the codename of this SystemOverviewResponse. :param codename: The codename of this SystemOverviewResponse.
        :type: str
        """

        self._codename = codename

    @property
    def node_id(self):
        """
        Gets the node_id of this SystemOverviewResponse. :return: The node_id of this SystemOverviewResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this SystemOverviewResponse. :param node_id: The node_id of this SystemOverviewResponse.
        :type: str
        """

        self._node_id = node_id

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this SystemOverviewResponse. :return: The cluster_id of this SystemOverviewResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this SystemOverviewResponse. :param cluster_id: The cluster_id of this SystemOverviewResponse.
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def version(self):
        """
        Gets the version of this SystemOverviewResponse. :return: The version of this SystemOverviewResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SystemOverviewResponse. :param version: The version of this SystemOverviewResponse.
        :type: str
        """

        self._version = version

    @property
    def started_at(self):
        """
        Gets the started_at of this SystemOverviewResponse. :return: The started_at of this SystemOverviewResponse.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this SystemOverviewResponse. :param started_at: The started_at of this SystemOverviewResponse.
        :type: str
        """

        self._started_at = started_at

    @property
    def is_processing(self):
        """
        Gets the is_processing of this SystemOverviewResponse. :return: The is_processing of this SystemOverviewResponse.
        :rtype: bool
        """
        return self._is_processing

    @is_processing.setter
    def is_processing(self, is_processing):
        """
        Sets the is_processing of this SystemOverviewResponse. :param is_processing: The is_processing of this SystemOverviewResponse.
        :type: bool
        """

        self._is_processing = is_processing

    @property
    def hostname(self):
        """
        Gets the hostname of this SystemOverviewResponse. :return: The hostname of this SystemOverviewResponse.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this SystemOverviewResponse. :param hostname: The hostname of this SystemOverviewResponse.
        :type: str
        """

        self._hostname = hostname

    @property
    def lifecycle(self):
        """
        Gets the lifecycle of this SystemOverviewResponse. :return: The lifecycle of this SystemOverviewResponse.
        :rtype: str
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """
        Sets the lifecycle of this SystemOverviewResponse. :param lifecycle: The lifecycle of this SystemOverviewResponse.
        :type: str
        """

        self._lifecycle = lifecycle

    @property
    def lb_status(self):
        """
        Gets the lb_status of this SystemOverviewResponse. :return: The lb_status of this SystemOverviewResponse.
        :rtype: str
        """
        return self._lb_status

    @lb_status.setter
    def lb_status(self, lb_status):
        """
        Sets the lb_status of this SystemOverviewResponse. :param lb_status: The lb_status of this SystemOverviewResponse.
        :type: str
        """

        self._lb_status = lb_status

    @property
    def timezone(self):
        """
        Gets the timezone of this SystemOverviewResponse. :return: The timezone of this SystemOverviewResponse.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this SystemOverviewResponse. :param timezone: The timezone of this SystemOverviewResponse.
        :type: str
        """

        self._timezone = timezone

    @property
    def operating_system(self):
        """
        Gets the operating_system of this SystemOverviewResponse. :return: The operating_system of this SystemOverviewResponse.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this SystemOverviewResponse. :param operating_system: The operating_system of this SystemOverviewResponse.
        :type: str
        """

        self._operating_system = operating_system

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
