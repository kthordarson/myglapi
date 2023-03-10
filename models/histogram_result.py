

from pprint import pformat

import re
class HistogramResult(object):
    def __init__(self, queried_timerange=None, interval=None, time=None, results=None, built_query=None):
        """
        HistogramResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'queried_timerange': 'object', 'interval': 'str', 'time': 'int', 'results': 'object', 'built_query': 'str'}

        self.attribute_map = {'queried_timerange': 'queried_timerange', 'interval': 'interval', 'time': 'time', 'results': 'results', 'built_query': 'built_query'}

        self._queried_timerange = queried_timerange
        self._interval = interval
        self._time = time
        self._results = results
        self._built_query = built_query

    @property
    def queried_timerange(self):
        """
        Gets the queried_timerange of this HistogramResult. :return: The queried_timerange of this HistogramResult.
        :rtype: object
        """
        return self._queried_timerange

    @queried_timerange.setter
    def queried_timerange(self, queried_timerange):
        """
        Sets the queried_timerange of this HistogramResult. :param queried_timerange: The queried_timerange of this HistogramResult.
        :type: object
        """

        self._queried_timerange = queried_timerange

    @property
    def interval(self):
        """
        Gets the interval of this HistogramResult. :return: The interval of this HistogramResult.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this HistogramResult. :param interval: The interval of this HistogramResult.
        :type: str
        """

        self._interval = interval

    @property
    def time(self):
        """
        Gets the time of this HistogramResult. :return: The time of this HistogramResult.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this HistogramResult. :param time: The time of this HistogramResult.
        :type: int
        """

        self._time = time

    @property
    def results(self):
        """
        Gets the results of this HistogramResult. :return: The results of this HistogramResult.
        :rtype: object
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this HistogramResult. :param results: The results of this HistogramResult.
        :type: object
        """

        self._results = results

    @property
    def built_query(self):
        """
        Gets the built_query of this HistogramResult. :return: The built_query of this HistogramResult.
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """
        Sets the built_query of this HistogramResult. :param built_query: The built_query of this HistogramResult.
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
