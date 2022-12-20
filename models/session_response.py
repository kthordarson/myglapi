

from pprint import pformat

import re
class SessionResponse(object):
    def __init__(self, valid_until=None, session_id=None):
        """
        SessionResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'valid_until': 'datetime', 'session_id': 'str'}

        self.attribute_map = {'valid_until': 'valid_until', 'session_id': 'session_id'}

        self._valid_until = valid_until
        self._session_id = session_id

    @property
    def valid_until(self):
        """
        Gets the valid_until of this SessionResponse. :return: The valid_until of this SessionResponse.
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """
        Sets the valid_until of this SessionResponse. :param valid_until: The valid_until of this SessionResponse.
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def session_id(self):
        """
        Gets the session_id of this SessionResponse. :return: The session_id of this SessionResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this SessionResponse. :param session_id: The session_id of this SessionResponse.
        :type: str
        """

        self._session_id = session_id

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
