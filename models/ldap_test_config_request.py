

from pprint import pformat

import re
class LdapTestConfigRequest(object):
    def __init__(self, system_username=None, system_password=None, ldap_uri=None, use_start_tls=None, trust_all_certificates=None, active_directory=None, search_base=None, search_pattern=None, principal=None, password=None, test_connect_only=None, group_search_base=None, group_id_attribute=None, group_search_pattern=None):
        """
        LdapTestConfigRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'system_username': 'str', 'system_password': 'str', 'ldap_uri': 'str', 'use_start_tls': 'bool', 'trust_all_certificates': 'bool', 'active_directory': 'bool', 'search_base': 'str', 'search_pattern': 'str', 'principal': 'str', 'password': 'str', 'test_connect_only': 'bool', 'group_search_base': 'str', 'group_id_attribute': 'str', 'group_search_pattern': 'str'}

        self.attribute_map = {'system_username': 'system_username', 'system_password': 'system_password', 'ldap_uri': 'ldap_uri', 'use_start_tls': 'use_start_tls', 'trust_all_certificates': 'trust_all_certificates', 'active_directory': 'active_directory', 'search_base': 'search_base', 'search_pattern': 'search_pattern', 'principal': 'principal', 'password': 'password', 'test_connect_only': 'test_connect_only', 'group_search_base': 'group_search_base', 'group_id_attribute': 'group_id_attribute', 'group_search_pattern': 'group_search_pattern'}

        self._system_username = system_username
        self._system_password = system_password
        self._ldap_uri = ldap_uri
        self._use_start_tls = use_start_tls
        self._trust_all_certificates = trust_all_certificates
        self._active_directory = active_directory
        self._search_base = search_base
        self._search_pattern = search_pattern
        self._principal = principal
        self._password = password
        self._test_connect_only = test_connect_only
        self._group_search_base = group_search_base
        self._group_id_attribute = group_id_attribute
        self._group_search_pattern = group_search_pattern

    @property
    def system_username(self):
        """
        Gets the system_username of this LdapTestConfigRequest. :return: The system_username of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._system_username

    @system_username.setter
    def system_username(self, system_username):
        """
        Sets the system_username of this LdapTestConfigRequest. :param system_username: The system_username of this LdapTestConfigRequest.
        :type: str
        """

        self._system_username = system_username

    @property
    def system_password(self):
        """
        Gets the system_password of this LdapTestConfigRequest. :return: The system_password of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._system_password

    @system_password.setter
    def system_password(self, system_password):
        """
        Sets the system_password of this LdapTestConfigRequest. :param system_password: The system_password of this LdapTestConfigRequest.
        :type: str
        """

        self._system_password = system_password

    @property
    def ldap_uri(self):
        """
        Gets the ldap_uri of this LdapTestConfigRequest. :return: The ldap_uri of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._ldap_uri

    @ldap_uri.setter
    def ldap_uri(self, ldap_uri):
        """
        Sets the ldap_uri of this LdapTestConfigRequest. :param ldap_uri: The ldap_uri of this LdapTestConfigRequest.
        :type: str
        """

        self._ldap_uri = ldap_uri

    @property
    def use_start_tls(self):
        """
        Gets the use_start_tls of this LdapTestConfigRequest. :return: The use_start_tls of this LdapTestConfigRequest.
        :rtype: bool
        """
        return self._use_start_tls

    @use_start_tls.setter
    def use_start_tls(self, use_start_tls):
        """
        Sets the use_start_tls of this LdapTestConfigRequest. :param use_start_tls: The use_start_tls of this LdapTestConfigRequest.
        :type: bool
        """

        self._use_start_tls = use_start_tls

    @property
    def trust_all_certificates(self):
        """
        Gets the trust_all_certificates of this LdapTestConfigRequest. :return: The trust_all_certificates of this LdapTestConfigRequest.
        :rtype: bool
        """
        return self._trust_all_certificates

    @trust_all_certificates.setter
    def trust_all_certificates(self, trust_all_certificates):
        """
        Sets the trust_all_certificates of this LdapTestConfigRequest. :param trust_all_certificates: The trust_all_certificates of this LdapTestConfigRequest.
        :type: bool
        """

        self._trust_all_certificates = trust_all_certificates

    @property
    def active_directory(self):
        """
        Gets the active_directory of this LdapTestConfigRequest. :return: The active_directory of this LdapTestConfigRequest.
        :rtype: bool
        """
        return self._active_directory

    @active_directory.setter
    def active_directory(self, active_directory):
        """
        Sets the active_directory of this LdapTestConfigRequest. :param active_directory: The active_directory of this LdapTestConfigRequest.
        :type: bool
        """

        self._active_directory = active_directory

    @property
    def search_base(self):
        """
        Gets the search_base of this LdapTestConfigRequest. :return: The search_base of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._search_base

    @search_base.setter
    def search_base(self, search_base):
        """
        Sets the search_base of this LdapTestConfigRequest. :param search_base: The search_base of this LdapTestConfigRequest.
        :type: str
        """

        self._search_base = search_base

    @property
    def search_pattern(self):
        """
        Gets the search_pattern of this LdapTestConfigRequest. :return: The search_pattern of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._search_pattern

    @search_pattern.setter
    def search_pattern(self, search_pattern):
        """
        Sets the search_pattern of this LdapTestConfigRequest. :param search_pattern: The search_pattern of this LdapTestConfigRequest.
        :type: str
        """

        self._search_pattern = search_pattern

    @property
    def principal(self):
        """
        Gets the principal of this LdapTestConfigRequest. :return: The principal of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """
        Sets the principal of this LdapTestConfigRequest. :param principal: The principal of this LdapTestConfigRequest.
        :type: str
        """

        self._principal = principal

    @property
    def password(self):
        """
        Gets the password of this LdapTestConfigRequest. :return: The password of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this LdapTestConfigRequest. :param password: The password of this LdapTestConfigRequest.
        :type: str
        """

        self._password = password

    @property
    def test_connect_only(self):
        """
        Gets the test_connect_only of this LdapTestConfigRequest. :return: The test_connect_only of this LdapTestConfigRequest.
        :rtype: bool
        """
        return self._test_connect_only

    @test_connect_only.setter
    def test_connect_only(self, test_connect_only):
        """
        Sets the test_connect_only of this LdapTestConfigRequest. :param test_connect_only: The test_connect_only of this LdapTestConfigRequest.
        :type: bool
        """

        self._test_connect_only = test_connect_only

    @property
    def group_search_base(self):
        """
        Gets the group_search_base of this LdapTestConfigRequest. :return: The group_search_base of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._group_search_base

    @group_search_base.setter
    def group_search_base(self, group_search_base):
        """
        Sets the group_search_base of this LdapTestConfigRequest. :param group_search_base: The group_search_base of this LdapTestConfigRequest.
        :type: str
        """

        self._group_search_base = group_search_base

    @property
    def group_id_attribute(self):
        """
        Gets the group_id_attribute of this LdapTestConfigRequest. :return: The group_id_attribute of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._group_id_attribute

    @group_id_attribute.setter
    def group_id_attribute(self, group_id_attribute):
        """
        Sets the group_id_attribute of this LdapTestConfigRequest. :param group_id_attribute: The group_id_attribute of this LdapTestConfigRequest.
        :type: str
        """

        self._group_id_attribute = group_id_attribute

    @property
    def group_search_pattern(self):
        """
        Gets the group_search_pattern of this LdapTestConfigRequest. :return: The group_search_pattern of this LdapTestConfigRequest.
        :rtype: str
        """
        return self._group_search_pattern

    @group_search_pattern.setter
    def group_search_pattern(self, group_search_pattern):
        """
        Sets the group_search_pattern of this LdapTestConfigRequest. :param group_search_pattern: The group_search_pattern of this LdapTestConfigRequest.
        :type: str
        """

        self._group_search_pattern = group_search_pattern

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
