

from pprint import pformat

import re
class ClusterHealth(object):
    def __init__(self, status=None, shards=None):
        """
        ClusterHealth - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'status': 'str', 'shards': 'object'}

        self.attribute_map = {'status': 'status', 'shards': 'shards'}

        self._status = status
        self._shards = shards

    @property
    def status(self):
        """
        Gets the status of this ClusterHealth. :return: The status of this ClusterHealth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClusterHealth. :param status: The status of this ClusterHealth.
        :type: str
        """

        self._status = status

    @property
    def shards(self):
        """
        Gets the shards of this ClusterHealth. :return: The shards of this ClusterHealth.
        :rtype: object
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        """
        Sets the shards of this ClusterHealth. :param shards: The shards of this ClusterHealth.
        :type: object
        """

        self._shards = shards

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
