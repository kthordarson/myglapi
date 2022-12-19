

from pprint import pformat
from six import iteritems
import re


class SubsystemSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, subsystems=None):
        """
        SubsystemSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'subsystems': 'object'
        }

        self.attribute_map = {
            'subsystems': 'subsystems'
        }

        self._subsystems = subsystems

    @property
    def subsystems(self):
        """
        Gets the subsystems of this SubsystemSummary.


        :return: The subsystems of this SubsystemSummary.
        :rtype: object
        """
        return self._subsystems

    @subsystems.setter
    def subsystems(self, subsystems):
        """
        Sets the subsystems of this SubsystemSummary.


        :param subsystems: The subsystems of this SubsystemSummary.
        :type: object
        """

        self._subsystems = subsystems

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
