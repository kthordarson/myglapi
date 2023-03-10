

from pprint import pformat

import re
class CreateUserRequest(object):
    def __init__(self, username=None, password=None, email=None, full_name=None, permissions=None, timezone=None, session_timeout_ms=None, startpage=None, roles=None):
        """
        CreateUserRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'username': 'str', 'password': 'str', 'email': 'str', 'full_name': 'str', 'permissions': 'list[str]', 'timezone': 'str', 'session_timeout_ms': 'int', 'startpage': 'object', 'roles': 'list[str]'}

        self.attribute_map = {'username': 'username', 'password': 'password', 'email': 'email', 'full_name': 'full_name', 'permissions': 'permissions', 'timezone': 'timezone', 'session_timeout_ms': 'session_timeout_ms', 'startpage': 'startpage', 'roles': 'roles'}

        self._username = username
        self._password = password
        self._email = email
        self._full_name = full_name
        self._permissions = permissions
        self._timezone = timezone
        self._session_timeout_ms = session_timeout_ms
        self._startpage = startpage
        self._roles = roles

    @property
    def username(self):
        """
        Gets the username of this CreateUserRequest. :return: The username of this CreateUserRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateUserRequest. :param username: The username of this CreateUserRequest.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this CreateUserRequest. :return: The password of this CreateUserRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateUserRequest. :param password: The password of this CreateUserRequest.
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """
        Gets the email of this CreateUserRequest. :return: The email of this CreateUserRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateUserRequest. :param email: The email of this CreateUserRequest.
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """
        Gets the full_name of this CreateUserRequest. :return: The full_name of this CreateUserRequest.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this CreateUserRequest. :param full_name: The full_name of this CreateUserRequest.
        :type: str
        """

        self._full_name = full_name

    @property
    def permissions(self):
        """
        Gets the permissions of this CreateUserRequest. :return: The permissions of this CreateUserRequest.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this CreateUserRequest. :param permissions: The permissions of this CreateUserRequest.
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def timezone(self):
        """
        Gets the timezone of this CreateUserRequest. :return: The timezone of this CreateUserRequest.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this CreateUserRequest. :param timezone: The timezone of this CreateUserRequest.
        :type: str
        """

        self._timezone = timezone

    @property
    def session_timeout_ms(self):
        """
        Gets the session_timeout_ms of this CreateUserRequest. :return: The session_timeout_ms of this CreateUserRequest.
        :rtype: int
        """
        return self._session_timeout_ms

    @session_timeout_ms.setter
    def session_timeout_ms(self, session_timeout_ms):
        """
        Sets the session_timeout_ms of this CreateUserRequest. :param session_timeout_ms: The session_timeout_ms of this CreateUserRequest.
        :type: int
        """

        self._session_timeout_ms = session_timeout_ms

    @property
    def startpage(self):
        """
        Gets the startpage of this CreateUserRequest. :return: The startpage of this CreateUserRequest.
        :rtype: object
        """
        return self._startpage

    @startpage.setter
    def startpage(self, startpage):
        """
        Sets the startpage of this CreateUserRequest. :param startpage: The startpage of this CreateUserRequest.
        :type: object
        """

        self._startpage = startpage

    @property
    def roles(self):
        """
        Gets the roles of this CreateUserRequest. :return: The roles of this CreateUserRequest.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this CreateUserRequest. :param roles: The roles of this CreateUserRequest.
        :type: list[str]
        """

        self._roles = roles

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
