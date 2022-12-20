import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemindexerfailuresApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def count(self, since, **kwargs):
        """
        Total count of failed index operations since the given date.
        

        >>> thread = api.count(since, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object since: ISO8601 date (required)
        :return:\s FailureCount If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.count_with_http_info(since, **kwargs)
        else:
            (data) = self.count_with_http_info(since, **kwargs)
            return data

    def count_with_http_info(self, since, **kwargs):
        """
        Total count of failed index operations since the given date.
        

        >>> thread = api.count_with_http_info(since, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object since: ISO8601 date (required)
        :return:\s FailureCount If the method is called asynchronously, returns the request thread.
        """

        all_params = ['since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'since' is set
        if ('since' not in params) or (params['since'] is None):
            raise ValueError("Missing the required parameter `since` when calling `count`")

        resource_path = '/system/indexer/failures/count'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'since' in params:
            query_params['since'] = params['since']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='FailureCount', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def single(self, limit, offset, **kwargs):
        """
        Get a list of failed index operations.
        

        >>> thread = api.single(limit, offset, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object limit: Limit (required)
        :param Object offset: Offset (required)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.single_with_http_info(limit, offset, **kwargs)
        else:
            (data) = self.single_with_http_info(limit, offset, **kwargs)
            return data

    def single_with_http_info(self, limit, offset, **kwargs):
        """
        Get a list of failed index operations.
        

        >>> thread = api.single_with_http_info(limit, offset, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object limit: Limit (required)
        :param Object offset: Offset (required)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """

        all_params = ['limit', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method single" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params) or (params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `single`")
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `single`")

        resource_path = '/system/indexer/failures'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']

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
