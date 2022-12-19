

from pprint import pformat

import re
class CollectorRegistrationRequest(object):
    def __init__(self, node_id=None, node_details=None):
        """
        CollectorRegistrationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'node_id': 'str', 'node_details': 'object'}

        self.attribute_map = {'node_id': 'node_id', 'node_details': 'node_details'}

        self._node_id = node_id
        self._node_details = node_details

    @property
    def node_id(self):
        """
        Gets the node_id of this CollectorRegistrationRequest.        :return: The node_id of this CollectorRegistrationRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this CollectorRegistrationRequest.        :param node_id: The node_id of this CollectorRegistrationRequest.
        :type: str
        """

        self._node_id = node_id

    @property
    def node_details(self):
        """
        Gets the node_details of this CollectorRegistrationRequest.        :return: The node_details of this CollectorRegistrationRequest.
        :rtype: object
        """
        return self._node_details

    @node_details.setter
    def node_details(self, node_details):
        """
        Sets the node_details of this CollectorRegistrationRequest.        :param node_details: The node_details of this CollectorRegistrationRequest.
        :type: object
        """

        self._node_details = node_details

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
