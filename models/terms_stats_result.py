

from pprint import pformat

import re
class TermsStatsResult(object):
    def __init__(self, time=None, terms=None, built_query=None):
        """
        TermsStatsResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'time': 'int', 'terms': 'list[object]', 'built_query': 'str'}

        self.attribute_map = {'time': 'time', 'terms': 'terms', 'built_query': 'built_query'}

        self._time = time
        self._terms = terms
        self._built_query = built_query

    @property
    def time(self):
        """
        Gets the time of this TermsStatsResult. :return: The time of this TermsStatsResult.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this TermsStatsResult. :param time: The time of this TermsStatsResult.
        :type: int
        """

        self._time = time

    @property
    def terms(self):
        """
        Gets the terms of this TermsStatsResult. :return: The terms of this TermsStatsResult.
        :rtype: list[object]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this TermsStatsResult. :param terms: The terms of this TermsStatsResult.
        :type: list[object]
        """

        self._terms = terms

    @property
    def built_query(self):
        """
        Gets the built_query of this TermsStatsResult. :return: The built_query of this TermsStatsResult.
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """
        Sets the built_query of this TermsStatsResult. :param built_query: The built_query of this TermsStatsResult.
        :type: str
        """

        self._built_query = built_query

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
