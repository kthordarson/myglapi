

from pprint import pformat

import re
class CreateStreamRequest(object):
    def __init__(self, title=None, description=None, rules=None, content_pack=None, matching_type=None):
        """
        CreateStreamRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'title': 'str', 'description': 'str', 'rules': 'list[object]', 'content_pack': 'str', 'matching_type': 'str'}

        self.attribute_map = {'title': 'title', 'description': 'description', 'rules': 'rules', 'content_pack': 'content_pack', 'matching_type': 'matching_type'}

        self._title = title
        self._description = description
        self._rules = rules
        self._content_pack = content_pack
        self._matching_type = matching_type

    @property
    def title(self):
        """
        Gets the title of this CreateStreamRequest. :return: The title of this CreateStreamRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateStreamRequest. :param title: The title of this CreateStreamRequest.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this CreateStreamRequest. :return: The description of this CreateStreamRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateStreamRequest. :param description: The description of this CreateStreamRequest.
        :type: str
        """

        self._description = description

    @property
    def rules(self):
        """
        Gets the rules of this CreateStreamRequest. :return: The rules of this CreateStreamRequest.
        :rtype: list[object]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this CreateStreamRequest. :param rules: The rules of this CreateStreamRequest.
        :type: list[object]
        """

        self._rules = rules

    @property
    def content_pack(self):
        """
        Gets the content_pack of this CreateStreamRequest. :return: The content_pack of this CreateStreamRequest.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this CreateStreamRequest. :param content_pack: The content_pack of this CreateStreamRequest.
        :type: str
        """

        self._content_pack = content_pack

    @property
    def matching_type(self):
        """
        Gets the matching_type of this CreateStreamRequest. :return: The matching_type of this CreateStreamRequest.
        :rtype: str
        """
        return self._matching_type

    @matching_type.setter
    def matching_type(self, matching_type):
        """
        Sets the matching_type of this CreateStreamRequest. :param matching_type: The matching_type of this CreateStreamRequest.
        :type: str
        """
        allowed_values = ["AND", "OR"]
        if matching_type not in allowed_values:
            raise ValueError(
                "Invalid value for `matching_type` ({0}), must be one of {1}"
                .format(matching_type, allowed_values)
            )

        self._matching_type = matching_type

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
