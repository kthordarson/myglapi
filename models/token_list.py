

from pprint import pformat

import re
class TokenList(object):
    def __init__(self, tokens=None):
        """
        TokenList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'tokens': 'list[object]'}

        self.attribute_map = {'tokens': 'tokens'}

        self._tokens = tokens

    @property
    def tokens(self):
        """
        Gets the tokens of this TokenList.        :return: The tokens of this TokenList.
        :rtype: list[object]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """
        Sets the tokens of this TokenList.        :param tokens: The tokens of this TokenList.
        :type: list[object]
        """

        self._tokens = tokens

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
