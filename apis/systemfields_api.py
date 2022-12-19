import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from configuration import Configuration
from api_client import ApiClient


class SystemfieldsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def fields(self, **kwargs):
        """
        Get list of message fields that exist
        This operation is comparably fast because it reads directly from the indexer mapping.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fields(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object limit: Maximum number of fields to return. Set to 0 for all fields.
        :return: Map
                 If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.fields_with_http_info(**kwargs)
        else:
            (data) = self.fields_with_http_info(**kwargs)
            return data

    def fields_with_http_info(self, **kwargs):
        """
        Get list of message fields that exist
        This operation is comparably fast because it reads directly from the indexer mapping.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fields_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object limit: Maximum number of fields to return. Set to 0 for all fields.
        :return: Map
                 If the method is called asynchronously, returns the request thread.
        """

        all_params = ['limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fields" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/fields'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
