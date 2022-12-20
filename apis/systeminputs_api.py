import sys
import os
import re
from loguru import logger
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SysteminputsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, json_body, **kwargs):
        """
        Launch input on this node
        

        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param InputCreateRequest json_body:  (required)
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
        Launch input on this node
        

        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param InputCreateRequest json_body:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in enumerate(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `create`")

        resource_path = '/system/inputs'.replace('{format}', 'json')
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

    def get(self, input_id, **kwargs):
        """
        Get information of a single input on this node
        

        >>> thread = api.get(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(input_id, **kwargs)
        else:
            (data) = self.get_with_http_info(input_id, **kwargs)
            return data

    def get_with_http_info(self, input_id, **kwargs):
        """
        Get information of a single input on this node
        

        >>> thread = api.get_with_http_info(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s InputSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['input_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in enumerate(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `get`")

        resource_path = '/system/inputs/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'input_id' in params:
            path_params['inputId'] = params['input_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        Get all inputs
        

        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s InputsList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            data = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Get all inputs
        

        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s InputsList If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key} to method list")
            params[key] = val
        del params['kwargs']

        resource_path = '/system/inputs'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='InputsList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def terminate(self, input_id, **kwargs):
        """
        Terminate input on this node
        

        >>> thread = api.terminate(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.terminate_with_http_info(input_id, **kwargs)
        else:
            (data) = self.terminate_with_http_info(input_id, **kwargs)
            return data

    def terminate_with_http_info(self, input_id, **kwargs):
        """
        Terminate input on this node
        

        >>> thread = api.terminate_with_http_info(input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object input_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['input_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in enumerate(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `terminate`")

        resource_path = '/system/inputs/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'input_id' in params:
            path_params['inputId'] = params['input_id']

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

    def update(self, json_body, input_id, **kwargs):
        """
        Update input on this node
        

        >>> thread = api.update(json_body, input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param InputCreateRequest json_body:  (required)
        :param Object input_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(json_body, input_id, **kwargs)
        else:
            (data) = self.update_with_http_info(json_body, input_id, **kwargs)
            return data

    def update_with_http_info(self, json_body, input_id, **kwargs):
        """
        Update input on this node
        

        >>> thread = api.update_with_http_info(json_body, input_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param InputCreateRequest json_body:  (required)
        :param Object input_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['json_body', 'input_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in enumerate(params['kwargs']):
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update`")
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `update`")

        resource_path = '/system/inputs/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'input_id' in params:
            path_params['inputId'] = params['input_id']

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

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

