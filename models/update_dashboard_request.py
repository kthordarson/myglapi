

from pprint import pformat

import re
class UpdateDashboardRequest(object):
    def __init__(self, title=None, description=None):
        """
        UpdateDashboardRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'title': 'str', 'description': 'str'}

        self.attribute_map = {'title': 'title', 'description': 'description'}

        self._title = title
        self._description = description

    @property
    def title(self):
        """
        Gets the title of this UpdateDashboardRequest. :return: The title of this UpdateDashboardRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this UpdateDashboardRequest. :param title: The title of this UpdateDashboardRequest.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this UpdateDashboardRequest. :return: The description of this UpdateDashboardRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDashboardRequest. :param description: The description of this UpdateDashboardRequest.
        :type: str
        """

        self._description = description

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
