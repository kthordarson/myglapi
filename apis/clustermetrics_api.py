import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class ClustermetricsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def multiple_metrics_all_nodes(self, requested_metrics, **kwargs):
        """
        Get all metrics of all nodes in the cluster


        >>> thread = api.multiple_metrics_all_nodes(requested_metrics, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param MetricsReadRequest requested_metrics:  (required)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.multiple_metrics_all_nodes_with_http_info(requested_metrics, **kwargs)
        else:
            (data) = self.multiple_metrics_all_nodes_with_http_info(requested_metrics, **kwargs)
            return data

    def multiple_metrics_all_nodes_with_http_info(self, requested_metrics, **kwargs):
        """
        Get all metrics of all nodes in the cluster


        >>> thread = api.multiple_metrics_all_nodes_with_http_info(requested_metrics, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param MetricsReadRequest requested_metrics:  (required)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """

        all_params = ['requested_metrics']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'requested_metrics' is set
        if ('requested_metrics' not in params) or (params['requested_metrics'] is None):
            raise ValueError("Missing the required parameter `requested_metrics` when calling `multiple_metrics_all_nodes`")

        resource_path = '/cluster/metrics/multiple'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'requested_metrics' in params:
            body_params = params['requested_metrics']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
