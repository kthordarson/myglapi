import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger



class SystemloggersApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def loggers(self, **kwargs):
        """
        List all loggers and their current levels


        >>> thread = api.loggers(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: LoggersSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.loggers_with_http_info(**kwargs)
        else:
            (data) = self.loggers_with_http_info(**kwargs)
            return data

    def loggers_with_http_info(self, **kwargs):
        """
        List all loggers and their current levels


        >>> thread = api.loggers_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: LoggersSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']

        resource_path = '/system/loggers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='LoggersSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def messages(self, **kwargs):
        """
        Get recent internal log messages


        >>> thread = api.messages(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object limit: How many log messages should be returned
        :param Object level: Which log level (or higher) should the messages have
        :return: LogMessagesSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.messages_with_http_info(**kwargs)
        else:
            (data) = self.messages_with_http_info(**kwargs)
            return data

    def messages_with_http_info(self, **kwargs):
        """
        Get recent internal log messages


        >>> thread = api.messages_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object limit: How many log messages should be returned
        :param Object level: Which log level (or higher) should the messages have
        :return: LogMessagesSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['limit', 'level']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']

        resource_path = '/system/loggers/messages/recent'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'level' in params:
            query_params['level'] = params['level']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='LogMessagesSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def set_single_logger_level(self, logger_name, level, **kwargs):
        """
        Set the loglevel of a single logger
        Provided level is falling back to DEBUG if it does not exist

        >>> thread = api.set_single_logger_level(logger_name, level, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object logger_name:  (required)
        :param Object level:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_single_logger_level_with_http_info(logger_name, level, **kwargs)
        else:
            (data) = self.set_single_logger_level_with_http_info(logger_name, level, **kwargs)
            return data

    def set_single_logger_level_with_http_info(self, logger_name, level, **kwargs):
        """
        Set the loglevel of a single logger
        Provided level is falling back to DEBUG if it does not exist

        >>> thread = api.set_single_logger_level_with_http_info(logger_name, level, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object logger_name:  (required)
        :param Object level:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['logger_name', 'level']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'logger_name' is set
        if ('logger_name' not in params) or (params['logger_name'] is None):
            raise ValueError("Missing the required parameter `logger_name` when calling `set_single_logger_level`")
        # verify the required parameter 'level' is set
        if ('level' not in params) or (params['level'] is None):
            raise ValueError("Missing the required parameter `level` when calling `set_single_logger_level`")

        resource_path = '/system/loggers/{loggerName}/level/{level}'.replace('{format}', 'json')
        path_params = {}
        if 'logger_name' in params:
            path_params['loggerName'] = params['logger_name']
        if 'level' in params:
            path_params['level'] = params['level']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))


    def set_subsystem_logger_level(self, subsystem, level, **kwargs):
        """
        Set the loglevel of a whole subsystem
        Provided level is falling back to DEBUG if it does not exist

        >>> thread = api.set_subsystem_logger_level(subsystem, level, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object subsystem:  (required)
        :param Object level:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_subsystem_logger_level_with_http_info(subsystem, level, **kwargs)
        else:
            (data) = self.set_subsystem_logger_level_with_http_info(subsystem, level, **kwargs)
            return data

    def set_subsystem_logger_level_with_http_info(self, subsystem, level, **kwargs):
        """
        Set the loglevel of a whole subsystem
        Provided level is falling back to DEBUG if it does not exist

        >>> thread = api.set_subsystem_logger_level_with_http_info(subsystem, level, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object subsystem:  (required)
        :param Object level:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['subsystem', 'level']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subsystem' is set
        if ('subsystem' not in params) or (params['subsystem'] is None):
            raise ValueError("Missing the required parameter `subsystem` when calling `set_subsystem_logger_level`")
        # verify the required parameter 'level' is set
        if ('level' not in params) or (params['level'] is None):
            raise ValueError("Missing the required parameter `level` when calling `set_subsystem_logger_level`")

        resource_path = '/system/loggers/subsystems/{subsystem}/level/{level}'.replace('{format}', 'json')
        path_params = {}
        if 'subsystem' in params:
            path_params['subsystem'] = params['subsystem']
        if 'level' in params:
            path_params['level'] = params['level']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))


    def subsystems(self, **kwargs):
        """
        List all logger subsystems and their current levels


        >>> thread = api.subsystems(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: SubsystemSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.subsystems_with_http_info(**kwargs)
        else:
            (data) = self.subsystems_with_http_info(**kwargs)
            return data

    def subsystems_with_http_info(self, **kwargs):
        """
        List all logger subsystems and their current levels


        >>> thread = api.subsystems_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: SubsystemSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']

        resource_path = '/system/loggers/subsystems'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SubsystemSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
