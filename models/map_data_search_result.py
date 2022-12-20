

from pprint import pformat

import re
class MapDataSearchResult(object):
    def __init__(self, query=None, timerange=None, limit=None, stream_id=None, fields=None):
        """
        MapDataSearchResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'query': 'str', 'timerange': 'object', 'limit': 'int', 'stream_id': 'str', 'fields': 'object'}

        self.attribute_map = {'query': 'query', 'timerange': 'timerange', 'limit': 'limit', 'stream_id': 'stream_id', 'fields': 'fields'}

        self._query = query
        self._timerange = timerange
        self._limit = limit
        self._stream_id = stream_id
        self._fields = fields

    @property
    def query(self):
        """
        Gets the query of this MapDataSearchResult. :return: The query of this MapDataSearchResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this MapDataSearchResult. :param query: The query of this MapDataSearchResult.
        :type: str
        """

        self._query = query

    @property
    def timerange(self):
        """
        Gets the timerange of this MapDataSearchResult. :return: The timerange of this MapDataSearchResult.
        :rtype: object
        """
        return self._timerange

    @timerange.setter
    def timerange(self, timerange):
        """
        Sets the timerange of this MapDataSearchResult. :param timerange: The timerange of this MapDataSearchResult.
        :type: object
        """

        self._timerange = timerange

    @property
    def limit(self):
        """
        Gets the limit of this MapDataSearchResult. :return: The limit of this MapDataSearchResult.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this MapDataSearchResult. :param limit: The limit of this MapDataSearchResult.
        :type: int
        """

        self._limit = limit

    @property
    def stream_id(self):
        """
        Gets the stream_id of this MapDataSearchResult. :return: The stream_id of this MapDataSearchResult.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this MapDataSearchResult. :param stream_id: The stream_id of this MapDataSearchResult.
        :type: str
        """

        self._stream_id = stream_id

    @property
    def fields(self):
        """
        Gets the fields of this MapDataSearchResult. :return: The fields of this MapDataSearchResult.
        :rtype: object
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this MapDataSearchResult. :param fields: The fields of this MapDataSearchResult.
        :type: object
        """

        self._fields = fields

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
