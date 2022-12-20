import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class MessagesApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def analyze(self, index, string, **kwargs):
        """
        Analyze a message string
        Returns what tokens/terms a message string (message or full_message) is split to.

        >>> thread = api.analyze(index, string, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index: The index the message containing the string is stored in. (required)
        :param Object string: The string to analyze. (required)
        :return:\s MessageTokens If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analyze_with_http_info(index, string, **kwargs)
        else:
            (data) = self.analyze_with_http_info(index, string, **kwargs)
            return data

    def analyze_with_http_info(self, index, string, **kwargs):
        """
        Analyze a message string
        Returns what tokens/terms a message string (message or full_message) is split to.

        >>> thread = api.analyze_with_http_info(index, string, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index: The index the message containing the string is stored in. (required)
        :param Object string: The string to analyze. (required)
        :return:\s MessageTokens If the method is called asynchronously, returns the request thread.
        """

        all_params = ['index', 'string']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params) or (params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `analyze`")
        # verify the required parameter 'string' is set
        if ('string' not in params) or (params['string'] is None):
            raise ValueError("Missing the required parameter `string` when calling `analyze`")

        resource_path = '/messages/{index}/analyze'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']

        query_params = {}
        if 'string' in params:
            query_params['string'] = params['string']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='MessageTokens', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def parse(self, json_body, **kwargs):
        """
        Parse a raw message


        >>> thread = api.parse(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param MessageParseRequest json_body:  (required)
        :return:\s ResultMessage If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.parse_with_http_info(json_body, **kwargs)
        else:
            (data) = self.parse_with_http_info(json_body, **kwargs)
            return data

    def parse_with_http_info(self, json_body, **kwargs):
        """
        Parse a raw message


        >>> thread = api.parse_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param MessageParseRequest json_body:  (required)
        :return:\s ResultMessage If the method is called asynchronously, returns the request thread.
        """

        all_params = ['json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `parse`")

        resource_path = '/messages/parse'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ResultMessage', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def search(self, index, message_id, **kwargs):
        """
        Get a single message
        >>> thread = api.search(index, message_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index: The index this message is stored in. (required)
        :param Object message_id:  (required)
        :return:\s ResultMessage If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_with_http_info(index, message_id, **kwargs)
        else:
            (data) = self.search_with_http_info(index, message_id, **kwargs)
            return data

    def search_with_http_info(self, index, message_id, **kwargs):
        """
        Get a single message
        >>> thread = api.search_with_http_info(index, message_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index: The index this message is stored in. (required)
        :param Object message_id:  (required)
        :return:\s ResultMessage If the method is called asynchronously, returns the request thread.
        """

        all_params = ['index', 'message_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'index' is set
        if ('index' not in params) or (params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `search`")
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `search`")

        resource_path = '/messages/{index}/{messageId}'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ResultMessage', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
