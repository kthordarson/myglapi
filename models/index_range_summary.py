

from pprint import pformat

import re
class IndexRangeSummary(object):
    def __init__(self, index_name=None, begin=None, end=None, calculated_at=None, took_ms=None):
        """
        IndexRangeSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'index_name': 'str', 'begin': 'datetime', 'end': 'datetime', 'calculated_at': 'datetime', 'took_ms': 'int'}

        self.attribute_map = {'index_name': 'index_name', 'begin': 'begin', 'end': 'end', 'calculated_at': 'calculated_at', 'took_ms': 'took_ms'}

        self._index_name = index_name
        self._begin = begin
        self._end = end
        self._calculated_at = calculated_at
        self._took_ms = took_ms

    @property
    def index_name(self):
        """
        Gets the index_name of this IndexRangeSummary. :return: The index_name of this IndexRangeSummary.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """
        Sets the index_name of this IndexRangeSummary. :param index_name: The index_name of this IndexRangeSummary.
        :type: str
        """

        self._index_name = index_name

    @property
    def begin(self):
        """
        Gets the begin of this IndexRangeSummary. :return: The begin of this IndexRangeSummary.
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """
        Sets the begin of this IndexRangeSummary. :param begin: The begin of this IndexRangeSummary.
        :type: datetime
        """

        self._begin = begin

    @property
    def end(self):
        """
        Gets the end of this IndexRangeSummary. :return: The end of this IndexRangeSummary.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this IndexRangeSummary. :param end: The end of this IndexRangeSummary.
        :type: datetime
        """

        self._end = end

    @property
    def calculated_at(self):
        """
        Gets the calculated_at of this IndexRangeSummary. :return: The calculated_at of this IndexRangeSummary.
        :rtype: datetime
        """
        return self._calculated_at

    @calculated_at.setter
    def calculated_at(self, calculated_at):
        """
        Sets the calculated_at of this IndexRangeSummary. :param calculated_at: The calculated_at of this IndexRangeSummary.
        :type: datetime
        """

        self._calculated_at = calculated_at

    @property
    def took_ms(self):
        """
        Gets the took_ms of this IndexRangeSummary. :return: The took_ms of this IndexRangeSummary.
        :rtype: int
        """
        return self._took_ms

    @took_ms.setter
    def took_ms(self, took_ms):
        """
        Sets the took_ms of this IndexRangeSummary. :param took_ms: The took_ms of this IndexRangeSummary.
        :type: int
        """

        self._took_ms = took_ms

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
