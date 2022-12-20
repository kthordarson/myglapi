

from pprint import pformat

import re
class SimulationRequest(object):
    def __init__(self, stream_id=None, message=None, input_id=None):
        """
        SimulationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'stream_id': 'str', 'message': 'object', 'input_id': 'str'}

        self.attribute_map = {'stream_id': 'stream_id', 'message': 'message', 'input_id': 'input_id'}

        self._stream_id = stream_id
        self._message = message
        self._input_id = input_id

    @property
    def stream_id(self):
        """
        Gets the stream_id of this SimulationRequest. :return: The stream_id of this SimulationRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this SimulationRequest. :param stream_id: The stream_id of this SimulationRequest.
        :type: str
        """

        self._stream_id = stream_id

    @property
    def message(self):
        """
        Gets the message of this SimulationRequest. :return: The message of this SimulationRequest.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SimulationRequest. :param message: The message of this SimulationRequest.
        :type: object
        """

        self._message = message

    @property
    def input_id(self):
        """
        Gets the input_id of this SimulationRequest. :return: The input_id of this SimulationRequest.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """
        Sets the input_id of this SimulationRequest. :param input_id: The input_id of this SimulationRequest.
        :type: str
        """

        self._input_id = input_id

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
