

from pprint import pformat

import re
class MongoStats(object):
    def __init__(self, server_status=None, servers=None, host_info=None, build_info=None, database_stats=None):
        """
        MongoStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name and the value is attribute type.
        :param dict attributeMap: The key is attribute name and the value is json key in definition.
        """
        self.swagger_types = {'server_status': 'object', 'servers': 'list[str]', 'host_info': 'object', 'build_info': 'object', 'database_stats': 'object'}

        self.attribute_map = {'server_status': 'server_status', 'servers': 'servers', 'host_info': 'host_info', 'build_info': 'build_info', 'database_stats': 'database_stats'}

        self._server_status = server_status
        self._servers = servers
        self._host_info = host_info
        self._build_info = build_info
        self._database_stats = database_stats

    @property
    def server_status(self):
        """
        Gets the server_status of this MongoStats. :return: The server_status of this MongoStats.
        :rtype: object
        """
        return self._server_status

    @server_status.setter
    def server_status(self, server_status):
        """
        Sets the server_status of this MongoStats. :param server_status: The server_status of this MongoStats.
        :type: object
        """

        self._server_status = server_status

    @property
    def servers(self):
        """
        Gets the servers of this MongoStats. :return: The servers of this MongoStats.
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """
        Sets the servers of this MongoStats. :param servers: The servers of this MongoStats.
        :type: list[str]
        """

        self._servers = servers

    @property
    def host_info(self):
        """
        Gets the host_info of this MongoStats. :return: The host_info of this MongoStats.
        :rtype: object
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info):
        """
        Sets the host_info of this MongoStats. :param host_info: The host_info of this MongoStats.
        :type: object
        """

        self._host_info = host_info

    @property
    def build_info(self):
        """
        Gets the build_info of this MongoStats. :return: The build_info of this MongoStats.
        :rtype: object
        """
        return self._build_info

    @build_info.setter
    def build_info(self, build_info):
        """
        Sets the build_info of this MongoStats. :param build_info: The build_info of this MongoStats.
        :type: object
        """

        self._build_info = build_info

    @property
    def database_stats(self):
        """
        Gets the database_stats of this MongoStats. :return: The database_stats of this MongoStats.
        :rtype: object
        """
        return self._database_stats

    @database_stats.setter
    def database_stats(self, database_stats):
        """
        Sets the database_stats of this MongoStats. :param database_stats: The database_stats of this MongoStats.
        :type: object
        """

        self._database_stats = database_stats

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
