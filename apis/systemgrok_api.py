import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class SystemgrokApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def bulk_update_patterns(self, patterns, **kwargs):
        """
        Add a list of new patterns


        >>> thread = api.bulk_update_patterns(patterns, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param GrokPatternList patterns:  (required)
        :param Object replace: Replace all patterns with the new ones.
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.bulk_update_patterns_with_http_info(patterns, **kwargs)
        else:
            (data) = self.bulk_update_patterns_with_http_info(patterns, **kwargs)
            return data

    def bulk_update_patterns_with_http_info(self, patterns, **kwargs):
        """
        Add a list of new patterns


        >>> thread = api.bulk_update_patterns_with_http_info(patterns, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param GrokPatternList patterns:  (required)
        :param Object replace: Replace all patterns with the new ones.
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['patterns', 'replace']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'patterns' is set
        if ('patterns' not in params) or (params['patterns'] is None):
            raise ValueError("Missing the required parameter `patterns` when calling `bulk_update_patterns`")

        resource_path = '/system/grok'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'replace' in params:
            query_params['replace'] = params['replace']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patterns' in params:
            body_params = params['patterns']

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


    def create_pattern(self, pattern, **kwargs):
        """
        Add a new named pattern


        >>> thread = api.create_pattern(pattern, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param GrokPatternSummary pattern:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_pattern_with_http_info(pattern, **kwargs)
        else:
            (data) = self.create_pattern_with_http_info(pattern, **kwargs)
            return data

    def create_pattern_with_http_info(self, pattern, **kwargs):
        """
        Add a new named pattern


        >>> thread = api.create_pattern_with_http_info(pattern, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param GrokPatternSummary pattern:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['pattern']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pattern' is set
        if ('pattern' not in params) or (params['pattern'] is None):
            raise ValueError("Missing the required parameter `pattern` when calling `create_pattern`")

        resource_path = '/system/grok'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pattern' in params:
            body_params = params['pattern']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_grok_patterns(self, **kwargs):
        """
        Get all existing grok patterns


        >>> thread = api.list_grok_patterns(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: GrokPatternList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_grok_patterns_with_http_info(**kwargs)
        else:
            (data) = self.list_grok_patterns_with_http_info(**kwargs)
            return data

    def list_grok_patterns_with_http_info(self, **kwargs):
        """
        Get all existing grok patterns


        >>> thread = api.list_grok_patterns_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: GrokPatternList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/grok'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='GrokPatternList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_pattern(self, pattern_id, **kwargs):
        """
        Get the existing grok pattern


        >>> thread = api.list_pattern(pattern_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object pattern_id:  (required)
        :return: GrokPattern If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_pattern_with_http_info(pattern_id, **kwargs)
        else:
            (data) = self.list_pattern_with_http_info(pattern_id, **kwargs)
            return data

    def list_pattern_with_http_info(self, pattern_id, **kwargs):
        """
        Get the existing grok pattern


        >>> thread = api.list_pattern_with_http_info(pattern_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object pattern_id:  (required)
        :return: GrokPattern If the method is called asynchronously, returns the request thread.
        """

        all_params = ['pattern_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pattern_id' is set
        if ('pattern_id' not in params) or (params['pattern_id'] is None):
            raise ValueError("Missing the required parameter `pattern_id` when calling `list_pattern`")

        resource_path = '/system/grok/{patternId}'.replace('{format}', 'json')
        path_params = {}
        if 'pattern_id' in params:
            path_params['patternId'] = params['pattern_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='GrokPattern', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def remove_pattern(self, **kwargs):
        """
        Remove an existing pattern by id


        >>> thread = api.remove_pattern(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_pattern_with_http_info(**kwargs)
        else:
            (data) = self.remove_pattern_with_http_info(**kwargs)
            return data

    def remove_pattern_with_http_info(self, **kwargs):
        """
        Remove an existing pattern by id


        >>> thread = api.remove_pattern_with_http_info(callback=callback_function)

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

        resource_path = '/system/grok/{patternId}'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update_pattern(self, pattern_id, pattern, **kwargs):
        """
        Update an existing pattern


        >>> thread = api.update_pattern(pattern_id, pattern, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object pattern_id:  (required)
        :param GrokPatternSummary pattern:  (required)
        :return: GrokPattern If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_pattern_with_http_info(pattern_id, pattern, **kwargs)
        else:
            (data) = self.update_pattern_with_http_info(pattern_id, pattern, **kwargs)
            return data

    def update_pattern_with_http_info(self, pattern_id, pattern, **kwargs):
        """
        Update an existing pattern


        >>> thread = api.update_pattern_with_http_info(pattern_id, pattern, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object pattern_id:  (required)
        :param GrokPatternSummary pattern:  (required)
        :return: GrokPattern If the method is called asynchronously, returns the request thread.
        """

        all_params = ['pattern_id', 'pattern']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pattern_id' is set
        if ('pattern_id' not in params) or (params['pattern_id'] is None):
            raise ValueError("Missing the required parameter `pattern_id` when calling `update_pattern`")
        # verify the required parameter 'pattern' is set
        if ('pattern' not in params) or (params['pattern'] is None):
            raise ValueError("Missing the required parameter `pattern` when calling `update_pattern`")

        resource_path = '/system/grok/{patternId}'.replace('{format}', 'json')
        path_params = {}
        if 'pattern_id' in params:
            path_params['patternId'] = params['pattern_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pattern' in params:
            body_params = params['pattern']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='GrokPattern', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
