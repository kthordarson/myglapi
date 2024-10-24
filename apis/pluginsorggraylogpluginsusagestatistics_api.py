import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class PluginsorggraylogpluginsusagestatisticsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def show_cluster_data_set(self, **kwargs):
        """
        Show the collected anonymous usage statistics of this Graylog cluster


        >>> thread = api.show_cluster_data_set(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: ClusterDataSet If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_cluster_data_set_with_http_info(**kwargs)
        else:
            (data) = self.show_cluster_data_set_with_http_info(**kwargs)
            return data

    def show_cluster_data_set_with_http_info(self, **kwargs):
        """
        Show the collected anonymous usage statistics of this Graylog cluster


        >>> thread = api.show_cluster_data_set_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: ClusterDataSet If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.usagestatistics/cluster'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ClusterDataSet', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def show_config(self, **kwargs):
        """
        Show configuration for the anonymous usage statistics plugin


        >>> thread = api.show_config(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: UsageStatsConfigurationResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_config_with_http_info(**kwargs)
        else:
            (data) = self.show_config_with_http_info(**kwargs)
            return data

    def show_config_with_http_info(self, **kwargs):
        """
        Show configuration for the anonymous usage statistics plugin


        >>> thread = api.show_config_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: UsageStatsConfigurationResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.usagestatistics/config'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='UsageStatsConfigurationResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def show_node_data_set(self, **kwargs):
        """
        Show the collected anonymous usage statistics of this Graylog node


        >>> thread = api.show_node_data_set(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: NodeDataSet If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_node_data_set_with_http_info(**kwargs)
        else:
            (data) = self.show_node_data_set_with_http_info(**kwargs)
            return data

    def show_node_data_set_with_http_info(self, **kwargs):
        """
        Show the collected anonymous usage statistics of this Graylog node


        >>> thread = api.show_node_data_set_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: NodeDataSet If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.usagestatistics/node'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='NodeDataSet', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
