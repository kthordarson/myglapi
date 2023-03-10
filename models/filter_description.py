

from pprint import pformat

import re
class FilterDescription(object):
    def __init__(self, creator_user_id=None, created_at=None, name=None, description=None, field_name=None, pattern=None, id=None):
        """
        FilterDescription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'creator_user_id': 'str', 'created_at': 'datetime', 'name': 'str', 'description': 'str', 'field_name': 'str', 'pattern': 'str', 'id': 'Any'}

        self.attribute_map = {'creator_user_id': 'creator_user_id', 'created_at': 'created_at', 'name': 'name', 'description': 'description', 'field_name': 'field_name', 'pattern': 'pattern', 'id': 'id'}

        self._creator_user_id = creator_user_id
        self._created_at = created_at
        self._name = name
        self._description = description
        self._field_name = field_name
        self._pattern = pattern
        self._id = id

    @property
    def creator_user_id(self):
        """
        Gets the creator_user_id of this FilterDescription. :return: The creator_user_id of this FilterDescription.
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """
        Sets the creator_user_id of this FilterDescription. :param creator_user_id: The creator_user_id of this FilterDescription.
        :type: str
        """

        self._creator_user_id = creator_user_id

    @property
    def created_at(self):
        """
        Gets the created_at of this FilterDescription. :return: The created_at of this FilterDescription.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FilterDescription. :param created_at: The created_at of this FilterDescription.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """
        Gets the name of this FilterDescription. :return: The name of this FilterDescription.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FilterDescription. :param name: The name of this FilterDescription.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FilterDescription. :return: The description of this FilterDescription.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FilterDescription. :param description: The description of this FilterDescription.
        :type: str
        """

        self._description = description

    @property
    def field_name(self):
        """
        Gets the field_name of this FilterDescription. :return: The field_name of this FilterDescription.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this FilterDescription. :param field_name: The field_name of this FilterDescription.
        :type: str
        """

        self._field_name = field_name

    @property
    def pattern(self):
        """
        Gets the pattern of this FilterDescription. :return: The pattern of this FilterDescription.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this FilterDescription. :param pattern: The pattern of this FilterDescription.
        :type: str
        """

        self._pattern = pattern

    @property
    def id(self):
        """
        Gets the id of this FilterDescription. :return: The id of this FilterDescription.
        :rtype: Any
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FilterDescription. :param id: The id of this FilterDescription.
        :type: Any
        """

        self._id = id

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
