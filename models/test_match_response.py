

from pprint import pformat

import re
class TestMatchResponse(object):
    def __init__(self, matches=None, rules=None):
        """
        TestMatchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'matches': 'bool', 'rules': 'object'}

        self.attribute_map = {'matches': 'matches', 'rules': 'rules'}

        self._matches = matches
        self._rules = rules

    @property
    def matches(self):
        """
        Gets the matches of this TestMatchResponse. :return: The matches of this TestMatchResponse.
        :rtype: bool
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """
        Sets the matches of this TestMatchResponse. :param matches: The matches of this TestMatchResponse.
        :type: bool
        """

        self._matches = matches

    @property
    def rules(self):
        """
        Gets the rules of this TestMatchResponse. :return: The rules of this TestMatchResponse.
        :rtype: object
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this TestMatchResponse. :param rules: The rules of this TestMatchResponse.
        :type: object
        """

        self._rules = rules

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
