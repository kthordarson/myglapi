

from pprint import pformat

import re
class FieldStatsResult(object):
    def __init__(self, sum_of_squares=None, count=None, min=None, max=None, time=None, sum=None, cardinality=None, mean=None, built_query=None, variance=None, std_deviation=None):
        """
        FieldStatsResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'sum_of_squares': 'float', 'count': 'int', 'min': 'float', 'max': 'float', 'time': 'int', 'sum': 'float', 'cardinality': 'int', 'mean': 'float', 'built_query': 'str', 'variance': 'float', 'std_deviation': 'float'}

        self.attribute_map = {'sum_of_squares': 'sum_of_squares', 'count': 'count', 'min': 'min', 'max': 'max', 'time': 'time', 'sum': 'sum', 'cardinality': 'cardinality', 'mean': 'mean', 'built_query': 'built_query', 'variance': 'variance', 'std_deviation': 'std_deviation'}

        self._sum_of_squares = sum_of_squares
        self._count = count
        self._min = min
        self._max = max
        self._time = time
        self._sum = sum
        self._cardinality = cardinality
        self._mean = mean
        self._built_query = built_query
        self._variance = variance
        self._std_deviation = std_deviation

    @property
    def sum_of_squares(self):
        """
        Gets the sum_of_squares of this FieldStatsResult.        :return: The sum_of_squares of this FieldStatsResult.
        :rtype: float
        """
        return self._sum_of_squares

    @sum_of_squares.setter
    def sum_of_squares(self, sum_of_squares):
        """
        Sets the sum_of_squares of this FieldStatsResult.        :param sum_of_squares: The sum_of_squares of this FieldStatsResult.
        :type: float
        """

        self._sum_of_squares = sum_of_squares

    @property
    def count(self):
        """
        Gets the count of this FieldStatsResult.        :return: The count of this FieldStatsResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this FieldStatsResult.        :param count: The count of this FieldStatsResult.
        :type: int
        """

        self._count = count

    @property
    def min(self):
        """
        Gets the min of this FieldStatsResult.        :return: The min of this FieldStatsResult.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this FieldStatsResult.        :param min: The min of this FieldStatsResult.
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """
        Gets the max of this FieldStatsResult.        :return: The max of this FieldStatsResult.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this FieldStatsResult.        :param max: The max of this FieldStatsResult.
        :type: float
        """

        self._max = max

    @property
    def time(self):
        """
        Gets the time of this FieldStatsResult.        :return: The time of this FieldStatsResult.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this FieldStatsResult.        :param time: The time of this FieldStatsResult.
        :type: int
        """

        self._time = time

    @property
    def sum(self):
        """
        Gets the sum of this FieldStatsResult.        :return: The sum of this FieldStatsResult.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """
        Sets the sum of this FieldStatsResult.        :param sum: The sum of this FieldStatsResult.
        :type: float
        """

        self._sum = sum

    @property
    def cardinality(self):
        """
        Gets the cardinality of this FieldStatsResult.        :return: The cardinality of this FieldStatsResult.
        :rtype: int
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """
        Sets the cardinality of this FieldStatsResult.        :param cardinality: The cardinality of this FieldStatsResult.
        :type: int
        """

        self._cardinality = cardinality

    @property
    def mean(self):
        """
        Gets the mean of this FieldStatsResult.        :return: The mean of this FieldStatsResult.
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """
        Sets the mean of this FieldStatsResult.        :param mean: The mean of this FieldStatsResult.
        :type: float
        """

        self._mean = mean

    @property
    def built_query(self):
        """
        Gets the built_query of this FieldStatsResult.        :return: The built_query of this FieldStatsResult.
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """
        Sets the built_query of this FieldStatsResult.        :param built_query: The built_query of this FieldStatsResult.
        :type: str
        """

        self._built_query = built_query

    @property
    def variance(self):
        """
        Gets the variance of this FieldStatsResult.        :return: The variance of this FieldStatsResult.
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """
        Sets the variance of this FieldStatsResult.        :param variance: The variance of this FieldStatsResult.
        :type: float
        """

        self._variance = variance

    @property
    def std_deviation(self):
        """
        Gets the std_deviation of this FieldStatsResult.        :return: The std_deviation of this FieldStatsResult.
        :rtype: float
        """
        return self._std_deviation

    @std_deviation.setter
    def std_deviation(self, std_deviation):
        """
        Sets the std_deviation of this FieldStatsResult.        :param std_deviation: The std_deviation of this FieldStatsResult.
        :type: float
        """

        self._std_deviation = std_deviation

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
