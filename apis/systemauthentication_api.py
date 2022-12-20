import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemauthenticationApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, config, **kwargs):
        """
        Update authentication providers configuration


        >>> thread = api.create(config, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param AuthenticationConfig config:  (required)
        :return:\s AuthenticationConfig If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(config, **kwargs)
        else:
            (data) = self.create_with_http_info(config, **kwargs)
            return data

    def create_with_http_info(self, config, **kwargs):
        """
        Update authentication providers configuration


        >>> thread = api.create_with_http_info(config, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param AuthenticationConfig config:  (required)
        :return:\s AuthenticationConfig If the method is called asynchronously, returns the request thread.
        """

        all_params = ['config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'config' is set
        if ('config' not in params) or (params['config'] is None):
            raise ValueError("Missing the required parameter `config` when calling `create`")

        resource_path = '/system/authentication/config'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'config' in params:
            body_params = params['config']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='AuthenticationConfig', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_authenticators(self, **kwargs):
        """
        Retrieve authentication providers configuration


        >>> thread = api.get_authenticators(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s AuthenticationConfig If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_authenticators_with_http_info(**kwargs)
        else:
            (data) = self.get_authenticators_with_http_info(**kwargs)
            return data

    def get_authenticators_with_http_info(self, **kwargs):
        """
        Retrieve authentication providers configuration


        >>> thread = api.get_authenticators_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s AuthenticationConfig If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/authentication/config'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='AuthenticationConfig', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
