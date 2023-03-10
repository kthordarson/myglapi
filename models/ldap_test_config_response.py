

from pprint import pformat

import re
class LdapTestConfigResponse(object):
    def __init__(self, connected=None, system_authenticated=None, login_authenticated=None, entry=None, groups=None, exception=None):
        """
        LdapTestConfigResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'connected': 'bool', 'system_authenticated': 'bool', 'login_authenticated': 'bool', 'entry': 'object', 'groups': 'list[str]', 'exception': 'str'}

        self.attribute_map = {'connected': 'connected', 'system_authenticated': 'system_authenticated', 'login_authenticated': 'login_authenticated', 'entry': 'entry', 'groups': 'groups', 'exception': 'exception'}

        self._connected = connected
        self._system_authenticated = system_authenticated
        self._login_authenticated = login_authenticated
        self._entry = entry
        self._groups = groups
        self._exception = exception

    @property
    def connected(self):
        """
        Gets the connected of this LdapTestConfigResponse. :return: The connected of this LdapTestConfigResponse.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """
        Sets the connected of this LdapTestConfigResponse. :param connected: The connected of this LdapTestConfigResponse.
        :type: bool
        """

        self._connected = connected

    @property
    def system_authenticated(self):
        """
        Gets the system_authenticated of this LdapTestConfigResponse. :return: The system_authenticated of this LdapTestConfigResponse.
        :rtype: bool
        """
        return self._system_authenticated

    @system_authenticated.setter
    def system_authenticated(self, system_authenticated):
        """
        Sets the system_authenticated of this LdapTestConfigResponse. :param system_authenticated: The system_authenticated of this LdapTestConfigResponse.
        :type: bool
        """

        self._system_authenticated = system_authenticated

    @property
    def login_authenticated(self):
        """
        Gets the login_authenticated of this LdapTestConfigResponse. :return: The login_authenticated of this LdapTestConfigResponse.
        :rtype: bool
        """
        return self._login_authenticated

    @login_authenticated.setter
    def login_authenticated(self, login_authenticated):
        """
        Sets the login_authenticated of this LdapTestConfigResponse. :param login_authenticated: The login_authenticated of this LdapTestConfigResponse.
        :type: bool
        """

        self._login_authenticated = login_authenticated

    @property
    def entry(self):
        """
        Gets the entry of this LdapTestConfigResponse. :return: The entry of this LdapTestConfigResponse.
        :rtype: object
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """
        Sets the entry of this LdapTestConfigResponse. :param entry: The entry of this LdapTestConfigResponse.
        :type: object
        """

        self._entry = entry

    @property
    def groups(self):
        """
        Gets the groups of this LdapTestConfigResponse. :return: The groups of this LdapTestConfigResponse.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this LdapTestConfigResponse. :param groups: The groups of this LdapTestConfigResponse.
        :type: list[str]
        """

        self._groups = groups

    @property
    def exception(self):
        """
        Gets the exception of this LdapTestConfigResponse. :return: The exception of this LdapTestConfigResponse.
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """
        Sets the exception of this LdapTestConfigResponse. :param exception: The exception of this LdapTestConfigResponse.
        :type: str
        """

        self._exception = exception

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
