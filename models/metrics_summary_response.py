

from pprint import pformat
from six import iteritems
import re
class MetricsSummaryResponse(object):
    def __init__(self, total=None, metrics=None):
        """
        MetricsSummaryResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int', 'metrics': 'list[object]'
        }

        self.attribute_map = {
            'total': 'total', 'metrics': 'metrics'
        }

        self._total = total
        self._metrics = metrics

    @property
    def total(self):
        """
        Gets the total of this MetricsSummaryResponse.        :return: The total of this MetricsSummaryResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this MetricsSummaryResponse.        :param total: The total of this MetricsSummaryResponse.
        :type: int
        """

        self._total = total

    @property
    def metrics(self):
        """
        Gets the metrics of this MetricsSummaryResponse.        :return: The metrics of this MetricsSummaryResponse.
        :rtype: list[object]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this MetricsSummaryResponse.        :param metrics: The metrics of this MetricsSummaryResponse.
        :type: list[object]
        """

        self._metrics = metrics

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
