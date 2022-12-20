

from pprint import pformat

import re
class SimulationResponse(object):
    def __init__(self, messages=None, simulation_trace=None, took_microseconds=None):
        """
        SimulationResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'messages': 'list[object]', 'simulation_trace': 'list[object]', 'took_microseconds': 'int'}

        self.attribute_map = {'messages': 'messages', 'simulation_trace': 'simulation_trace', 'took_microseconds': 'took_microseconds'}

        self._messages = messages
        self._simulation_trace = simulation_trace
        self._took_microseconds = took_microseconds

    @property
    def messages(self):
        """
        Gets the messages of this SimulationResponse. :return: The messages of this SimulationResponse.
        :rtype: list[object]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this SimulationResponse. :param messages: The messages of this SimulationResponse.
        :type: list[object]
        """

        self._messages = messages

    @property
    def simulation_trace(self):
        """
        Gets the simulation_trace of this SimulationResponse. :return: The simulation_trace of this SimulationResponse.
        :rtype: list[object]
        """
        return self._simulation_trace

    @simulation_trace.setter
    def simulation_trace(self, simulation_trace):
        """
        Sets the simulation_trace of this SimulationResponse. :param simulation_trace: The simulation_trace of this SimulationResponse.
        :type: list[object]
        """

        self._simulation_trace = simulation_trace

    @property
    def took_microseconds(self):
        """
        Gets the took_microseconds of this SimulationResponse. :return: The took_microseconds of this SimulationResponse.
        :rtype: int
        """
        return self._took_microseconds

    @took_microseconds.setter
    def took_microseconds(self, took_microseconds):
        """
        Sets the took_microseconds of this SimulationResponse. :param took_microseconds: The took_microseconds of this SimulationResponse.
        :type: int
        """

        self._took_microseconds = took_microseconds

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
