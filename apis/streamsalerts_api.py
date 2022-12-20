import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class StreamsalertsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list_all(self, **kwargs):
        """
        Get the 300 most recent alarms of all streams
        >>> thread = api.list_all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object since: Optional parameter to define a lower date boundary. (UNIX timestamp)
        :return:\s AlertListSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_all_with_http_info(**kwargs)
        else:
            (data) = self.list_all_with_http_info(**kwargs)
            return data

    def list_all_with_http_info(self, **kwargs):
        """
        Get the 300 most recent alarms of all streams
        >>> thread = api.list_all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object since: Optional parameter to define a lower date boundary. (UNIX timestamp)
        :return:\s AlertListSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']

        resource_path = '/streams/alerts'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='AlertListSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
