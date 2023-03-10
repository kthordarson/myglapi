

from pprint import pformat

import re
class ClusterStats(object):
    def __init__(self, output_count=None, stream_rule_count=None, stream_rule_count_by_stream=None, input_count_by_type=None, stream_count=None, user_count=None, output_count_by_type=None, dashboard_count=None, input_count=None, global_input_count=None, extractor_count=None, content_pack_count=None, extractor_count_by_type=None, ldap_stats=None, alarm_stats=None, elasticsearch=None, mongo=None):
        """
        ClusterStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'output_count': 'int', 'stream_rule_count': 'int', 'stream_rule_count_by_stream': 'object', 'input_count_by_type': 'object', 'stream_count': 'int', 'user_count': 'int', 'output_count_by_type': 'object', 'dashboard_count': 'int', 'input_count': 'int', 'global_input_count': 'int', 'extractor_count': 'int', 'content_pack_count': 'int', 'extractor_count_by_type': 'object', 'ldap_stats': 'object', 'alarm_stats': 'object', 'elasticsearch': 'object', 'mongo': 'object'}

        self.attribute_map = {'output_count': 'output_count', 'stream_rule_count': 'stream_rule_count', 'stream_rule_count_by_stream': 'stream_rule_count_by_stream', 'input_count_by_type': 'input_count_by_type', 'stream_count': 'stream_count', 'user_count': 'user_count', 'output_count_by_type': 'output_count_by_type', 'dashboard_count': 'dashboard_count', 'input_count': 'input_count', 'global_input_count': 'global_input_count', 'extractor_count': 'extractor_count', 'content_pack_count': 'content_pack_count', 'extractor_count_by_type': 'extractor_count_by_type', 'ldap_stats': 'ldap_stats', 'alarm_stats': 'alarm_stats', 'elasticsearch': 'elasticsearch', 'mongo': 'mongo'}

        self._output_count = output_count
        self._stream_rule_count = stream_rule_count
        self._stream_rule_count_by_stream = stream_rule_count_by_stream
        self._input_count_by_type = input_count_by_type
        self._stream_count = stream_count
        self._user_count = user_count
        self._output_count_by_type = output_count_by_type
        self._dashboard_count = dashboard_count
        self._input_count = input_count
        self._global_input_count = global_input_count
        self._extractor_count = extractor_count
        self._content_pack_count = content_pack_count
        self._extractor_count_by_type = extractor_count_by_type
        self._ldap_stats = ldap_stats
        self._alarm_stats = alarm_stats
        self._elasticsearch = elasticsearch
        self._mongo = mongo

    @property
    def output_count(self):
        """
        Gets the output_count of this ClusterStats. :return: The output_count of this ClusterStats.
        :rtype: int
        """
        return self._output_count

    @output_count.setter
    def output_count(self, output_count):
        """
        Sets the output_count of this ClusterStats. :param output_count: The output_count of this ClusterStats.
        :type: int
        """

        self._output_count = output_count

    @property
    def stream_rule_count(self):
        """
        Gets the stream_rule_count of this ClusterStats. :return: The stream_rule_count of this ClusterStats.
        :rtype: int
        """
        return self._stream_rule_count

    @stream_rule_count.setter
    def stream_rule_count(self, stream_rule_count):
        """
        Sets the stream_rule_count of this ClusterStats. :param stream_rule_count: The stream_rule_count of this ClusterStats.
        :type: int
        """

        self._stream_rule_count = stream_rule_count

    @property
    def stream_rule_count_by_stream(self):
        """
        Gets the stream_rule_count_by_stream of this ClusterStats. :return: The stream_rule_count_by_stream of this ClusterStats.
        :rtype: object
        """
        return self._stream_rule_count_by_stream

    @stream_rule_count_by_stream.setter
    def stream_rule_count_by_stream(self, stream_rule_count_by_stream):
        """
        Sets the stream_rule_count_by_stream of this ClusterStats. :param stream_rule_count_by_stream: The stream_rule_count_by_stream of this ClusterStats.
        :type: object
        """

        self._stream_rule_count_by_stream = stream_rule_count_by_stream

    @property
    def input_count_by_type(self):
        """
        Gets the input_count_by_type of this ClusterStats. :return: The input_count_by_type of this ClusterStats.
        :rtype: object
        """
        return self._input_count_by_type

    @input_count_by_type.setter
    def input_count_by_type(self, input_count_by_type):
        """
        Sets the input_count_by_type of this ClusterStats. :param input_count_by_type: The input_count_by_type of this ClusterStats.
        :type: object
        """

        self._input_count_by_type = input_count_by_type

    @property
    def stream_count(self):
        """
        Gets the stream_count of this ClusterStats. :return: The stream_count of this ClusterStats.
        :rtype: int
        """
        return self._stream_count

    @stream_count.setter
    def stream_count(self, stream_count):
        """
        Sets the stream_count of this ClusterStats. :param stream_count: The stream_count of this ClusterStats.
        :type: int
        """

        self._stream_count = stream_count

    @property
    def user_count(self):
        """
        Gets the user_count of this ClusterStats. :return: The user_count of this ClusterStats.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this ClusterStats. :param user_count: The user_count of this ClusterStats.
        :type: int
        """

        self._user_count = user_count

    @property
    def output_count_by_type(self):
        """
        Gets the output_count_by_type of this ClusterStats. :return: The output_count_by_type of this ClusterStats.
        :rtype: object
        """
        return self._output_count_by_type

    @output_count_by_type.setter
    def output_count_by_type(self, output_count_by_type):
        """
        Sets the output_count_by_type of this ClusterStats. :param output_count_by_type: The output_count_by_type of this ClusterStats.
        :type: object
        """

        self._output_count_by_type = output_count_by_type

    @property
    def dashboard_count(self):
        """
        Gets the dashboard_count of this ClusterStats. :return: The dashboard_count of this ClusterStats.
        :rtype: int
        """
        return self._dashboard_count

    @dashboard_count.setter
    def dashboard_count(self, dashboard_count):
        """
        Sets the dashboard_count of this ClusterStats. :param dashboard_count: The dashboard_count of this ClusterStats.
        :type: int
        """

        self._dashboard_count = dashboard_count

    @property
    def input_count(self):
        """
        Gets the input_count of this ClusterStats. :return: The input_count of this ClusterStats.
        :rtype: int
        """
        return self._input_count

    @input_count.setter
    def input_count(self, input_count):
        """
        Sets the input_count of this ClusterStats. :param input_count: The input_count of this ClusterStats.
        :type: int
        """

        self._input_count = input_count

    @property
    def global_input_count(self):
        """
        Gets the global_input_count of this ClusterStats. :return: The global_input_count of this ClusterStats.
        :rtype: int
        """
        return self._global_input_count

    @global_input_count.setter
    def global_input_count(self, global_input_count):
        """
        Sets the global_input_count of this ClusterStats. :param global_input_count: The global_input_count of this ClusterStats.
        :type: int
        """

        self._global_input_count = global_input_count

    @property
    def extractor_count(self):
        """
        Gets the extractor_count of this ClusterStats. :return: The extractor_count of this ClusterStats.
        :rtype: int
        """
        return self._extractor_count

    @extractor_count.setter
    def extractor_count(self, extractor_count):
        """
        Sets the extractor_count of this ClusterStats. :param extractor_count: The extractor_count of this ClusterStats.
        :type: int
        """

        self._extractor_count = extractor_count

    @property
    def content_pack_count(self):
        """
        Gets the content_pack_count of this ClusterStats. :return: The content_pack_count of this ClusterStats.
        :rtype: int
        """
        return self._content_pack_count

    @content_pack_count.setter
    def content_pack_count(self, content_pack_count):
        """
        Sets the content_pack_count of this ClusterStats. :param content_pack_count: The content_pack_count of this ClusterStats.
        :type: int
        """

        self._content_pack_count = content_pack_count

    @property
    def extractor_count_by_type(self):
        """
        Gets the extractor_count_by_type of this ClusterStats. :return: The extractor_count_by_type of this ClusterStats.
        :rtype: object
        """
        return self._extractor_count_by_type

    @extractor_count_by_type.setter
    def extractor_count_by_type(self, extractor_count_by_type):
        """
        Sets the extractor_count_by_type of this ClusterStats. :param extractor_count_by_type: The extractor_count_by_type of this ClusterStats.
        :type: object
        """

        self._extractor_count_by_type = extractor_count_by_type

    @property
    def ldap_stats(self):
        """
        Gets the ldap_stats of this ClusterStats. :return: The ldap_stats of this ClusterStats.
        :rtype: object
        """
        return self._ldap_stats

    @ldap_stats.setter
    def ldap_stats(self, ldap_stats):
        """
        Sets the ldap_stats of this ClusterStats. :param ldap_stats: The ldap_stats of this ClusterStats.
        :type: object
        """

        self._ldap_stats = ldap_stats

    @property
    def alarm_stats(self):
        """
        Gets the alarm_stats of this ClusterStats. :return: The alarm_stats of this ClusterStats.
        :rtype: object
        """
        return self._alarm_stats

    @alarm_stats.setter
    def alarm_stats(self, alarm_stats):
        """
        Sets the alarm_stats of this ClusterStats. :param alarm_stats: The alarm_stats of this ClusterStats.
        :type: object
        """

        self._alarm_stats = alarm_stats

    @property
    def elasticsearch(self):
        """
        Gets the elasticsearch of this ClusterStats. :return: The elasticsearch of this ClusterStats.
        :rtype: object
        """
        return self._elasticsearch

    @elasticsearch.setter
    def elasticsearch(self, elasticsearch):
        """
        Sets the elasticsearch of this ClusterStats. :param elasticsearch: The elasticsearch of this ClusterStats.
        :type: object
        """

        self._elasticsearch = elasticsearch

    @property
    def mongo(self):
        """
        Gets the mongo of this ClusterStats. :return: The mongo of this ClusterStats.
        :rtype: object
        """
        return self._mongo

    @mongo.setter
    def mongo(self, mongo):
        """
        Sets the mongo of this ClusterStats. :param mongo: The mongo of this ClusterStats.
        :type: object
        """

        self._mongo = mongo

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
