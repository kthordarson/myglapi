from pprint import pformat
import re
class InputStateSummary(object):
    def __init__(self, id=None, state=None, started_at=None, detailed_message=None, message_input=None):
        """
        InputStateSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'id': 'str', 'state': 'str', 'started_at': 'datetime', 'detailed_message': 'str', 'message_input': 'object'}
        self.attribute_map = {'id': 'id', 'state': 'state', 'started_at': 'started_at', 'detailed_message': 'detailed_message', 'message_input': 'message_input'}

        self._id = id
        self._state = state
        self._started_at = started_at
        self._detailed_message = detailed_message
        self._message_input = message_input

    @property
    def id(self):
        """
        Gets the id of this InputStateSummary. :return: The id of this InputStateSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InputStateSummary. :param id: The id of this InputStateSummary.
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """
        Gets the state of this InputStateSummary. :return: The state of this InputStateSummary.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this InputStateSummary. :param state: The state of this InputStateSummary.
        :type: str
        """

        self._state = state

    @property
    def started_at(self):
        """
        Gets the started_at of this InputStateSummary. :return: The started_at of this InputStateSummary.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this InputStateSummary. :param started_at: The started_at of this InputStateSummary.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def detailed_message(self):
        """
        Gets the detailed_message of this InputStateSummary. :return: The detailed_message of this InputStateSummary.
        :rtype: str
        """
        return self._detailed_message

    @detailed_message.setter
    def detailed_message(self, detailed_message):
        """
        Sets the detailed_message of this InputStateSummary. :param detailed_message: The detailed_message of this InputStateSummary.
        :type: str
        """

        self._detailed_message = detailed_message

    @property
    def message_input(self):
        """
        Gets the message_input of this InputStateSummary. :return: The message_input of this InputStateSummary.
        :rtype: object
        """
        return self._message_input

    @message_input.setter
    def message_input(self, message_input):
        """
        Sets the message_input of this InputStateSummary. :param message_input: The message_input of this InputStateSummary.
        :type: object
        """

        self._message_input = message_input

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
