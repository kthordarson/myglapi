import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemclusterconfigApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete(self, config_class, **kwargs):
        """
        Delete configuration settings from database


        >>> thread = api.delete(config_class, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object config_class: The name of the cluster configuration class (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(config_class, **kwargs)
        else:
            (data) = self.delete_with_http_info(config_class, **kwargs)
            return data

    def delete_with_http_info(self, config_class, **kwargs):
        """
        Delete configuration settings from database


        >>> thread = api.delete_with_http_info(config_class, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object config_class: The name of the cluster configuration class (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['config_class']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_class' is set
        if ('config_class' not in params) or (params['config_class'] is None):
            raise ValueError("Missing the required parameter `config_class` when calling `delete`")

        resource_path = '/system/cluster_config/{configClass}'.replace('{format}', 'json')
        path_params = {}
        if 'config_class' in params:
            path_params['configClass'] = params['config_class']

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

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        List all configuration classes


        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s ClusterConfigList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        List all configuration classes


        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s ClusterConfigList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/cluster_config'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ClusterConfigList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def schema(self, config_class, **kwargs):
        """
        Get JSON schema of configuration class


        >>> thread = api.schema(config_class, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object config_class: The name of the cluster configuration class (required)
        :return:\s JsonSchema If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.schema_with_http_info(config_class, **kwargs)
        else:
            (data) = self.schema_with_http_info(config_class, **kwargs)
            return data

    def schema_with_http_info(self, config_class, **kwargs):
        """
        Get JSON schema of configuration class


        >>> thread = api.schema_with_http_info(config_class, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object config_class: The name of the cluster configuration class (required)
        :return:\s JsonSchema If the method is called asynchronously, returns the request thread.
        """

        all_params = ['config_class']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_class' is set
        if ('config_class' not in params) or (params['config_class'] is None):
            raise ValueError("Missing the required parameter `config_class` when calling `schema`")

        resource_path = '/system/cluster_config/{configClass}'.replace('{format}', 'json')
        path_params = {}
        if 'config_class' in params:
            path_params['configClass'] = params['config_class']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/schema+json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='JsonSchema', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update(self, config_class, body, **kwargs):
        """
        Update configuration in database


        >>> thread = api.update(config_class, body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object config_class: The name of the cluster configuration class (required)
        :param InputStream body: The payload of the cluster configuration (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(config_class, body, **kwargs)
        else:
            (data) = self.update_with_http_info(config_class, body, **kwargs)
            return data

    def update_with_http_info(self, config_class, body, **kwargs):
        """
        Update configuration in database


        >>> thread = api.update_with_http_info(config_class, body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object config_class: The name of the cluster configuration class (required)
        :param InputStream body: The payload of the cluster configuration (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['config_class', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config_class' is set
        if ('config_class' not in params) or (params['config_class'] is None):
            raise ValueError("Missing the required parameter `config_class` when calling `update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update`")

        resource_path = '/system/cluster_config/{configClass}'.replace('{format}', 'json')
        path_params = {}
        if 'config_class' in params:
            path_params['configClass'] = params['config_class']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
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

