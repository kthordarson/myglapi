

from pprint import pformat

import re
class TermsResult(object):
    def __init__(self, total=None, other=None, time=None, missing=None, terms=None, built_query=None):
        """
        TermsResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'total': 'int', 'other': 'int', 'time': 'int', 'missing': 'int', 'terms': 'object', 'built_query': 'str'}

        self.attribute_map = {'total': 'total', 'other': 'other', 'time': 'time', 'missing': 'missing', 'terms': 'terms', 'built_query': 'built_query'}

        self._total = total
        self._other = other
        self._time = time
        self._missing = missing
        self._terms = terms
        self._built_query = built_query

    @property
    def total(self):
        """
        Gets the total of this TermsResult. :return: The total of this TermsResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this TermsResult. :param total: The total of this TermsResult.
        :type: int
        """

        self._total = total

    @property
    def other(self):
        """
        Gets the other of this TermsResult. :return: The other of this TermsResult.
        :rtype: int
        """
        return self._other

    @other.setter
    def other(self, other):
        """
        Sets the other of this TermsResult. :param other: The other of this TermsResult.
        :type: int
        """

        self._other = other

    @property
    def time(self):
        """
        Gets the time of this TermsResult. :return: The time of this TermsResult.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this TermsResult. :param time: The time of this TermsResult.
        :type: int
        """

        self._time = time

    @property
    def missing(self):
        """
        Gets the missing of this TermsResult. :return: The missing of this TermsResult.
        :rtype: int
        """
        return self._missing

    @missing.setter
    def missing(self, missing):
        """
        Sets the missing of this TermsResult. :param missing: The missing of this TermsResult.
        :type: int
        """

        self._missing = missing

    @property
    def terms(self):
        """
        Gets the terms of this TermsResult. :return: The terms of this TermsResult.
        :rtype: object
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this TermsResult. :param terms: The terms of this TermsResult.
        :type: object
        """

        self._terms = terms

    @property
    def built_query(self):
        """
        Gets the built_query of this TermsResult. :return: The built_query of this TermsResult.
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """
        Sets the built_query of this TermsResult. :param built_query: The built_query of this TermsResult.
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
