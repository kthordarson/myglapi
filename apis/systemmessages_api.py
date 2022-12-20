import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemmessagesApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def all(self, **kwargs):
        """
        Get internal Graylog system messages
        

        >>> thread = api.all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object page: Page
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.all_with_http_info(**kwargs)
        else:
            (data) = self.all_with_http_info(**kwargs)
            return data

    def all_with_http_info(self, **kwargs):
        """
        Get internal Graylog system messages
        

        >>> thread = api.all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object page: Page
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """

        all_params = ['page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/messages'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
