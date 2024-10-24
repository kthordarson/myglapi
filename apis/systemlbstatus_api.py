import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class SystemlbstatusApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def override(self, status, **kwargs):
        """
        Override load balancer status of this Graylog server node. Next lifecycle change will override it again to its default. Set to ALIVE, DEAD, or THROTTLED
        >>> thread = api.override(status, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object status:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.override_with_http_info(status, **kwargs)
        else:
            (data) = self.override_with_http_info(status, **kwargs)
            return data

    def override_with_http_info(self, status, **kwargs):
        """
        Override load balancer status of this Graylog server node. Next lifecycle change will override it again to its default. Set to ALIVE, DEAD, or THROTTLED
        >>> thread = api.override_with_http_info(status, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object status:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if ('status' not in params) or (params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `override`")

        resource_path = '/system/lbstatus/override/{status}'.replace('{format}', 'json')
        path_params = {}
        if 'status' in params:
            path_params['status'] = params['status']

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

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))


    def status(self, **kwargs):
        """
        Get status of this Graylog server node for load balancers. Returns ALIVE with HTTP 200, DEAD with HTTP 503, or THROTTLED with HTTP 429
        >>> thread = api.status(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.status_with_http_info(**kwargs)
        else:
            (data) = self.status_with_http_info(**kwargs)
            return data

    def status_with_http_info(self, **kwargs):
        """
        Get status of this Graylog server node for load balancers. Returns ALIVE with HTTP 200, DEAD with HTTP 503, or THROTTLED with HTTP 429
        >>> thread = api.status_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: None If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/lbstatus'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['text/plain'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
