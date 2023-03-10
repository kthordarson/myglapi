

from pprint import pformat

import re
class RoleResponse(object):
    def __init__(self, name=None, description=None, permissions=None, read_only=None):
        """
        RoleResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'name': 'str', 'description': 'str', 'permissions': 'list[str]', 'read_only': 'bool'}

        self.attribute_map = {'name': 'name', 'description': 'description', 'permissions': 'permissions', 'read_only': 'read_only'}

        self._name = name
        self._description = description
        self._permissions = permissions
        self._read_only = read_only

    @property
    def name(self):
        """
        Gets the name of this RoleResponse. :return: The name of this RoleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RoleResponse. :param name: The name of this RoleResponse.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this RoleResponse. :return: The description of this RoleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RoleResponse. :param description: The description of this RoleResponse.
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """
        Gets the permissions of this RoleResponse. :return: The permissions of this RoleResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this RoleResponse. :param permissions: The permissions of this RoleResponse.
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def read_only(self):
        """
        Gets the read_only of this RoleResponse. :return: The read_only of this RoleResponse.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this RoleResponse. :param read_only: The read_only of this RoleResponse.
        :type: bool
        """

        self._read_only = read_only

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
