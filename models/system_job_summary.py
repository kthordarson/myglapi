

from pprint import pformat

import re
class SystemJobSummary(object):
    def __init__(self, id=None, description=None, name=None, info=None, node_id=None, started_at=None, percent_complete=None, is_cancelable=None, provides_progress=None):
        """
        SystemJobSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'description': 'str', 'name': 'str', 'info': 'str', 'node_id': 'str', 'started_at': 'datetime', 'percent_complete': 'int', 'is_cancelable': 'bool', 'provides_progress': 'bool'}

        self.attribute_map = {'id': 'id', 'description': 'description', 'name': 'name', 'info': 'info', 'node_id': 'node_id', 'started_at': 'started_at', 'percent_complete': 'percent_complete', 'is_cancelable': 'is_cancelable', 'provides_progress': 'provides_progress'}

        self._id = id
        self._description = description
        self._name = name
        self._info = info
        self._node_id = node_id
        self._started_at = started_at
        self._percent_complete = percent_complete
        self._is_cancelable = is_cancelable
        self._provides_progress = provides_progress

    @property
    def id(self):
        """
        Gets the id of this SystemJobSummary.        :return: The id of this SystemJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SystemJobSummary.        :param id: The id of this SystemJobSummary.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this SystemJobSummary.        :return: The description of this SystemJobSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SystemJobSummary.        :param description: The description of this SystemJobSummary.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this SystemJobSummary.        :return: The name of this SystemJobSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SystemJobSummary.        :param name: The name of this SystemJobSummary.
        :type: str
        """

        self._name = name

    @property
    def info(self):
        """
        Gets the info of this SystemJobSummary.        :return: The info of this SystemJobSummary.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this SystemJobSummary.        :param info: The info of this SystemJobSummary.
        :type: str
        """

        self._info = info

    @property
    def node_id(self):
        """
        Gets the node_id of this SystemJobSummary.        :return: The node_id of this SystemJobSummary.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this SystemJobSummary.        :param node_id: The node_id of this SystemJobSummary.
        :type: str
        """

        self._node_id = node_id

    @property
    def started_at(self):
        """
        Gets the started_at of this SystemJobSummary.        :return: The started_at of this SystemJobSummary.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this SystemJobSummary.        :param started_at: The started_at of this SystemJobSummary.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this SystemJobSummary.        :return: The percent_complete of this SystemJobSummary.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this SystemJobSummary.        :param percent_complete: The percent_complete of this SystemJobSummary.
        :type: int
        """

        self._percent_complete = percent_complete

    @property
    def is_cancelable(self):
        """
        Gets the is_cancelable of this SystemJobSummary.        :return: The is_cancelable of this SystemJobSummary.
        :rtype: bool
        """
        return self._is_cancelable

    @is_cancelable.setter
    def is_cancelable(self, is_cancelable):
        """
        Sets the is_cancelable of this SystemJobSummary.        :param is_cancelable: The is_cancelable of this SystemJobSummary.
        :type: bool
        """

        self._is_cancelable = is_cancelable

    @property
    def provides_progress(self):
        """
        Gets the provides_progress of this SystemJobSummary.        :return: The provides_progress of this SystemJobSummary.
        :rtype: bool
        """
        return self._provides_progress

    @provides_progress.setter
    def provides_progress(self, provides_progress):
        """
        Sets the provides_progress of this SystemJobSummary.        :param provides_progress: The provides_progress of this SystemJobSummary.
        :type: bool
        """

        self._provides_progress = provides_progress

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
