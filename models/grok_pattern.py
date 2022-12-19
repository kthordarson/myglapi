

from pprint import pformat
from six import iteritems
import re
class GrokPattern(object):
    def __init__(self, id=None, name=None, pattern=None, content_pack=None):
        """
        GrokPattern - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'Any', 'name': 'str', 'pattern': 'str', 'content_pack': 'str'
        }

        self.attribute_map = {
            'id': 'id', 'name': 'name', 'pattern': 'pattern', 'content_pack': 'content_pack'
        }

        self._id = id
        self._name = name
        self._pattern = pattern
        self._content_pack = content_pack

    @property
    def id(self):
        """
        Gets the id of this GrokPattern.        :return: The id of this GrokPattern.
        :rtype: Any
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GrokPattern.        :param id: The id of this GrokPattern.
        :type: Any
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GrokPattern.        :return: The name of this GrokPattern.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GrokPattern.        :param name: The name of this GrokPattern.
        :type: str
        """

        self._name = name

    @property
    def pattern(self):
        """
        Gets the pattern of this GrokPattern.        :return: The pattern of this GrokPattern.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this GrokPattern.        :param pattern: The pattern of this GrokPattern.
        :type: str
        """

        self._pattern = pattern

    @property
    def content_pack(self):
        """
        Gets the content_pack of this GrokPattern.        :return: The content_pack of this GrokPattern.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this GrokPattern.        :param content_pack: The content_pack of this GrokPattern.
        :type: str
        """

        self._content_pack = content_pack

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
