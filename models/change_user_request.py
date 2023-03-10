

from pprint import pformat

import re
class ChangeUserRequest(object):
    def __init__(self, email=None, full_name=None, permissions=None, timezone=None, startpage=None, session_timeout_ms=None, roles=None):
        """
        ChangeUserRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'email': 'str', 'full_name': 'str', 'permissions': 'list[str]', 'timezone': 'str', 'startpage': 'object', 'session_timeout_ms': 'int', 'roles': 'list[str]'}

        self.attribute_map = {'email': 'email', 'full_name': 'full_name', 'permissions': 'permissions', 'timezone': 'timezone', 'startpage': 'startpage', 'session_timeout_ms': 'session_timeout_ms', 'roles': 'roles'}

        self._email = email
        self._full_name = full_name
        self._permissions = permissions
        self._timezone = timezone
        self._startpage = startpage
        self._session_timeout_ms = session_timeout_ms
        self._roles = roles

    @property
    def email(self):
        """
        Gets the email of this ChangeUserRequest. :return: The email of this ChangeUserRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ChangeUserRequest. :param email: The email of this ChangeUserRequest.
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """
        Gets the full_name of this ChangeUserRequest. :return: The full_name of this ChangeUserRequest.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this ChangeUserRequest. :param full_name: The full_name of this ChangeUserRequest.
        :type: str
        """

        self._full_name = full_name

    @property
    def permissions(self):
        """
        Gets the permissions of this ChangeUserRequest. :return: The permissions of this ChangeUserRequest.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ChangeUserRequest. :param permissions: The permissions of this ChangeUserRequest.
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def timezone(self):
        """
        Gets the timezone of this ChangeUserRequest. :return: The timezone of this ChangeUserRequest.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ChangeUserRequest. :param timezone: The timezone of this ChangeUserRequest.
        :type: str
        """

        self._timezone = timezone

    @property
    def startpage(self):
        """
        Gets the startpage of this ChangeUserRequest. :return: The startpage of this ChangeUserRequest.
        :rtype: object
        """
        return self._startpage

    @startpage.setter
    def startpage(self, startpage):
        """
        Sets the startpage of this ChangeUserRequest. :param startpage: The startpage of this ChangeUserRequest.
        :type: object
        """

        self._startpage = startpage

    @property
    def session_timeout_ms(self):
        """
        Gets the session_timeout_ms of this ChangeUserRequest. :return: The session_timeout_ms of this ChangeUserRequest.
        :rtype: int
        """
        return self._session_timeout_ms

    @session_timeout_ms.setter
    def session_timeout_ms(self, session_timeout_ms):
        """
        Sets the session_timeout_ms of this ChangeUserRequest. :param session_timeout_ms: The session_timeout_ms of this ChangeUserRequest.
        :type: int
        """

        self._session_timeout_ms = session_timeout_ms

    @property
    def roles(self):
        """
        Gets the roles of this ChangeUserRequest. :return: The roles of this ChangeUserRequest.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this ChangeUserRequest. :param roles: The roles of this ChangeUserRequest.
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
