import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from configuration import Configuration
from api_client import ApiClient


class SystemindicesrotationApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def config(self, **kwargs):
        """
        Configuration of the current rotation strategy
        This resource returns the configuration of the currently used rotation strategy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RotationStrategySummary
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.config_with_http_info(**kwargs)
        else:
            (data) = self.config_with_http_info(**kwargs)
            return data

    def config_with_http_info(self, **kwargs):
        """
        Configuration of the current rotation strategy
        This resource returns the configuration of the currently used rotation strategy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RotationStrategySummary
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method config" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/indices/rotation/config'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RotationStrategySummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def config_0(self, **kwargs):
        """
        Configuration of the current rotation strategy
        This resource stores the configuration of the currently used rotation strategy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_0(, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RotationStrategySummary : The description of the rotation strategy and its configuration (required)
        :return: RotationStrategySummary
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.config_0_with_http_info(**kwargs)
        else:
            (data) = self.config_0_with_http_info(**kwargs)
            return data

    def config_0_with_http_info(self, **kwargs):
        """
        Configuration of the current rotation strategy
        This resource stores the configuration of the currently used rotation strategy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_0_with_http_info(, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RotationStrategySummary : The description of the rotation strategy and its configuration (required)
        :return: RotationStrategySummary
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = ['']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method config_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '' is set
        if ('' not in params) or (params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `config_0`")

        resource_path = '/system/indices/rotation/config'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if '' in params:
            body_params = params['']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RotationStrategySummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def config_schema(self, strategy, **kwargs):
        """
        Show JSON schema for configuration of given rotation strategies
        This resource returns a JSON schema for the configuration of the given rotation strategy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_schema(strategy, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object strategy: The name of the rotation strategy (required)
        :return: RotationStrategyDescription
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.config_schema_with_http_info(strategy, **kwargs)
        else:
            (data) = self.config_schema_with_http_info(strategy, **kwargs)
            return data

    def config_schema_with_http_info(self, strategy, **kwargs):
        """
        Show JSON schema for configuration of given rotation strategies
        This resource returns a JSON schema for the configuration of the given rotation strategy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.config_schema_with_http_info(strategy, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object strategy: The name of the rotation strategy (required)
        :return: RotationStrategyDescription
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = ['strategy']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method config_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'strategy' is set
        if ('strategy' not in params) or (params['strategy'] is None):
            raise ValueError("Missing the required parameter `strategy` when calling `config_schema`")

        resource_path = '/system/indices/rotation/strategies/{strategy}'.replace('{format}', 'json')
        path_params = {}
        if 'strategy' in params:
            path_params['strategy'] = params['strategy']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RotationStrategyDescription', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        List available rotation strategies
        This resource returns a list of all available rotation strategies on this Graylog node.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RotationStrategies
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        List available rotation strategies
        This resource returns a list of all available rotation strategies on this Graylog node.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RotationStrategies
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/indices/rotation/strategies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RotationStrategies', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))