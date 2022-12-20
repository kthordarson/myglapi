

from pprint import pformat

import re
class DebugEvent(object):
    def __init__(self, node_id=None, date=None, text=None):
        """
        DebugEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'node_id': 'str', 'date': 'datetime', 'text': 'str'}

        self.attribute_map = {'node_id': 'node_id', 'date': 'date', 'text': 'text'}

        self._node_id = node_id
        self._date = date
        self._text = text

    @property
    def node_id(self):
        """
        Gets the node_id of this DebugEvent. :return: The node_id of this DebugEvent.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this DebugEvent. :param node_id: The node_id of this DebugEvent.
        :type: str
        """

        self._node_id = node_id

    @property
    def date(self):
        """
        Gets the date of this DebugEvent. :return: The date of this DebugEvent.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this DebugEvent. :param date: The date of this DebugEvent.
        :type: datetime
        """

        self._date = date

    @property
    def text(self):
        """
        Gets the text of this DebugEvent. :return: The text of this DebugEvent.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this DebugEvent. :param text: The text of this DebugEvent.
        :type: str
        """

        self._text = text

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
