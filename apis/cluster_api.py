from loguru import logger
import sys
import os
import re

from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class ClusterApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get(self, **kwargs):
        """
        Get system overview of all Graylog nodes
        >>> thread = api.get(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(**kwargs)
        else:
            (data) = self.get_with_http_info(**kwargs)
            return data

    def get_with_http_info(self, **kwargs):
        """
        Get system overview of all Graylog nodes


        >>> thread = api.get_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Map If the method is called asynchronously, returns the request thread.
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

        resource_path = '/cluster'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def jvm(self, node_id, **kwargs):
        """
        Get JVM information of the given node


        >>> thread = api.jvm(node_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object node_id: The id of the node where processing will be paused. (required)
        :return: SystemJVMResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.jvm_with_http_info(node_id, **kwargs)
        else:
            (data) = self.jvm_with_http_info(node_id, **kwargs)
            return data

    def jvm_with_http_info(self, node_id, **kwargs):
        """
        Get JVM information of the given node


        >>> thread = api.jvm_with_http_info(node_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object node_id: The id of the node where processing will be paused. (required)
        :return: SystemJVMResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['node_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params) or (params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `jvm`")

        resource_path = '/cluster/{nodeId}/jvm'.replace('{format}', 'json')
        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SystemJVMResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def thread_dump(self, node_id, **kwargs):
        """
        Get a thread dump of the given node


        >>> thread = api.thread_dump(node_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object node_id: The id of the node where processing will be paused. (required)
        :return: SystemThreadDumpResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.thread_dump_with_http_info(node_id, **kwargs)
        else:
            (data) = self.thread_dump_with_http_info(node_id, **kwargs)
            return data

    def thread_dump_with_http_info(self, node_id, **kwargs):
        """
        Get a thread dump of the given node


        >>> thread = api.thread_dump_with_http_info(node_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object node_id: The id of the node where processing will be paused. (required)
        :return: SystemThreadDumpResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['node_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_id' is set
        if ('node_id' not in params) or (params['node_id'] is None):
            raise ValueError("Missing the required parameter `node_id` when calling `thread_dump`")

        resource_path = '/cluster/{nodeId}/threaddump'.replace('{format}', 'json')
        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SystemThreadDumpResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
