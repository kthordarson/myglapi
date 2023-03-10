

from pprint import pformat

import re
class MessageProcessorsConfigWithDescriptors(object):
    def __init__(self, processor_order=None, disabled_processors=None):
        """
        MessageProcessorsConfigWithDescriptors - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'processor_order': 'list[object]', 'disabled_processors': 'list[str]'}

        self.attribute_map = {'processor_order': 'processor_order', 'disabled_processors': 'disabled_processors'}

        self._processor_order = processor_order
        self._disabled_processors = disabled_processors

    @property
    def processor_order(self):
        """
        Gets the processor_order of this MessageProcessorsConfigWithDescriptors. :return: The processor_order of this MessageProcessorsConfigWithDescriptors.
        :rtype: list[object]
        """
        return self._processor_order

    @processor_order.setter
    def processor_order(self, processor_order):
        """
        Sets the processor_order of this MessageProcessorsConfigWithDescriptors. :param processor_order: The processor_order of this MessageProcessorsConfigWithDescriptors.
        :type: list[object]
        """

        self._processor_order = processor_order

    @property
    def disabled_processors(self):
        """
        Gets the disabled_processors of this MessageProcessorsConfigWithDescriptors. :return: The disabled_processors of this MessageProcessorsConfigWithDescriptors.
        :rtype: list[str]
        """
        return self._disabled_processors

    @disabled_processors.setter
    def disabled_processors(self, disabled_processors):
        """
        Sets the disabled_processors of this MessageProcessorsConfigWithDescriptors. :param disabled_processors: The disabled_processors of this MessageProcessorsConfigWithDescriptors.
        :type: list[str]
        """

        self._disabled_processors = disabled_processors

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
