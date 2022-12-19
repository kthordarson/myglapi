

from pprint import pformat

import re
class IndexerOverview(object):
    def __init__(self, indexer_cluster=None, counts=None, indices=None, deflector=None):
        """
        IndexerOverview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'indexer_cluster': 'object', 'counts': 'object', 'indices': 'object', 'deflector': 'object'}

        self.attribute_map = {'indexer_cluster': 'indexer_cluster', 'counts': 'counts', 'indices': 'indices', 'deflector': 'deflector'}

        self._indexer_cluster = indexer_cluster
        self._counts = counts
        self._indices = indices
        self._deflector = deflector

    @property
    def indexer_cluster(self):
        """
        Gets the indexer_cluster of this IndexerOverview.        :return: The indexer_cluster of this IndexerOverview.
        :rtype: object
        """
        return self._indexer_cluster

    @indexer_cluster.setter
    def indexer_cluster(self, indexer_cluster):
        """
        Sets the indexer_cluster of this IndexerOverview.        :param indexer_cluster: The indexer_cluster of this IndexerOverview.
        :type: object
        """

        self._indexer_cluster = indexer_cluster

    @property
    def counts(self):
        """
        Gets the counts of this IndexerOverview.        :return: The counts of this IndexerOverview.
        :rtype: object
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """
        Sets the counts of this IndexerOverview.        :param counts: The counts of this IndexerOverview.
        :type: object
        """

        self._counts = counts

    @property
    def indices(self):
        """
        Gets the indices of this IndexerOverview.        :return: The indices of this IndexerOverview.
        :rtype: object
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """
        Sets the indices of this IndexerOverview.        :param indices: The indices of this IndexerOverview.
        :type: object
        """

        self._indices = indices

    @property
    def deflector(self):
        """
        Gets the deflector of this IndexerOverview.        :return: The deflector of this IndexerOverview.
        :rtype: object
        """
        return self._deflector

    @deflector.setter
    def deflector(self, deflector):
        """
        Sets the deflector of this IndexerOverview.        :param deflector: The deflector of this IndexerOverview.
        :type: object
        """

        self._deflector = deflector

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
