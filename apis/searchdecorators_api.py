import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SearchdecoratorsApi(object):
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
        Creates a message decoration configuration


        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param DecoratorImpl json_body:  (required)
        :return:\s Decorator If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(json_body, **kwargs)
        else:
            (data) = self.create_with_http_info(json_body, **kwargs)
            return data

    def create_with_http_info(self, json_body, **kwargs):
        """
        Creates a message decoration configuration


        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param DecoratorImpl json_body:  (required)
        :return:\s Decorator If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `json_body` when calling `create`")

        resource_path = '/search/decorators'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Decorator', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, decorator_id, **kwargs):
        """
        Create a decorator


        >>> thread = api.delete(decorator_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object decorator_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(decorator_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(decorator_id, **kwargs)
            return data

    def delete_with_http_info(self, decorator_id, **kwargs):
        """
        Create a decorator


        >>> thread = api.delete_with_http_info(decorator_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object decorator_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['decorator_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'decorator_id' is set
        if ('decorator_id' not in params) or (params['decorator_id'] is None):
            raise ValueError("Missing the required parameter `decorator_id` when calling `delete`")

        resource_path = '/search/decorators/{decoratorId}'.replace('{format}', 'json')
        path_params = {}
        if 'decorator_id' in params:
            path_params['decorator id'] = params['decorator_id']

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

    def get(self, **kwargs):
        """
        Returns all configured message decorations


        >>> thread = api.get(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s List If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(**kwargs)
        else:
            (data) = self.get_with_http_info(**kwargs)
            return data

    def get_with_http_info(self, **kwargs):
        """
        Returns all configured message decorations


        >>> thread = api.get_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s List If the method is called asynchronously, returns the request thread.
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

        resource_path = '/search/decorators'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='List', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_available(self, **kwargs):
        """
        Returns all available message decorations


        >>> thread = api.get_available(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_available_with_http_info(**kwargs)
        else:
            (data) = self.get_available_with_http_info(**kwargs)
            return data

    def get_available_with_http_info(self, **kwargs):
        """
        Returns all available message decorations


        >>> thread = api.get_available_with_http_info(callback=callback_function)

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

        resource_path = '/search/decorators/available'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update(self, decorator_id, json_body, **kwargs):
        """
        Update a decorator


        >>> thread = api.update(decorator_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object decorator_id:  (required)
        :param DecoratorImpl json_body:  (required)
        :return:\s Decorator If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(decorator_id, json_body, **kwargs)
        else:
            (data) = self.update_with_http_info(decorator_id, json_body, **kwargs)
            return data

    def update_with_http_info(self, decorator_id, json_body, **kwargs):
        """
        Update a decorator


        >>> thread = api.update_with_http_info(decorator_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object decorator_id:  (required)
        :param DecoratorImpl json_body:  (required)
        :return:\s Decorator If the method is called asynchronously, returns the request thread.
        """

        all_params = ['decorator_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'decorator_id' is set
        if ('decorator_id' not in params) or (params['decorator_id'] is None):
            raise ValueError("Missing the required parameter `decorator_id` when calling `update`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update`")

        resource_path = '/search/decorators/{decoratorId}'.replace('{format}', 'json')
        path_params = {}
        if 'decorator_id' in params:
            path_params['decorator id'] = params['decorator_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Decorator', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
