

from pprint import pformat

import re
class DecoratorImpl(object):
    def __init__(self, type=None, config=None, stream=None, order=None, id=None):
        """
        DecoratorImpl - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'type': 'str', 'config': 'object', 'stream': 'str', 'order': 'int', 'id': 'str'}

        self.attribute_map = {'type': 'type', 'config': 'config', 'stream': 'stream', 'order': 'order', 'id': 'id'}

        self._type = type
        self._config = config
        self._stream = stream
        self._order = order
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this DecoratorImpl. :return: The type of this DecoratorImpl.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DecoratorImpl. :param type: The type of this DecoratorImpl.
        :type: str
        """

        self._type = type

    @property
    def config(self):
        """
        Gets the config of this DecoratorImpl. :return: The config of this DecoratorImpl.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this DecoratorImpl. :param config: The config of this DecoratorImpl.
        :type: object
        """

        self._config = config

    @property
    def stream(self):
        """
        Gets the stream of this DecoratorImpl. :return: The stream of this DecoratorImpl.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """
        Sets the stream of this DecoratorImpl. :param stream: The stream of this DecoratorImpl.
        :type: str
        """

        self._stream = stream

    @property
    def order(self):
        """
        Gets the order of this DecoratorImpl. :return: The order of this DecoratorImpl.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this DecoratorImpl. :param order: The order of this DecoratorImpl.
        :type: int
        """

        self._order = order

    @property
    def id(self):
        """
        Gets the id of this DecoratorImpl. :return: The id of this DecoratorImpl.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DecoratorImpl. :param id: The id of this DecoratorImpl.
        :type: str
        """

        self._id = id

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
