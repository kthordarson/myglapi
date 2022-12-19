import base64
import urllib3
import http.client #  as httplib

import sys
from loguru import logger

from six import iteritems

import os

def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton@singleton
class Configuration(object):
    def __init__(self):
        """
        Constructor
        """
        # Default Base url
        self.host = os.getenv("GRAYLOG_HOST")
        # Default api client
        self.api_client = None
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {os.getenv("GRAYLOG_APIKEY")}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # Username for HTTP basic authentication
        self.username = os.getenv("GRAYLOG_USER")
        # Password for HTTP basic authentication
        self.password = os.getenv("GRAYLOG_PASS")

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logger #.getLogger("graylog")
        self.logger["urllib3_logger"] = logger #.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None

    @property
    def logger_file(self):
        """
        Gets the logger_file.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        pass

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        pass

    @property
    def logger_format(self):
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        self.__logger_format = value
        # self.logger_formatter = logger.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        if self.api_key.get(identifier) and self.api_key_prefix.get(identifier):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        token = None
        try:
            token = urllib3.util.make_headers(basic_auth=self.username + ':' + self.password).get('authorization')
        except TypeError as e:
            logger.error(e)
        return token

    def auth_settings(self):
        return {}

    def to_debug_report(self):
        return "Python SDK Debug Report:\n OS: {env}\n Python Version: {pyversion}\n Version of the API: 2.1.1+01d50e5\n SDK Package Version: 1.0.0".format(env=sys.platform, pyversion=sys.version)
