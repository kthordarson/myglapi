import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemindexerclusterApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cluster_health(self, **kwargs):
        """
        Get cluster and shard health overview
        

        >>> thread = api.cluster_health(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s ClusterHealth If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cluster_health_with_http_info(**kwargs)
        else:
            (data) = self.cluster_health_with_http_info(**kwargs)
            return data

    def cluster_health_with_http_info(self, **kwargs):
        """
        Get cluster and shard health overview
        

        >>> thread = api.cluster_health_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s ClusterHealth If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/indexer/cluster/health'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ClusterHealth', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def cluster_name(self, **kwargs):
        """
        Get the cluster name
        

        >>> thread = api.cluster_name(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s ClusterName If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cluster_name_with_http_info(**kwargs)
        else:
            (data) = self.cluster_name_with_http_info(**kwargs)
            return data

    def cluster_name_with_http_info(self, **kwargs):
        """
        Get the cluster name
        

        >>> thread = api.cluster_name_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s ClusterName If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/indexer/cluster/name'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ClusterName', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
