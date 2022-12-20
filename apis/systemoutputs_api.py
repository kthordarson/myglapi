import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemoutputsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def available(self, **kwargs):
        """
        Get all available output modules
        

        >>> thread = api.available(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.available_with_http_info(**kwargs)
        else:
            (data) = self.available_with_http_info(**kwargs)
            return data

    def available_with_http_info(self, **kwargs):
        """
        Get all available output modules
        

        >>> thread = api.available_with_http_info(callback=callback_function)

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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method available" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/outputs/available'.replace('{format}', 'json')
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

    def create(self, json_body, **kwargs):
        """
        Create an output
        

        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateOutputRequest json_body:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(json_body, **kwargs)
        else:
            (data) = self.create_with_http_info(json_body, **kwargs)
            return data

    def create_with_http_info(self, json_body, **kwargs):
        """
        Create an output
        

        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateOutputRequest json_body:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `create`")

        resource_path = '/system/outputs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, output_id, **kwargs):
        """
        Delete output
        

        >>> thread = api.delete(output_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object output_id: The id of the output that should be deleted (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(output_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(output_id, **kwargs)
            return data

    def delete_with_http_info(self, output_id, **kwargs):
        """
        Delete output
        

        >>> thread = api.delete_with_http_info(output_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object output_id: The id of the output that should be deleted (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['output_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'output_id' is set
        if ('output_id' not in params) or (params['output_id'] is None):
            raise ValueError("Missing the required parameter `output_id` when calling `delete`")

        resource_path = '/system/outputs/{outputId}'.replace('{format}', 'json')
        path_params = {}
        if 'output_id' in params:
            path_params['outputId'] = params['output_id']

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

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, **kwargs):
        """
        Get a list of all outputs
        

        >>> thread = api.get(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s OutputListResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(**kwargs)
        else:
            (data) = self.get_with_http_info(**kwargs)
            return data

    def get_with_http_info(self, **kwargs):
        """
        Get a list of all outputs
        

        >>> thread = api.get_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s OutputListResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/system/outputs'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='OutputListResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_0(self, output_id, **kwargs):
        """
        Get specific output
        

        >>> thread = api.get_0(output_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object output_id: The id of the output we want. (required)
        :return:\s OutputSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_0_with_http_info(output_id, **kwargs)
        else:
            (data) = self.get_0_with_http_info(output_id, **kwargs)
            return data

    def get_0_with_http_info(self, output_id, **kwargs):
        """
        Get specific output
        

        >>> thread = api.get_0_with_http_info(output_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object output_id: The id of the output we want. (required)
        :return:\s OutputSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['output_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'output_id' is set
        if ('output_id' not in params) or (params['output_id'] is None):
            raise ValueError("Missing the required parameter `output_id` when calling `get_0`")

        resource_path = '/system/outputs/{outputId}'.replace('{format}', 'json')
        path_params = {}
        if 'output_id' in params:
            path_params['outputId'] = params['output_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='OutputSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update(self, output_id, json_body, **kwargs):
        """
        Update output
        

        >>> thread = api.update(output_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object output_id: The id of the output that should be deleted (required)
        :param Map json_body:  (required)
        :return:\s Output If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(output_id, json_body, **kwargs)
        else:
            (data) = self.update_with_http_info(output_id, json_body, **kwargs)
            return data

    def update_with_http_info(self, output_id, json_body, **kwargs):
        """
        Update output
        

        >>> thread = api.update_with_http_info(output_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object output_id: The id of the output that should be deleted (required)
        :param Map json_body:  (required)
        :return:\s Output If the method is called asynchronously, returns the request thread.
        """

        all_params = ['output_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'output_id' is set
        if ('output_id' not in params) or (params['output_id'] is None):
            raise ValueError("Missing the required parameter `output_id` when calling `update`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update`")

        resource_path = '/system/outputs/{outputId}'.replace('{format}', 'json')
        path_params = {}
        if 'output_id' in params:
            path_params['outputId'] = params['output_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

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

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Output', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
