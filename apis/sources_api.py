import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SourcesApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list(self, range, **kwargs):
        """
        Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.
        Range: The parameter is in seconds relative to the current time. 86400 means 'in the last day',0 is special and means 'across all indices'

        >>> thread = api.list(range, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object range: Relative timeframe to search in. See method description. (required)
        :param Object size: Maximum size of the result set.
        :return:\s SourcesList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(range, **kwargs)
        else:
            (data) = self.list_with_http_info(range, **kwargs)
            return data

    def list_with_http_info(self, range, **kwargs):
        """
        Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.
        Range: The parameter is in seconds relative to the current time. 86400 means 'in the last day',0 is special and means 'across all indices'

        >>> thread = api.list_with_http_info(range, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object range: Relative timeframe to search in. See method description. (required)
        :param Object size: Maximum size of the result set.
        :return:\s SourcesList If the method is called asynchronously, returns the request thread.
        """

        all_params = ['range', 'size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'range' is set
        if ('range' not in params) or (params['range'] is None):
            raise ValueError("Missing the required parameter `range` when calling `list`")

        resource_path = '/sources'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'range' in params:
            query_params['range'] = params['range']
        if 'size' in params:
            query_params['size'] = params['size']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SourcesList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
