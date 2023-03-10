

from pprint import pformat

import re
class JournalSummaryResponse(object):
    def __init__(self, enabled=None, append_events_per_second=None, read_events_per_second=None, uncommitted_journal_entries=None, journal_size=None, journal_size_limit=None, number_of_segments=None, oldest_segment=None, journal_config=None):
        """
        JournalSummaryResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'enabled': 'bool', 'append_events_per_second': 'int', 'read_events_per_second': 'int', 'uncommitted_journal_entries': 'int', 'journal_size': 'Any', 'journal_size_limit': 'Any', 'number_of_segments': 'int', 'oldest_segment': 'datetime', 'journal_config': 'object'}

        self.attribute_map = {'enabled': 'enabled', 'append_events_per_second': 'append_events_per_second', 'read_events_per_second': 'read_events_per_second', 'uncommitted_journal_entries': 'uncommitted_journal_entries', 'journal_size': 'journal_size', 'journal_size_limit': 'journal_size_limit', 'number_of_segments': 'number_of_segments', 'oldest_segment': 'oldest_segment', 'journal_config': 'journal_config'}

        self._enabled = enabled
        self._append_events_per_second = append_events_per_second
        self._read_events_per_second = read_events_per_second
        self._uncommitted_journal_entries = uncommitted_journal_entries
        self._journal_size = journal_size
        self._journal_size_limit = journal_size_limit
        self._number_of_segments = number_of_segments
        self._oldest_segment = oldest_segment
        self._journal_config = journal_config

    @property
    def enabled(self):
        """
        Gets the enabled of this JournalSummaryResponse. :return: The enabled of this JournalSummaryResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this JournalSummaryResponse. :param enabled: The enabled of this JournalSummaryResponse.
        :type: bool
        """

        self._enabled = enabled

    @property
    def append_events_per_second(self):
        """
        Gets the append_events_per_second of this JournalSummaryResponse. :return: The append_events_per_second of this JournalSummaryResponse.
        :rtype: int
        """
        return self._append_events_per_second

    @append_events_per_second.setter
    def append_events_per_second(self, append_events_per_second):
        """
        Sets the append_events_per_second of this JournalSummaryResponse. :param append_events_per_second: The append_events_per_second of this JournalSummaryResponse.
        :type: int
        """

        self._append_events_per_second = append_events_per_second

    @property
    def read_events_per_second(self):
        """
        Gets the read_events_per_second of this JournalSummaryResponse. :return: The read_events_per_second of this JournalSummaryResponse.
        :rtype: int
        """
        return self._read_events_per_second

    @read_events_per_second.setter
    def read_events_per_second(self, read_events_per_second):
        """
        Sets the read_events_per_second of this JournalSummaryResponse. :param read_events_per_second: The read_events_per_second of this JournalSummaryResponse.
        :type: int
        """

        self._read_events_per_second = read_events_per_second

    @property
    def uncommitted_journal_entries(self):
        """
        Gets the uncommitted_journal_entries of this JournalSummaryResponse. :return: The uncommitted_journal_entries of this JournalSummaryResponse.
        :rtype: int
        """
        return self._uncommitted_journal_entries

    @uncommitted_journal_entries.setter
    def uncommitted_journal_entries(self, uncommitted_journal_entries):
        """
        Sets the uncommitted_journal_entries of this JournalSummaryResponse. :param uncommitted_journal_entries: The uncommitted_journal_entries of this JournalSummaryResponse.
        :type: int
        """

        self._uncommitted_journal_entries = uncommitted_journal_entries

    @property
    def journal_size(self):
        """
        Gets the journal_size of this JournalSummaryResponse. :return: The journal_size of this JournalSummaryResponse.
        :rtype: Any
        """
        return self._journal_size

    @journal_size.setter
    def journal_size(self, journal_size):
        """
        Sets the journal_size of this JournalSummaryResponse. :param journal_size: The journal_size of this JournalSummaryResponse.
        :type: Any
        """

        self._journal_size = journal_size

    @property
    def journal_size_limit(self):
        """
        Gets the journal_size_limit of this JournalSummaryResponse. :return: The journal_size_limit of this JournalSummaryResponse.
        :rtype: Any
        """
        return self._journal_size_limit

    @journal_size_limit.setter
    def journal_size_limit(self, journal_size_limit):
        """
        Sets the journal_size_limit of this JournalSummaryResponse. :param journal_size_limit: The journal_size_limit of this JournalSummaryResponse.
        :type: Any
        """

        self._journal_size_limit = journal_size_limit

    @property
    def number_of_segments(self):
        """
        Gets the number_of_segments of this JournalSummaryResponse. :return: The number_of_segments of this JournalSummaryResponse.
        :rtype: int
        """
        return self._number_of_segments

    @number_of_segments.setter
    def number_of_segments(self, number_of_segments):
        """
        Sets the number_of_segments of this JournalSummaryResponse. :param number_of_segments: The number_of_segments of this JournalSummaryResponse.
        :type: int
        """

        self._number_of_segments = number_of_segments

    @property
    def oldest_segment(self):
        """
        Gets the oldest_segment of this JournalSummaryResponse. :return: The oldest_segment of this JournalSummaryResponse.
        :rtype: datetime
        """
        return self._oldest_segment

    @oldest_segment.setter
    def oldest_segment(self, oldest_segment):
        """
        Sets the oldest_segment of this JournalSummaryResponse. :param oldest_segment: The oldest_segment of this JournalSummaryResponse.
        :type: datetime
        """

        self._oldest_segment = oldest_segment

    @property
    def journal_config(self):
        """
        Gets the journal_config of this JournalSummaryResponse. :return: The journal_config of this JournalSummaryResponse.
        :rtype: object
        """
        return self._journal_config

    @journal_config.setter
    def journal_config(self, journal_config):
        """
        Sets the journal_config of this JournalSummaryResponse. :param journal_config: The journal_config of this JournalSummaryResponse.
        :type: object
        """

        self._journal_config = journal_config

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
