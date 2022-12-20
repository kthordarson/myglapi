import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemclusterApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def node(self, **kwargs):
        """
        Information about this node.
        This is returning information of this node in context to its state in the cluster. Use the system API of the node itself to get system information.

        >>> thread = api.node(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s NodeSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.node_with_http_info(**kwargs)
        else:
            (data) = self.node_with_http_info(**kwargs)
            return data

    def node_with_http_info(self, **kwargs):
        """
        Information about this node.
        This is returning information of this node in context to its state in the cluster. Use the system API of the node itself to get system information.

        >>> thread = api.node_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s NodeSummary If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/cluster/node'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='NodeSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def node_0(self, node_id, **kwargs):
        """
        Information about a node.
        This is returning information of a node in context to its state in the cluster. Use the system API of the node itself to get system information.

        >>> thread = api.node_0(node_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object node_id:  (required)
        :return:\s NodeSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.node_0_with_http_info(node_id, **kwargs)
        else:
            (data) = self.node_0_with_http_info(node_id, **kwargs)
            return data

    def node_0_with_http_info(self, node_id, **kwargs):
        """
        Information about a node.
        This is returning information of a node in context to its state in the cluster. Use the system API of the node itself to get system information.

        >>> thread = api.node_0_with_http_info(node_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object node_id:  (required)
        :return:\s NodeSummary If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `node_id` when calling `node_0`")

        resource_path = '/system/cluster/nodes/{nodeId}'.replace('{format}', 'json')
        path_params = {}
        if 'node_id' in params:
            path_params['nodeId'] = params['node_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='NodeSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def nodes(self, **kwargs):
        """
        List all active nodes in this cluster
        >>> thread = api.nodes(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s NodeSummaryList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.nodes_with_http_info(**kwargs)
        else:
            (data) = self.nodes_with_http_info(**kwargs)
            return data

    def nodes_with_http_info(self, **kwargs):
        """
        List all active nodes in this cluster
        >>> thread = api.nodes_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s NodeSummaryList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/cluster/nodes'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='NodeSummaryList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
