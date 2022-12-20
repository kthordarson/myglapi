

from pprint import pformat

import re
class SessionCreateRequest(object):
    def __init__(self, username=None, password=None, host=None):
        """
        SessionCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'username': 'str', 'password': 'str', 'host': 'str'}

        self.attribute_map = {'username': 'username', 'password': 'password', 'host': 'host'}

        self._username = username
        self._password = password
        self._host = host

    @property
    def username(self):
        """
        Gets the username of this SessionCreateRequest. :return: The username of this SessionCreateRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SessionCreateRequest. :param username: The username of this SessionCreateRequest.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this SessionCreateRequest. :return: The password of this SessionCreateRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this SessionCreateRequest. :param password: The password of this SessionCreateRequest.
        :type: str
        """

        self._password = password

    @property
    def host(self):
        """
        Gets the host of this SessionCreateRequest. :return: The host of this SessionCreateRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this SessionCreateRequest. :param host: The host of this SessionCreateRequest.
        :type: str
        """

        self._host = host

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
