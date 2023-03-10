

from pprint import pformat

import re
class InputSummary(object):
    def __init__(self, title=None, _global=None, name=None, content_pack=None, id=None, created_at=None, type=None, creator_user_id=None, attributes=None, static_fields=None, node=None):
        """
        InputSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'title': 'str', '_global': 'bool', 'name': 'str', 'content_pack': 'str', 'id': 'str', 'created_at': 'datetime', 'type': 'str', 'creator_user_id': 'str', 'attributes': 'object', 'static_fields': 'object', 'node': 'str'}

        self.attribute_map = {'title': 'title', '_global': 'global', 'name': 'name', 'content_pack': 'content_pack', 'id': 'id', 'created_at': 'created_at', 'type': 'type', 'creator_user_id': 'creator_user_id', 'attributes': 'attributes', 'static_fields': 'static_fields', 'node': 'node'}

        self._title = title
        self.__global = _global
        self._name = name
        self._content_pack = content_pack
        self._id = id
        self._created_at = created_at
        self._type = type
        self._creator_user_id = creator_user_id
        self._attributes = attributes
        self._static_fields = static_fields
        self._node = node

    @property
    def title(self):
        """
        Gets the title of this InputSummary. :return: The title of this InputSummary.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this InputSummary. :param title: The title of this InputSummary.
        :type: str
        """

        self._title = title

    @property
    def _global(self):
        """
        Gets the _global of this InputSummary. :return: The _global of this InputSummary.
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """
        Sets the _global of this InputSummary. :param _global: The _global of this InputSummary.
        :type: bool
        """

        self.__global = _global

    @property
    def name(self):
        """
        Gets the name of this InputSummary. :return: The name of this InputSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InputSummary. :param name: The name of this InputSummary.
        :type: str
        """

        self._name = name

    @property
    def content_pack(self):
        """
        Gets the content_pack of this InputSummary. :return: The content_pack of this InputSummary.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this InputSummary. :param content_pack: The content_pack of this InputSummary.
        :type: str
        """

        self._content_pack = content_pack

    @property
    def id(self):
        """
        Gets the id of this InputSummary. :return: The id of this InputSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InputSummary. :param id: The id of this InputSummary.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this InputSummary. :return: The created_at of this InputSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this InputSummary. :param created_at: The created_at of this InputSummary.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def type(self):
        """
        Gets the type of this InputSummary. :return: The type of this InputSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InputSummary. :param type: The type of this InputSummary.
        :type: str
        """

        self._type = type

    @property
    def creator_user_id(self):
        """
        Gets the creator_user_id of this InputSummary. :return: The creator_user_id of this InputSummary.
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """
        Sets the creator_user_id of this InputSummary. :param creator_user_id: The creator_user_id of this InputSummary.
        :type: str
        """

        self._creator_user_id = creator_user_id

    @property
    def attributes(self):
        """
        Gets the attributes of this InputSummary. :return: The attributes of this InputSummary.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this InputSummary. :param attributes: The attributes of this InputSummary.
        :type: object
        """

        self._attributes = attributes

    @property
    def static_fields(self):
        """
        Gets the static_fields of this InputSummary. :return: The static_fields of this InputSummary.
        :rtype: object
        """
        return self._static_fields

    @static_fields.setter
    def static_fields(self, static_fields):
        """
        Sets the static_fields of this InputSummary. :param static_fields: The static_fields of this InputSummary.
        :type: object
        """

        self._static_fields = static_fields

    @property
    def node(self):
        """
        Gets the node of this InputSummary. :return: The node of this InputSummary.
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """
        Sets the node of this InputSummary. :param node: The node of this InputSummary.
        :type: str
        """

        self._node = node

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
