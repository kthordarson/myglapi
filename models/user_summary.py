

from pprint import pformat

import re
class UserSummary(object):
    def __init__(self, id=None, username=None, email=None, full_name=None, permissions=None, preferences=None, timezone=None, session_timeout_ms=None, read_only=None, external=None, startpage=None, roles=None, session_active=None, last_activity=None, client_address=None):
        """
        UserSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'username': 'str', 'email': 'str', 'full_name': 'str', 'permissions': 'list[str]', 'preferences': 'object', 'timezone': 'str', 'session_timeout_ms': 'int', 'read_only': 'bool', 'external': 'bool', 'startpage': 'object', 'roles': 'list[str]', 'session_active': 'bool', 'last_activity': 'datetime', 'client_address': 'str'}

        self.attribute_map = {'id': 'id', 'username': 'username', 'email': 'email', 'full_name': 'full_name', 'permissions': 'permissions', 'preferences': 'preferences', 'timezone': 'timezone', 'session_timeout_ms': 'session_timeout_ms', 'read_only': 'read_only', 'external': 'external', 'startpage': 'startpage', 'roles': 'roles', 'session_active': 'session_active', 'last_activity': 'last_activity', 'client_address': 'client_address'}

        self._id = id
        self._username = username
        self._email = email
        self._full_name = full_name
        self._permissions = permissions
        self._preferences = preferences
        self._timezone = timezone
        self._session_timeout_ms = session_timeout_ms
        self._read_only = read_only
        self._external = external
        self._startpage = startpage
        self._roles = roles
        self._session_active = session_active
        self._last_activity = last_activity
        self._client_address = client_address

    @property
    def id(self):
        """
        Gets the id of this UserSummary. :return: The id of this UserSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserSummary. :param id: The id of this UserSummary.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this UserSummary. :return: The username of this UserSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserSummary. :param username: The username of this UserSummary.
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """
        Gets the email of this UserSummary. :return: The email of this UserSummary.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserSummary. :param email: The email of this UserSummary.
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """
        Gets the full_name of this UserSummary. :return: The full_name of this UserSummary.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this UserSummary. :param full_name: The full_name of this UserSummary.
        :type: str
        """

        self._full_name = full_name

    @property
    def permissions(self):
        """
        Gets the permissions of this UserSummary. :return: The permissions of this UserSummary.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this UserSummary. :param permissions: The permissions of this UserSummary.
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def preferences(self):
        """
        Gets the preferences of this UserSummary. :return: The preferences of this UserSummary.
        :rtype: object
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """
        Sets the preferences of this UserSummary. :param preferences: The preferences of this UserSummary.
        :type: object
        """

        self._preferences = preferences

    @property
    def timezone(self):
        """
        Gets the timezone of this UserSummary. :return: The timezone of this UserSummary.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this UserSummary. :param timezone: The timezone of this UserSummary.
        :type: str
        """

        self._timezone = timezone

    @property
    def session_timeout_ms(self):
        """
        Gets the session_timeout_ms of this UserSummary. :return: The session_timeout_ms of this UserSummary.
        :rtype: int
        """
        return self._session_timeout_ms

    @session_timeout_ms.setter
    def session_timeout_ms(self, session_timeout_ms):
        """
        Sets the session_timeout_ms of this UserSummary. :param session_timeout_ms: The session_timeout_ms of this UserSummary.
        :type: int
        """

        self._session_timeout_ms = session_timeout_ms

    @property
    def read_only(self):
        """
        Gets the read_only of this UserSummary. :return: The read_only of this UserSummary.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this UserSummary. :param read_only: The read_only of this UserSummary.
        :type: bool
        """

        self._read_only = read_only

    @property
    def external(self):
        """
        Gets the external of this UserSummary. :return: The external of this UserSummary.
        :rtype: bool
        """
        return self._external

    @external.setter
    def external(self, external):
        """
        Sets the external of this UserSummary. :param external: The external of this UserSummary.
        :type: bool
        """

        self._external = external

    @property
    def startpage(self):
        """
        Gets the startpage of this UserSummary. :return: The startpage of this UserSummary.
        :rtype: object
        """
        return self._startpage

    @startpage.setter
    def startpage(self, startpage):
        """
        Sets the startpage of this UserSummary. :param startpage: The startpage of this UserSummary.
        :type: object
        """

        self._startpage = startpage

    @property
    def roles(self):
        """
        Gets the roles of this UserSummary. :return: The roles of this UserSummary.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this UserSummary. :param roles: The roles of this UserSummary.
        :type: list[str]
        """

        self._roles = roles

    @property
    def session_active(self):
        """
        Gets the session_active of this UserSummary. :return: The session_active of this UserSummary.
        :rtype: bool
        """
        return self._session_active

    @session_active.setter
    def session_active(self, session_active):
        """
        Sets the session_active of this UserSummary. :param session_active: The session_active of this UserSummary.
        :type: bool
        """

        self._session_active = session_active

    @property
    def last_activity(self):
        """
        Gets the last_activity of this UserSummary. :return: The last_activity of this UserSummary.
        :rtype: datetime
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """
        Sets the last_activity of this UserSummary. :param last_activity: The last_activity of this UserSummary.
        :type: datetime
        """

        self._last_activity = last_activity

    @property
    def client_address(self):
        """
        Gets the client_address of this UserSummary. :return: The client_address of this UserSummary.
        :rtype: str
        """
        return self._client_address

    @client_address.setter
    def client_address(self, client_address):
        """
        Sets the client_address of this UserSummary. :param client_address: The client_address of this UserSummary.
        :type: str
        """

        self._client_address = client_address

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
