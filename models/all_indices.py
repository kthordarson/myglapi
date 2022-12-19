from pprint import pformat
from six import iteritems
import re

class AllIndices(object):
    def __init__(self, closed=None, reopened=None, all=None):
        """
        AllIndices - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'closed': 'object', 'reopened': 'object', 'all': 'object'
        }

        self.attribute_map = {
            'closed': 'closed', 'reopened': 'reopened', 'all': 'all'
        }

        self._closed = closed
        self._reopened = reopened
        self._all = all

    @property
    def closed(self):
        """
        Gets the closed of this AllIndices.        :return: The closed of this AllIndices.
        :rtype: object
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """
        Sets the closed of this AllIndices.        :param closed: The closed of this AllIndices.
        :type: object
        """

        self._closed = closed

    @property
    def reopened(self):
        """
        Gets the reopened of this AllIndices.        :return: The reopened of this AllIndices.
        :rtype: object
        """
        return self._reopened

    @reopened.setter
    def reopened(self, reopened):
        """
        Sets the reopened of this AllIndices.        :param reopened: The reopened of this AllIndices.
        :type: object
        """

        self._reopened = reopened

    @property
    def all(self):
        """
        Gets the all of this AllIndices.        :return: The all of this AllIndices.
        :rtype: object
        """
        return self._all

    @all.setter
    def all(self, all):
        """
        Sets the all of this AllIndices.        :param all: The all of this AllIndices.
        :type: object
        """

        self._all = all

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
