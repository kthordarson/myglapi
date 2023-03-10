

from pprint import pformat

import re
class CreateOutputRequest(object):
    def __init__(self, title=None, type=None, configuration=None, streams=None, content_pack=None):
        """
        CreateOutputRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'title': 'str', 'type': 'str', 'configuration': 'object', 'streams': 'list[str]', 'content_pack': 'str'}

        self.attribute_map = {'title': 'title', 'type': 'type', 'configuration': 'configuration', 'streams': 'streams', 'content_pack': 'content_pack'}

        self._title = title
        self._type = type
        self._configuration = configuration
        self._streams = streams
        self._content_pack = content_pack

    @property
    def title(self):
        """
        Gets the title of this CreateOutputRequest. :return: The title of this CreateOutputRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateOutputRequest. :param title: The title of this CreateOutputRequest.
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this CreateOutputRequest. :return: The type of this CreateOutputRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateOutputRequest. :param type: The type of this CreateOutputRequest.
        :type: str
        """

        self._type = type

    @property
    def configuration(self):
        """
        Gets the configuration of this CreateOutputRequest. :return: The configuration of this CreateOutputRequest.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this CreateOutputRequest. :param configuration: The configuration of this CreateOutputRequest.
        :type: object
        """

        self._configuration = configuration

    @property
    def streams(self):
        """
        Gets the streams of this CreateOutputRequest. :return: The streams of this CreateOutputRequest.
        :rtype: list[str]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """
        Sets the streams of this CreateOutputRequest. :param streams: The streams of this CreateOutputRequest.
        :type: list[str]
        """

        self._streams = streams

    @property
    def content_pack(self):
        """
        Gets the content_pack of this CreateOutputRequest. :return: The content_pack of this CreateOutputRequest.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this CreateOutputRequest. :param content_pack: The content_pack of this CreateOutputRequest.
        :type: str
        """

        self._content_pack = content_pack

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
