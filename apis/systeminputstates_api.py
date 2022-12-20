import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SysteminputstatesApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get(self, input_id, **kwargs):
        """
        Get input state for specified input id on this node


        >>> thread = api.get(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputStateSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(input_id, **kwargs)
        else:
            (data) = self.get_with_http_info(input_id, **kwargs)
            return data

    def get_with_http_info(self, input_id, **kwargs):
        """
        Get input state for specified input id on this node


        >>> thread = api.get_with_http_info(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputStateSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['input_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `get`")

        resource_path = '/system/inputstates/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'input_id' in params:
            path_params['inputId'] = params['input_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputStateSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        Get all input states of this node


        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s InputStatesList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get all input states of this node


        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s InputStatesList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/inputstates'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputStatesList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def start(self, input_id, **kwargs):
        """
        (Re-)Start specified input on this node


        >>> thread = api.start(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputCreated If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.start_with_http_info(input_id, **kwargs)
        else:
            (data) = self.start_with_http_info(input_id, **kwargs)
            return data

    def start_with_http_info(self, input_id, **kwargs):
        """
        (Re-)Start specified input on this node


        >>> thread = api.start_with_http_info(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputCreated If the method is called asynchronously, returns the request thread.
        """

        all_params = ['input_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `start`")

        resource_path = '/system/inputstates/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'input_id' in params:
            path_params['inputId'] = params['input_id']

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

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputCreated', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def stop(self, input_id, **kwargs):
        """
        Stop specified input on this node


        >>> thread = api.stop(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputDeleted If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.stop_with_http_info(input_id, **kwargs)
        else:
            (data) = self.stop_with_http_info(input_id, **kwargs)
            return data

    def stop_with_http_info(self, input_id, **kwargs):
        """
        Stop specified input on this node


        >>> thread = api.stop_with_http_info(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputDeleted If the method is called asynchronously, returns the request thread.
        """

        all_params = ['input_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `stop`")

        resource_path = '/system/inputstates/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'input_id' in params:
            path_params['inputId'] = params['input_id']

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

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputDeleted', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
