

from pprint import pformat

import re
class OutputSummary(object):
    def __init__(self, id=None, title=None, type=None, creator_user_id=None, created_at=None, configuration=None, content_pack=None):
        """
        OutputSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'title': 'str', 'type': 'str', 'creator_user_id': 'str', 'created_at': 'datetime', 'configuration': 'object', 'content_pack': 'str'}

        self.attribute_map = {'id': 'id', 'title': 'title', 'type': 'type', 'creator_user_id': 'creator_user_id', 'created_at': 'created_at', 'configuration': 'configuration', 'content_pack': 'content_pack'}

        self._id = id
        self._title = title
        self._type = type
        self._creator_user_id = creator_user_id
        self._created_at = created_at
        self._configuration = configuration
        self._content_pack = content_pack

    @property
    def id(self):
        """
        Gets the id of this OutputSummary. :return: The id of this OutputSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OutputSummary. :param id: The id of this OutputSummary.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this OutputSummary. :return: The title of this OutputSummary.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this OutputSummary. :param title: The title of this OutputSummary.
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this OutputSummary. :return: The type of this OutputSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OutputSummary. :param type: The type of this OutputSummary.
        :type: str
        """

        self._type = type

    @property
    def creator_user_id(self):
        """
        Gets the creator_user_id of this OutputSummary. :return: The creator_user_id of this OutputSummary.
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """
        Sets the creator_user_id of this OutputSummary. :param creator_user_id: The creator_user_id of this OutputSummary.
        :type: str
        """

        self._creator_user_id = creator_user_id

    @property
    def created_at(self):
        """
        Gets the created_at of this OutputSummary. :return: The created_at of this OutputSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this OutputSummary. :param created_at: The created_at of this OutputSummary.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def configuration(self):
        """
        Gets the configuration of this OutputSummary. :return: The configuration of this OutputSummary.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this OutputSummary. :param configuration: The configuration of this OutputSummary.
        :type: object
        """

        self._configuration = configuration

    @property
    def content_pack(self):
        """
        Gets the content_pack of this OutputSummary. :return: The content_pack of this OutputSummary.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this OutputSummary. :param content_pack: The content_pack of this OutputSummary.
        :type: str
        """

        self._content_pack = content_pack

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
