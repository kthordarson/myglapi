

from pprint import pformat
from six import iteritems
import re
class InputCreateRequest(object):
    def __init__(self, title=None, type=None, _global=None, configuration=None, node=None):
        """
        InputCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'title': 'str', 'type': 'str', '_global': 'bool', 'configuration': 'object', 'node': 'str'
        }

        self.attribute_map = {
            'title': 'title', 'type': 'type', '_global': 'global', 'configuration': 'configuration', 'node': 'node'
        }

        self._title = title
        self._type = type
        self.__global = _global
        self._configuration = configuration
        self._node = node

    @property
    def title(self):
        """
        Gets the title of this InputCreateRequest.        :return: The title of this InputCreateRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this InputCreateRequest.        :param title: The title of this InputCreateRequest.
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this InputCreateRequest.        :return: The type of this InputCreateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InputCreateRequest.        :param type: The type of this InputCreateRequest.
        :type: str
        """

        self._type = type

    @property
    def _global(self):
        """
        Gets the _global of this InputCreateRequest.        :return: The _global of this InputCreateRequest.
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """
        Sets the _global of this InputCreateRequest.        :param _global: The _global of this InputCreateRequest.
        :type: bool
        """

        self.__global = _global

    @property
    def configuration(self):
        """
        Gets the configuration of this InputCreateRequest.        :return: The configuration of this InputCreateRequest.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this InputCreateRequest.        :param configuration: The configuration of this InputCreateRequest.
        :type: object
        """

        self._configuration = configuration

    @property
    def node(self):
        """
        Gets the node of this InputCreateRequest.        :return: The node of this InputCreateRequest.
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """
        Sets the node of this InputCreateRequest.        :param node: The node of this InputCreateRequest.
        :type: str
        """

        self._node = node

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
