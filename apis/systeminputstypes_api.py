import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SysteminputstypesApi(object):
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
        Get information about all input types


        >>> thread = api.all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
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
        Get information about all input types


        >>> thread = api.all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/inputs/types/all'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def info(self, input_type, **kwargs):
        """
        Get information about a single input type


        >>> thread = api.info(input_type, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_type:  (required)
        :return:\s InputTypeInfo If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.info_with_http_info(input_type, **kwargs)
        else:
            (data) = self.info_with_http_info(input_type, **kwargs)
            return data

    def info_with_http_info(self, input_type, **kwargs):
        """
        Get information about a single input type


        >>> thread = api.info_with_http_info(input_type, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_type:  (required)
        :return:\s InputTypeInfo If the method is called asynchronously, returns the request thread.
        """

        all_params = ['input_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_type' is set
        if ('input_type' not in params) or (params['input_type'] is None):
            raise ValueError("Missing the required parameter `input_type` when calling `info`")

        resource_path = '/system/inputs/types/{inputType}'.replace('{format}', 'json')
        path_params = {}
        if 'input_type' in params:
            path_params['inputType'] = params['input_type']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputTypeInfo', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def types(self, **kwargs):
        """
        Get all available input types of this node


        >>> thread = api.types(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s InputTypesSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.types_with_http_info(**kwargs)
        else:
            (data) = self.types_with_http_info(**kwargs)
            return data

    def types_with_http_info(self, **kwargs):
        """
        Get all available input types of this node


        >>> thread = api.types_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s InputTypesSummary If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/inputs/types'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputTypesSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
