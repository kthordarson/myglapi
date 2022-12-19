

from pprint import pformat

import re
class SessionValidationResponse(object):
    def __init__(self, is_valid=None, session_id=None, username=None):
        """
        SessionValidationResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'is_valid': 'bool', 'session_id': 'str', 'username': 'str'}

        self.attribute_map = {'is_valid': 'is_valid', 'session_id': 'session_id', 'username': 'username'}

        self._is_valid = is_valid
        self._session_id = session_id
        self._username = username

    @property
    def is_valid(self):
        """
        Gets the is_valid of this SessionValidationResponse.        :return: The is_valid of this SessionValidationResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """
        Sets the is_valid of this SessionValidationResponse.        :param is_valid: The is_valid of this SessionValidationResponse.
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def session_id(self):
        """
        Gets the session_id of this SessionValidationResponse.        :return: The session_id of this SessionValidationResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this SessionValidationResponse.        :param session_id: The session_id of this SessionValidationResponse.
        :type: str
        """

        self._session_id = session_id

    @property
    def username(self):
        """
        Gets the username of this SessionValidationResponse.        :return: The username of this SessionValidationResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SessionValidationResponse.        :param username: The username of this SessionValidationResponse.
        :type: str
        """

        self._username = username

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
