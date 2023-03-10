

from pprint import pformat

import re
class StreamResponse(object):
    def __init__(self, id=None, creator_user_id=None, outputs=None, matching_type=None, description=None, created_at=None, disabled=None, rules=None, alert_conditions=None, alert_receivers=None, title=None, content_pack=None):
        """
        StreamResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'creator_user_id': 'str', 'outputs': 'list[object]', 'matching_type': 'str', 'description': 'str', 'created_at': 'str', 'disabled': 'bool', 'rules': 'list[object]', 'alert_conditions': 'list[object]', 'alert_receivers': 'object', 'title': 'str', 'content_pack': 'str'}

        self.attribute_map = {'id': 'id', 'creator_user_id': 'creator_user_id', 'outputs': 'outputs', 'matching_type': 'matching_type', 'description': 'description', 'created_at': 'created_at', 'disabled': 'disabled', 'rules': 'rules', 'alert_conditions': 'alert_conditions', 'alert_receivers': 'alert_receivers', 'title': 'title', 'content_pack': 'content_pack'}

        self._id = id
        self._creator_user_id = creator_user_id
        self._outputs = outputs
        self._matching_type = matching_type
        self._description = description
        self._created_at = created_at
        self._disabled = disabled
        self._rules = rules
        self._alert_conditions = alert_conditions
        self._alert_receivers = alert_receivers
        self._title = title
        self._content_pack = content_pack

    @property
    def id(self):
        """
        Gets the id of this StreamResponse. :return: The id of this StreamResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StreamResponse. :param id: The id of this StreamResponse.
        :type: str
        """

        self._id = id

    @property
    def creator_user_id(self):
        """
        Gets the creator_user_id of this StreamResponse. :return: The creator_user_id of this StreamResponse.
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """
        Sets the creator_user_id of this StreamResponse. :param creator_user_id: The creator_user_id of this StreamResponse.
        :type: str
        """

        self._creator_user_id = creator_user_id

    @property
    def outputs(self):
        """
        Gets the outputs of this StreamResponse. :return: The outputs of this StreamResponse.
        :rtype: list[object]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this StreamResponse. :param outputs: The outputs of this StreamResponse.
        :type: list[object]
        """

        self._outputs = outputs

    @property
    def matching_type(self):
        """
        Gets the matching_type of this StreamResponse. :return: The matching_type of this StreamResponse.
        :rtype: str
        """
        return self._matching_type

    @matching_type.setter
    def matching_type(self, matching_type):
        """
        Sets the matching_type of this StreamResponse. :param matching_type: The matching_type of this StreamResponse.
        :type: str
        """

        self._matching_type = matching_type

    @property
    def description(self):
        """
        Gets the description of this StreamResponse. :return: The description of this StreamResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StreamResponse. :param description: The description of this StreamResponse.
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """
        Gets the created_at of this StreamResponse. :return: The created_at of this StreamResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this StreamResponse. :param created_at: The created_at of this StreamResponse.
        :type: str
        """

        self._created_at = created_at

    @property
    def disabled(self):
        """
        Gets the disabled of this StreamResponse. :return: The disabled of this StreamResponse.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this StreamResponse. :param disabled: The disabled of this StreamResponse.
        :type: bool
        """

        self._disabled = disabled

    @property
    def rules(self):
        """
        Gets the rules of this StreamResponse. :return: The rules of this StreamResponse.
        :rtype: list[object]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this StreamResponse. :param rules: The rules of this StreamResponse.
        :type: list[object]
        """

        self._rules = rules

    @property
    def alert_conditions(self):
        """
        Gets the alert_conditions of this StreamResponse. :return: The alert_conditions of this StreamResponse.
        :rtype: list[object]
        """
        return self._alert_conditions

    @alert_conditions.setter
    def alert_conditions(self, alert_conditions):
        """
        Sets the alert_conditions of this StreamResponse. :param alert_conditions: The alert_conditions of this StreamResponse.
        :type: list[object]
        """

        self._alert_conditions = alert_conditions

    @property
    def alert_receivers(self):
        """
        Gets the alert_receivers of this StreamResponse. :return: The alert_receivers of this StreamResponse.
        :rtype: object
        """
        return self._alert_receivers

    @alert_receivers.setter
    def alert_receivers(self, alert_receivers):
        """
        Sets the alert_receivers of this StreamResponse. :param alert_receivers: The alert_receivers of this StreamResponse.
        :type: object
        """

        self._alert_receivers = alert_receivers

    @property
    def title(self):
        """
        Gets the title of this StreamResponse. :return: The title of this StreamResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this StreamResponse. :param title: The title of this StreamResponse.
        :type: str
        """

        self._title = title

    @property
    def content_pack(self):
        """
        Gets the content_pack of this StreamResponse. :return: The content_pack of this StreamResponse.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this StreamResponse. :param content_pack: The content_pack of this StreamResponse.
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
