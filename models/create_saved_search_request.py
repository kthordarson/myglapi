

from pprint import pformat

import re
class CreateSavedSearchRequest(object):
    def __init__(self, title=None, query=None):
        """
        CreateSavedSearchRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'title': 'str', 'query': 'object'}

        self.attribute_map = {'title': 'title', 'query': 'query'}

        self._title = title
        self._query = query

    @property
    def title(self):
        """
        Gets the title of this CreateSavedSearchRequest.        :return: The title of this CreateSavedSearchRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateSavedSearchRequest.        :param title: The title of this CreateSavedSearchRequest.
        :type: str
        """

        self._title = title

    @property
    def query(self):
        """
        Gets the query of this CreateSavedSearchRequest.        :return: The query of this CreateSavedSearchRequest.
        :rtype: object
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this CreateSavedSearchRequest.        :param query: The query of this CreateSavedSearchRequest.
        :type: object
        """

        self._query = query

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
