

from pprint import pformat
from six import iteritems
import re
class MessageParseRequest(object):
    def __init__(self, message=None, codec=None, remote_address=None, configuration=None):
        """
        MessageParseRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str', 'codec': 'str', 'remote_address': 'str', 'configuration': 'object'
        }

        self.attribute_map = {
            'message': 'message', 'codec': 'codec', 'remote_address': 'remote_address', 'configuration': 'configuration'
        }

        self._message = message
        self._codec = codec
        self._remote_address = remote_address
        self._configuration = configuration

    @property
    def message(self):
        """
        Gets the message of this MessageParseRequest.        :return: The message of this MessageParseRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this MessageParseRequest.        :param message: The message of this MessageParseRequest.
        :type: str
        """

        self._message = message

    @property
    def codec(self):
        """
        Gets the codec of this MessageParseRequest.        :return: The codec of this MessageParseRequest.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """
        Sets the codec of this MessageParseRequest.        :param codec: The codec of this MessageParseRequest.
        :type: str
        """

        self._codec = codec

    @property
    def remote_address(self):
        """
        Gets the remote_address of this MessageParseRequest.        :return: The remote_address of this MessageParseRequest.
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """
        Sets the remote_address of this MessageParseRequest.        :param remote_address: The remote_address of this MessageParseRequest.
        :type: str
        """

        self._remote_address = remote_address

    @property
    def configuration(self):
        """
        Gets the configuration of this MessageParseRequest.        :return: The configuration of this MessageParseRequest.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this MessageParseRequest.        :param configuration: The configuration of this MessageParseRequest.
        :type: object
        """

        self._configuration = configuration

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
