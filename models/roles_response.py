

from pprint import pformat

import re
class RolesResponse(object):
    def __init__(self, roles=None, total=None):
        """
        RolesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'roles': 'list[object]', 'total': 'int'}

        self.attribute_map = {'roles': 'roles', 'total': 'total'}

        self._roles = roles
        self._total = total

    @property
    def roles(self):
        """
        Gets the roles of this RolesResponse. :return: The roles of this RolesResponse.
        :rtype: list[object]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this RolesResponse. :param roles: The roles of this RolesResponse.
        :type: list[object]
        """

        self._roles = roles

    @property
    def total(self):
        """
        Gets the total of this RolesResponse. :return: The total of this RolesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this RolesResponse. :param total: The total of this RolesResponse.
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
