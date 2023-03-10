

from pprint import pformat

import re
class InputTypeInfo(object):
    def __init__(self, type=None, name=None, is_exclusive=None, requested_configuration=None, link_to_docs=None):
        """
        InputTypeInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'type': 'str', 'name': 'str', 'is_exclusive': 'bool', 'requested_configuration': 'object', 'link_to_docs': 'str'}

        self.attribute_map = {'type': 'type', 'name': 'name', 'is_exclusive': 'is_exclusive', 'requested_configuration': 'requested_configuration', 'link_to_docs': 'link_to_docs'}

        self._type = type
        self._name = name
        self._is_exclusive = is_exclusive
        self._requested_configuration = requested_configuration
        self._link_to_docs = link_to_docs

    @property
    def type(self):
        """
        Gets the type of this InputTypeInfo. :return: The type of this InputTypeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InputTypeInfo. :param type: The type of this InputTypeInfo.
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this InputTypeInfo. :return: The name of this InputTypeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InputTypeInfo. :param name: The name of this InputTypeInfo.
        :type: str
        """

        self._name = name

    @property
    def is_exclusive(self):
        """
        Gets the is_exclusive of this InputTypeInfo. :return: The is_exclusive of this InputTypeInfo.
        :rtype: bool
        """
        return self._is_exclusive

    @is_exclusive.setter
    def is_exclusive(self, is_exclusive):
        """
        Sets the is_exclusive of this InputTypeInfo. :param is_exclusive: The is_exclusive of this InputTypeInfo.
        :type: bool
        """

        self._is_exclusive = is_exclusive

    @property
    def requested_configuration(self):
        """
        Gets the requested_configuration of this InputTypeInfo. :return: The requested_configuration of this InputTypeInfo.
        :rtype: object
        """
        return self._requested_configuration

    @requested_configuration.setter
    def requested_configuration(self, requested_configuration):
        """
        Sets the requested_configuration of this InputTypeInfo. :param requested_configuration: The requested_configuration of this InputTypeInfo.
        :type: object
        """

        self._requested_configuration = requested_configuration

    @property
    def link_to_docs(self):
        """
        Gets the link_to_docs of this InputTypeInfo. :return: The link_to_docs of this InputTypeInfo.
        :rtype: str
        """
        return self._link_to_docs

    @link_to_docs.setter
    def link_to_docs(self, link_to_docs):
        """
        Sets the link_to_docs of this InputTypeInfo. :param link_to_docs: The link_to_docs of this InputTypeInfo.
        :type: str
        """

        self._link_to_docs = link_to_docs

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
