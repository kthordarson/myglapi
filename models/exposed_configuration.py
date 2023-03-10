

from pprint import pformat

import re
class ExposedConfiguration(object):
    def __init__(self, inputbuffer_processors=None, processbuffer_processors=None, outputbuffer_processors=None, processor_wait_strategy=None, inputbuffer_wait_strategy=None, inputbuffer_ring_size=None, ring_size=None, plugin_dir=None, node_id_file=None, allow_highlighting=None, allow_leading_wildcard_searches=None, elasticsearch_shards=None, elasticsearch_replicas=None, stream_processing_timeout=None, stream_processing_max_faults=None, output_module_timeout=None, stale_master_timeout=None, disable_index_optimization=None, index_optimization_max_num_segments=None, gc_warning_threshold=None):
        """
        ExposedConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'inputbuffer_processors': 'int', 'processbuffer_processors': 'int', 'outputbuffer_processors': 'int', 'processor_wait_strategy': 'str', 'inputbuffer_wait_strategy': 'str', 'inputbuffer_ring_size': 'int', 'ring_size': 'int', 'plugin_dir': 'str', 'node_id_file': 'str', 'allow_highlighting': 'bool', 'allow_leading_wildcard_searches': 'bool', 'elasticsearch_shards': 'int', 'elasticsearch_replicas': 'int', 'stream_processing_timeout': 'int', 'stream_processing_max_faults': 'int', 'output_module_timeout': 'int', 'stale_master_timeout': 'int', 'disable_index_optimization': 'bool', 'index_optimization_max_num_segments': 'int', 'gc_warning_threshold': 'str'}

        self.attribute_map = {'inputbuffer_processors': 'inputbuffer_processors', 'processbuffer_processors': 'processbuffer_processors', 'outputbuffer_processors': 'outputbuffer_processors', 'processor_wait_strategy': 'processor_wait_strategy', 'inputbuffer_wait_strategy': 'inputbuffer_wait_strategy', 'inputbuffer_ring_size': 'inputbuffer_ring_size', 'ring_size': 'ring_size', 'plugin_dir': 'plugin_dir', 'node_id_file': 'node_id_file', 'allow_highlighting': 'allow_highlighting', 'allow_leading_wildcard_searches': 'allow_leading_wildcard_searches', 'elasticsearch_shards': 'elasticsearch_shards', 'elasticsearch_replicas': 'elasticsearch_replicas', 'stream_processing_timeout': 'stream_processing_timeout', 'stream_processing_max_faults': 'stream_processing_max_faults', 'output_module_timeout': 'output_module_timeout', 'stale_master_timeout': 'stale_master_timeout', 'disable_index_optimization': 'disable_index_optimization', 'index_optimization_max_num_segments': 'index_optimization_max_num_segments', 'gc_warning_threshold': 'gc_warning_threshold'}

        self._inputbuffer_processors = inputbuffer_processors
        self._processbuffer_processors = processbuffer_processors
        self._outputbuffer_processors = outputbuffer_processors
        self._processor_wait_strategy = processor_wait_strategy
        self._inputbuffer_wait_strategy = inputbuffer_wait_strategy
        self._inputbuffer_ring_size = inputbuffer_ring_size
        self._ring_size = ring_size
        self._plugin_dir = plugin_dir
        self._node_id_file = node_id_file
        self._allow_highlighting = allow_highlighting
        self._allow_leading_wildcard_searches = allow_leading_wildcard_searches
        self._elasticsearch_shards = elasticsearch_shards
        self._elasticsearch_replicas = elasticsearch_replicas
        self._stream_processing_timeout = stream_processing_timeout
        self._stream_processing_max_faults = stream_processing_max_faults
        self._output_module_timeout = output_module_timeout
        self._stale_master_timeout = stale_master_timeout
        self._disable_index_optimization = disable_index_optimization
        self._index_optimization_max_num_segments = index_optimization_max_num_segments
        self._gc_warning_threshold = gc_warning_threshold

    @property
    def inputbuffer_processors(self):
        """
        Gets the inputbuffer_processors of this ExposedConfiguration. :return: The inputbuffer_processors of this ExposedConfiguration.
        :rtype: int
        """
        return self._inputbuffer_processors

    @inputbuffer_processors.setter
    def inputbuffer_processors(self, inputbuffer_processors):
        """
        Sets the inputbuffer_processors of this ExposedConfiguration. :param inputbuffer_processors: The inputbuffer_processors of this ExposedConfiguration.
        :type: int
        """

        self._inputbuffer_processors = inputbuffer_processors

    @property
    def processbuffer_processors(self):
        """
        Gets the processbuffer_processors of this ExposedConfiguration. :return: The processbuffer_processors of this ExposedConfiguration.
        :rtype: int
        """
        return self._processbuffer_processors

    @processbuffer_processors.setter
    def processbuffer_processors(self, processbuffer_processors):
        """
        Sets the processbuffer_processors of this ExposedConfiguration. :param processbuffer_processors: The processbuffer_processors of this ExposedConfiguration.
        :type: int
        """

        self._processbuffer_processors = processbuffer_processors

    @property
    def outputbuffer_processors(self):
        """
        Gets the outputbuffer_processors of this ExposedConfiguration. :return: The outputbuffer_processors of this ExposedConfiguration.
        :rtype: int
        """
        return self._outputbuffer_processors

    @outputbuffer_processors.setter
    def outputbuffer_processors(self, outputbuffer_processors):
        """
        Sets the outputbuffer_processors of this ExposedConfiguration. :param outputbuffer_processors: The outputbuffer_processors of this ExposedConfiguration.
        :type: int
        """

        self._outputbuffer_processors = outputbuffer_processors

    @property
    def processor_wait_strategy(self):
        """
        Gets the processor_wait_strategy of this ExposedConfiguration. :return: The processor_wait_strategy of this ExposedConfiguration.
        :rtype: str
        """
        return self._processor_wait_strategy

    @processor_wait_strategy.setter
    def processor_wait_strategy(self, processor_wait_strategy):
        """
        Sets the processor_wait_strategy of this ExposedConfiguration. :param processor_wait_strategy: The processor_wait_strategy of this ExposedConfiguration.
        :type: str
        """

        self._processor_wait_strategy = processor_wait_strategy

    @property
    def inputbuffer_wait_strategy(self):
        """
        Gets the inputbuffer_wait_strategy of this ExposedConfiguration. :return: The inputbuffer_wait_strategy of this ExposedConfiguration.
        :rtype: str
        """
        return self._inputbuffer_wait_strategy

    @inputbuffer_wait_strategy.setter
    def inputbuffer_wait_strategy(self, inputbuffer_wait_strategy):
        """
        Sets the inputbuffer_wait_strategy of this ExposedConfiguration. :param inputbuffer_wait_strategy: The inputbuffer_wait_strategy of this ExposedConfiguration.
        :type: str
        """

        self._inputbuffer_wait_strategy = inputbuffer_wait_strategy

    @property
    def inputbuffer_ring_size(self):
        """
        Gets the inputbuffer_ring_size of this ExposedConfiguration. :return: The inputbuffer_ring_size of this ExposedConfiguration.
        :rtype: int
        """
        return self._inputbuffer_ring_size

    @inputbuffer_ring_size.setter
    def inputbuffer_ring_size(self, inputbuffer_ring_size):
        """
        Sets the inputbuffer_ring_size of this ExposedConfiguration. :param inputbuffer_ring_size: The inputbuffer_ring_size of this ExposedConfiguration.
        :type: int
        """

        self._inputbuffer_ring_size = inputbuffer_ring_size

    @property
    def ring_size(self):
        """
        Gets the ring_size of this ExposedConfiguration. :return: The ring_size of this ExposedConfiguration.
        :rtype: int
        """
        return self._ring_size

    @ring_size.setter
    def ring_size(self, ring_size):
        """
        Sets the ring_size of this ExposedConfiguration. :param ring_size: The ring_size of this ExposedConfiguration.
        :type: int
        """

        self._ring_size = ring_size

    @property
    def plugin_dir(self):
        """
        Gets the plugin_dir of this ExposedConfiguration. :return: The plugin_dir of this ExposedConfiguration.
        :rtype: str
        """
        return self._plugin_dir

    @plugin_dir.setter
    def plugin_dir(self, plugin_dir):
        """
        Sets the plugin_dir of this ExposedConfiguration. :param plugin_dir: The plugin_dir of this ExposedConfiguration.
        :type: str
        """

        self._plugin_dir = plugin_dir

    @property
    def node_id_file(self):
        """
        Gets the node_id_file of this ExposedConfiguration. :return: The node_id_file of this ExposedConfiguration.
        :rtype: str
        """
        return self._node_id_file

    @node_id_file.setter
    def node_id_file(self, node_id_file):
        """
        Sets the node_id_file of this ExposedConfiguration. :param node_id_file: The node_id_file of this ExposedConfiguration.
        :type: str
        """

        self._node_id_file = node_id_file

    @property
    def allow_highlighting(self):
        """
        Gets the allow_highlighting of this ExposedConfiguration. :return: The allow_highlighting of this ExposedConfiguration.
        :rtype: bool
        """
        return self._allow_highlighting

    @allow_highlighting.setter
    def allow_highlighting(self, allow_highlighting):
        """
        Sets the allow_highlighting of this ExposedConfiguration. :param allow_highlighting: The allow_highlighting of this ExposedConfiguration.
        :type: bool
        """

        self._allow_highlighting = allow_highlighting

    @property
    def allow_leading_wildcard_searches(self):
        """
        Gets the allow_leading_wildcard_searches of this ExposedConfiguration. :return: The allow_leading_wildcard_searches of this ExposedConfiguration.
        :rtype: bool
        """
        return self._allow_leading_wildcard_searches

    @allow_leading_wildcard_searches.setter
    def allow_leading_wildcard_searches(self, allow_leading_wildcard_searches):
        """
        Sets the allow_leading_wildcard_searches of this ExposedConfiguration. :param allow_leading_wildcard_searches: The allow_leading_wildcard_searches of this ExposedConfiguration.
        :type: bool
        """

        self._allow_leading_wildcard_searches = allow_leading_wildcard_searches

    @property
    def elasticsearch_shards(self):
        """
        Gets the elasticsearch_shards of this ExposedConfiguration. :return: The elasticsearch_shards of this ExposedConfiguration.
        :rtype: int
        """
        return self._elasticsearch_shards

    @elasticsearch_shards.setter
    def elasticsearch_shards(self, elasticsearch_shards):
        """
        Sets the elasticsearch_shards of this ExposedConfiguration. :param elasticsearch_shards: The elasticsearch_shards of this ExposedConfiguration.
        :type: int
        """

        self._elasticsearch_shards = elasticsearch_shards

    @property
    def elasticsearch_replicas(self):
        """
        Gets the elasticsearch_replicas of this ExposedConfiguration. :return: The elasticsearch_replicas of this ExposedConfiguration.
        :rtype: int
        """
        return self._elasticsearch_replicas

    @elasticsearch_replicas.setter
    def elasticsearch_replicas(self, elasticsearch_replicas):
        """
        Sets the elasticsearch_replicas of this ExposedConfiguration. :param elasticsearch_replicas: The elasticsearch_replicas of this ExposedConfiguration.
        :type: int
        """

        self._elasticsearch_replicas = elasticsearch_replicas

    @property
    def stream_processing_timeout(self):
        """
        Gets the stream_processing_timeout of this ExposedConfiguration. :return: The stream_processing_timeout of this ExposedConfiguration.
        :rtype: int
        """
        return self._stream_processing_timeout

    @stream_processing_timeout.setter
    def stream_processing_timeout(self, stream_processing_timeout):
        """
        Sets the stream_processing_timeout of this ExposedConfiguration. :param stream_processing_timeout: The stream_processing_timeout of this ExposedConfiguration.
        :type: int
        """

        self._stream_processing_timeout = stream_processing_timeout

    @property
    def stream_processing_max_faults(self):
        """
        Gets the stream_processing_max_faults of this ExposedConfiguration. :return: The stream_processing_max_faults of this ExposedConfiguration.
        :rtype: int
        """
        return self._stream_processing_max_faults

    @stream_processing_max_faults.setter
    def stream_processing_max_faults(self, stream_processing_max_faults):
        """
        Sets the stream_processing_max_faults of this ExposedConfiguration. :param stream_processing_max_faults: The stream_processing_max_faults of this ExposedConfiguration.
        :type: int
        """

        self._stream_processing_max_faults = stream_processing_max_faults

    @property
    def output_module_timeout(self):
        """
        Gets the output_module_timeout of this ExposedConfiguration. :return: The output_module_timeout of this ExposedConfiguration.
        :rtype: int
        """
        return self._output_module_timeout

    @output_module_timeout.setter
    def output_module_timeout(self, output_module_timeout):
        """
        Sets the output_module_timeout of this ExposedConfiguration. :param output_module_timeout: The output_module_timeout of this ExposedConfiguration.
        :type: int
        """

        self._output_module_timeout = output_module_timeout

    @property
    def stale_master_timeout(self):
        """
        Gets the stale_master_timeout of this ExposedConfiguration. :return: The stale_master_timeout of this ExposedConfiguration.
        :rtype: int
        """
        return self._stale_master_timeout

    @stale_master_timeout.setter
    def stale_master_timeout(self, stale_master_timeout):
        """
        Sets the stale_master_timeout of this ExposedConfiguration. :param stale_master_timeout: The stale_master_timeout of this ExposedConfiguration.
        :type: int
        """

        self._stale_master_timeout = stale_master_timeout

    @property
    def disable_index_optimization(self):
        """
        Gets the disable_index_optimization of this ExposedConfiguration. :return: The disable_index_optimization of this ExposedConfiguration.
        :rtype: bool
        """
        return self._disable_index_optimization

    @disable_index_optimization.setter
    def disable_index_optimization(self, disable_index_optimization):
        """
        Sets the disable_index_optimization of this ExposedConfiguration. :param disable_index_optimization: The disable_index_optimization of this ExposedConfiguration.
        :type: bool
        """

        self._disable_index_optimization = disable_index_optimization

    @property
    def index_optimization_max_num_segments(self):
        """
        Gets the index_optimization_max_num_segments of this ExposedConfiguration. :return: The index_optimization_max_num_segments of this ExposedConfiguration.
        :rtype: int
        """
        return self._index_optimization_max_num_segments

    @index_optimization_max_num_segments.setter
    def index_optimization_max_num_segments(self, index_optimization_max_num_segments):
        """
        Sets the index_optimization_max_num_segments of this ExposedConfiguration. :param index_optimization_max_num_segments: The index_optimization_max_num_segments of this ExposedConfiguration.
        :type: int
        """

        self._index_optimization_max_num_segments = index_optimization_max_num_segments

    @property
    def gc_warning_threshold(self):
        """
        Gets the gc_warning_threshold of this ExposedConfiguration. :return: The gc_warning_threshold of this ExposedConfiguration.
        :rtype: str
        """
        return self._gc_warning_threshold

    @gc_warning_threshold.setter
    def gc_warning_threshold(self, gc_warning_threshold):
        """
        Sets the gc_warning_threshold of this ExposedConfiguration. :param gc_warning_threshold: The gc_warning_threshold of this ExposedConfiguration.
        :type: str
        """

        self._gc_warning_threshold = gc_warning_threshold

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
