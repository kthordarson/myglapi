

from pprint import pformat

import re
class RuleSource(object):
    def __init__(self, id=None, title=None, description=None, source=None, created_at=None, modified_at=None, errors=None):
        """
        RuleSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'title': 'str', 'description': 'str', 'source': 'str', 'created_at': 'datetime', 'modified_at': 'datetime', 'errors': 'list[object]'}

        self.attribute_map = {'id': 'id', 'title': 'title', 'description': 'description', 'source': 'source', 'created_at': 'created_at', 'modified_at': 'modified_at', 'errors': 'errors'}

        self._id = id
        self._title = title
        self._description = description
        self._source = source
        self._created_at = created_at
        self._modified_at = modified_at
        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this RuleSource.        :return: The id of this RuleSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RuleSource.        :param id: The id of this RuleSource.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this RuleSource.        :return: The title of this RuleSource.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this RuleSource.        :param title: The title of this RuleSource.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this RuleSource.        :return: The description of this RuleSource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuleSource.        :param description: The description of this RuleSource.
        :type: str
        """

        self._description = description

    @property
    def source(self):
        """
        Gets the source of this RuleSource.        :return: The source of this RuleSource.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this RuleSource.        :param source: The source of this RuleSource.
        :type: str
        """

        self._source = source

    @property
    def created_at(self):
        """
        Gets the created_at of this RuleSource.        :return: The created_at of this RuleSource.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this RuleSource.        :param created_at: The created_at of this RuleSource.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this RuleSource.        :return: The modified_at of this RuleSource.
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this RuleSource.        :param modified_at: The modified_at of this RuleSource.
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def errors(self):
        """
        Gets the errors of this RuleSource.        :return: The errors of this RuleSource.
        :rtype: list[object]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this RuleSource.        :param errors: The errors of this RuleSource.
        :type: list[object]
        """

        self._errors = errors

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
