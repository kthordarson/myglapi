

from pprint import pformat

import re
class ExportBundle(object):
    def __init__(self, name=None, description=None, category=None, inputs=None, streams=None, outputs=None, dashboards=None, grok_patterns=None):
        """
        ExportBundle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'name': 'str', 'description': 'str', 'category': 'str', 'inputs': 'list[str]', 'streams': 'list[str]', 'outputs': 'list[str]', 'dashboards': 'list[str]', 'grok_patterns': 'list[str]'}

        self.attribute_map = {'name': 'name', 'description': 'description', 'category': 'category', 'inputs': 'inputs', 'streams': 'streams', 'outputs': 'outputs', 'dashboards': 'dashboards', 'grok_patterns': 'grok_patterns'}

        self._name = name
        self._description = description
        self._category = category
        self._inputs = inputs
        self._streams = streams
        self._outputs = outputs
        self._dashboards = dashboards
        self._grok_patterns = grok_patterns

    @property
    def name(self):
        """
        Gets the name of this ExportBundle. :return: The name of this ExportBundle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExportBundle. :param name: The name of this ExportBundle.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ExportBundle. :return: The description of this ExportBundle.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExportBundle. :param description: The description of this ExportBundle.
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """
        Gets the category of this ExportBundle. :return: The category of this ExportBundle.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ExportBundle. :param category: The category of this ExportBundle.
        :type: str
        """

        self._category = category

    @property
    def inputs(self):
        """
        Gets the inputs of this ExportBundle. :return: The inputs of this ExportBundle.
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this ExportBundle. :param inputs: The inputs of this ExportBundle.
        :type: list[str]
        """

        self._inputs = inputs

    @property
    def streams(self):
        """
        Gets the streams of this ExportBundle. :return: The streams of this ExportBundle.
        :rtype: list[str]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """
        Sets the streams of this ExportBundle. :param streams: The streams of this ExportBundle.
        :type: list[str]
        """

        self._streams = streams

    @property
    def outputs(self):
        """
        Gets the outputs of this ExportBundle. :return: The outputs of this ExportBundle.
        :rtype: list[str]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this ExportBundle. :param outputs: The outputs of this ExportBundle.
        :type: list[str]
        """

        self._outputs = outputs

    @property
    def dashboards(self):
        """
        Gets the dashboards of this ExportBundle. :return: The dashboards of this ExportBundle.
        :rtype: list[str]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """
        Sets the dashboards of this ExportBundle. :param dashboards: The dashboards of this ExportBundle.
        :type: list[str]
        """

        self._dashboards = dashboards

    @property
    def grok_patterns(self):
        """
        Gets the grok_patterns of this ExportBundle. :return: The grok_patterns of this ExportBundle.
        :rtype: list[str]
        """
        return self._grok_patterns

    @grok_patterns.setter
    def grok_patterns(self, grok_patterns):
        """
        Sets the grok_patterns of this ExportBundle. :param grok_patterns: The grok_patterns of this ExportBundle.
        :type: list[str]
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
