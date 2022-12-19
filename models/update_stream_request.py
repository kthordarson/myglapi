

from pprint import pformat
from six import iteritems
import re
class UpdateStreamRequest(object):
    def __init__(self, title=None, description=None, matching_type=None):
        """
        UpdateStreamRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'title': 'str', 'description': 'str', 'matching_type': 'str'
        }

        self.attribute_map = {
            'title': 'title', 'description': 'description', 'matching_type': 'matching_type'
        }

        self._title = title
        self._description = description
        self._matching_type = matching_type

    @property
    def title(self):
        """
        Gets the title of this UpdateStreamRequest.        :return: The title of this UpdateStreamRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this UpdateStreamRequest.        :param title: The title of this UpdateStreamRequest.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this UpdateStreamRequest.        :return: The description of this UpdateStreamRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateStreamRequest.        :param description: The description of this UpdateStreamRequest.
        :type: str
        """

        self._description = description

    @property
    def matching_type(self):
        """
        Gets the matching_type of this UpdateStreamRequest.        :return: The matching_type of this UpdateStreamRequest.
        :rtype: str
        """
        return self._matching_type

    @matching_type.setter
    def matching_type(self, matching_type):
        """
        Sets the matching_type of this UpdateStreamRequest.        :param matching_type: The matching_type of this UpdateStreamRequest.
        :type: str
        """

        self._matching_type = matching_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
