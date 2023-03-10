

from pprint import pformat

import re
class SearchResponse(object):
    def __init__(self, to=None, fields=None, _from=None, time=None, query=None, messages=None, built_query=None, decoration_stats=None, total_results=None, used_indices=None):
        """
        SearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'to': 'datetime', 'fields': 'list[str]', '_from': 'datetime', 'time': 'int', 'query': 'str', 'messages': 'list[object]', 'built_query': 'str', 'decoration_stats': 'object', 'total_results': 'int', 'used_indices': 'list[object]'}

        self.attribute_map = {'to': 'to', 'fields': 'fields', '_from': 'from', 'time': 'time', 'query': 'query', 'messages': 'messages', 'built_query': 'built_query', 'decoration_stats': 'decoration_stats', 'total_results': 'total_results', 'used_indices': 'used_indices'}

        self._to = to
        self._fields = fields
        self.__from = _from
        self._time = time
        self._query = query
        self._messages = messages
        self._built_query = built_query
        self._decoration_stats = decoration_stats
        self._total_results = total_results
        self._used_indices = used_indices

    @property
    def to(self):
        """
        Gets the to of this SearchResponse. :return: The to of this SearchResponse.
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this SearchResponse. :param to: The to of this SearchResponse.
        :type: datetime
        """

        self._to = to

    @property
    def fields(self):
        """
        Gets the fields of this SearchResponse. :return: The fields of this SearchResponse.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this SearchResponse. :param fields: The fields of this SearchResponse.
        :type: list[str]
        """

        self._fields = fields

    @property
    def _from(self):
        """
        Gets the _from of this SearchResponse. :return: The _from of this SearchResponse.
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this SearchResponse. :param _from: The _from of this SearchResponse.
        :type: datetime
        """

        self.__from = _from

    @property
    def time(self):
        """
        Gets the time of this SearchResponse. :return: The time of this SearchResponse.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this SearchResponse. :param time: The time of this SearchResponse.
        :type: int
        """

        self._time = time

    @property
    def query(self):
        """
        Gets the query of this SearchResponse. :return: The query of this SearchResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchResponse. :param query: The query of this SearchResponse.
        :type: str
        """

        self._query = query

    @property
    def messages(self):
        """
        Gets the messages of this SearchResponse. :return: The messages of this SearchResponse.
        :rtype: list[object]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this SearchResponse. :param messages: The messages of this SearchResponse.
        :type: list[object]
        """

        self._messages = messages

    @property
    def built_query(self):
        """
        Gets the built_query of this SearchResponse. :return: The built_query of this SearchResponse.
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """
        Sets the built_query of this SearchResponse. :param built_query: The built_query of this SearchResponse.
        :type: str
        """

        self._built_query = built_query

    @property
    def decoration_stats(self):
        """
        Gets the decoration_stats of this SearchResponse. :return: The decoration_stats of this SearchResponse.
        :rtype: object
        """
        return self._decoration_stats

    @decoration_stats.setter
    def decoration_stats(self, decoration_stats):
        """
        Sets the decoration_stats of this SearchResponse. :param decoration_stats: The decoration_stats of this SearchResponse.
        :type: object
        """

        self._decoration_stats = decoration_stats

    @property
    def total_results(self):
        """
        Gets the total_results of this SearchResponse. :return: The total_results of this SearchResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """
        Sets the total_results of this SearchResponse. :param total_results: The total_results of this SearchResponse.
        :type: int
        """

        self._total_results = total_results

    @property
    def used_indices(self):
        """
        Gets the used_indices of this SearchResponse. :return: The used_indices of this SearchResponse.
        :rtype: list[object]
        """
        return self._used_indices

    @used_indices.setter
    def used_indices(self, used_indices):
        """
        Sets the used_indices of this SearchResponse. :param used_indices: The used_indices of this SearchResponse.
        :type: list[object]
        """

        self._used_indices = used_indices

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
