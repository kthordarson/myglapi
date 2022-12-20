

from pprint import pformat

import re
class Token(object):
    def __init__(self, name=None, token=None, last_access=None):
        """
        Token - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'name': 'str', 'token': 'str', 'last_access': 'datetime'}

        self.attribute_map = {'name': 'name', 'token': 'token', 'last_access': 'last_access'}

        self._name = name
        self._token = token
        self._last_access = last_access

    @property
    def name(self):
        """
        Gets the name of this Token. :return: The name of this Token.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Token. :param name: The name of this Token.
        :type: str
        """

        self._name = name

    @property
    def token(self):
        """
        Gets the token of this Token. :return: The token of this Token.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this Token. :param token: The token of this Token.
        :type: str
        """

        self._token = token

    @property
    def last_access(self):
        """
        Gets the last_access of this Token. :return: The last_access of this Token.
        :rtype: datetime
        """
        return self._last_access

    @last_access.setter
    def last_access(self, last_access):
        """
        Sets the last_access of this Token. :param last_access: The last_access of this Token.
        :type: datetime
        """

        self._last_access = last_access

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
