

from pprint import pformat

import re
class ConfigurationBundle(object):
    def __init__(self, id=None, name=None, description=None, category=None, inputs=None, streams=None, outputs=None, dashboards=None, grok_patterns=None):
        """
        ConfigurationBundle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'name': 'str', 'description': 'str', 'category': 'str', 'inputs': 'list[object]', 'streams': 'list[object]', 'outputs': 'list[object]', 'dashboards': 'list[object]', 'grok_patterns': 'list[object]'}

        self.attribute_map = {'id': 'id', 'name': 'name', 'description': 'description', 'category': 'category', 'inputs': 'inputs', 'streams': 'streams', 'outputs': 'outputs', 'dashboards': 'dashboards', 'grok_patterns': 'grok_patterns'}

        self._id = id
        self._name = name
        self._description = description
        self._category = category
        self._inputs = inputs
        self._streams = streams
        self._outputs = outputs
        self._dashboards = dashboards
        self._grok_patterns = grok_patterns

    @property
    def id(self):
        """
        Gets the id of this ConfigurationBundle. :return: The id of this ConfigurationBundle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConfigurationBundle. :param id: The id of this ConfigurationBundle.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ConfigurationBundle. :return: The name of this ConfigurationBundle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConfigurationBundle. :param name: The name of this ConfigurationBundle.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ConfigurationBundle. :return: The description of this ConfigurationBundle.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationBundle. :param description: The description of this ConfigurationBundle.
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """
        Gets the category of this ConfigurationBundle. :return: The category of this ConfigurationBundle.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ConfigurationBundle. :param category: The category of this ConfigurationBundle.
        :type: str
        """

        self._category = category

    @property
    def inputs(self):
        """
        Gets the inputs of this ConfigurationBundle. :return: The inputs of this ConfigurationBundle.
        :rtype: list[object]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this ConfigurationBundle. :param inputs: The inputs of this ConfigurationBundle.
        :type: list[object]
        """

        self._inputs = inputs

    @property
    def streams(self):
        """
        Gets the streams of this ConfigurationBundle. :return: The streams of this ConfigurationBundle.
        :rtype: list[object]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """
        Sets the streams of this ConfigurationBundle. :param streams: The streams of this ConfigurationBundle.
        :type: list[object]
        """

        self._streams = streams

    @property
    def outputs(self):
        """
        Gets the outputs of this ConfigurationBundle. :return: The outputs of this ConfigurationBundle.
        :rtype: list[object]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this ConfigurationBundle. :param outputs: The outputs of this ConfigurationBundle.
        :type: list[object]
        """

        self._outputs = outputs

    @property
    def dashboards(self):
        """
        Gets the dashboards of this ConfigurationBundle. :return: The dashboards of this ConfigurationBundle.
        :rtype: list[object]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """
        Sets the dashboards of this ConfigurationBundle. :param dashboards: The dashboards of this ConfigurationBundle.
        :type: list[object]
        """

        self._dashboards = dashboards

    @property
    def grok_patterns(self):
        """
        Gets the grok_patterns of this ConfigurationBundle. :return: The grok_patterns of this ConfigurationBundle.
        :rtype: list[object]
        """
        return self._grok_patterns

    @grok_patterns.setter
    def grok_patterns(self, grok_patterns):
        """
        Sets the grok_patterns of this ConfigurationBundle. :param grok_patterns: The grok_patterns of this ConfigurationBundle.
        :type: list[object]
        """

        self._grok_patterns = grok_patterns

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
