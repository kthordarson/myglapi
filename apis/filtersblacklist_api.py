import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class FiltersblacklistApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, filter_entry, **kwargs):
        """
        Create a blacklist filter
        It can take up to a second until the change is applied

        >>> thread = api.create(filter_entry, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param FilterDescription filter_entry:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(filter_entry, **kwargs)
        else:
            (data) = self.create_with_http_info(filter_entry, **kwargs)
            return data

    def create_with_http_info(self, filter_entry, **kwargs):
        """
        Create a blacklist filter
        It can take up to a second until the change is applied

        >>> thread = api.create_with_http_info(filter_entry, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param FilterDescription filter_entry:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['filter_entry']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filter_entry' is set
        if ('filter_entry' not in params) or (params['filter_entry'] is None):
            raise ValueError("Missing the required parameter `filter_entry` when calling `create`")

        resource_path = '/filters/blacklist'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filter_entry' in params:
            body_params = params['filter_entry']

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

    def delete(self, filter_id, **kwargs):
        """
        Remove the existing blacklist filter
        It can take up to a second until the change is applied

        >>> thread = api.delete(filter_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object filter_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(filter_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(filter_id, **kwargs)
            return data

    def delete_with_http_info(self, filter_id, **kwargs):
        """
        Remove the existing blacklist filter
        It can take up to a second until the change is applied

        >>> thread = api.delete_with_http_info(filter_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object filter_id:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['filter_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filter_id' is set
        if ('filter_id' not in params) or (params['filter_id'] is None):
            raise ValueError("Missing the required parameter `filter_id` when calling `delete`")

        resource_path = '/filters/blacklist/{filterId}'.replace('{format}', 'json')
        path_params = {}
        if 'filter_id' in params:
            path_params['filterId'] = params['filter_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, filter_id, **kwargs):
        """
        Get the existing blacklist filter
        

        >>> thread = api.get(filter_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object filter_id:  (required)
        :return:\s FilterDescription If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(filter_id, **kwargs)
        else:
            (data) = self.get_with_http_info(filter_id, **kwargs)
            return data

    def get_with_http_info(self, filter_id, **kwargs):
        """
        Get the existing blacklist filter
        

        >>> thread = api.get_with_http_info(filter_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object filter_id:  (required)
        :return:\s FilterDescription If the method is called asynchronously, returns the request thread.
        """

        all_params = ['filter_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filter_id' is set
        if ('filter_id' not in params) or (params['filter_id'] is None):
            raise ValueError("Missing the required parameter `filter_id` when calling `get`")

        resource_path = '/filters/blacklist/{filterId}'.replace('{format}', 'json')
        path_params = {}
        if 'filter_id' in params:
            path_params['filterId'] = params['filter_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='FilterDescription', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_all(self, **kwargs):
        """
        Get all blacklist filters
        

        >>> thread = api.get_all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Set If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_with_http_info(**kwargs)
        else:
            (data) = self.get_all_with_http_info(**kwargs)
            return data

    def get_all_with_http_info(self, **kwargs):
        """
        Get all blacklist filters
        

        >>> thread = api.get_all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Set If the method is called asynchronously, returns the request thread.
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

        resource_path = '/filters/blacklist'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Set', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update(self, filter_id, filter_entry, **kwargs):
        """
        Update an existing blacklist filter
        It can take up to a second until the change is applied

        >>> thread = api.update(filter_id, filter_entry, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object filter_id:  (required)
        :param FilterDescription filter_entry:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(filter_id, filter_entry, **kwargs)
        else:
            (data) = self.update_with_http_info(filter_id, filter_entry, **kwargs)
            return data

    def update_with_http_info(self, filter_id, filter_entry, **kwargs):
        """
        Update an existing blacklist filter
        It can take up to a second until the change is applied

        >>> thread = api.update_with_http_info(filter_id, filter_entry, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object filter_id:  (required)
        :param FilterDescription filter_entry:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['filter_id', 'filter_entry']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filter_id' is set
        if ('filter_id' not in params) or (params['filter_id'] is None):
            raise ValueError("Missing the required parameter `filter_id` when calling `update`")
        # verify the required parameter 'filter_entry' is set
        if ('filter_entry' not in params) or (params['filter_entry'] is None):
            raise ValueError("Missing the required parameter `filter_entry` when calling `update`")

        resource_path = '/filters/blacklist/{filterId}'.replace('{format}', 'json')
        path_params = {}
        if 'filter_id' in params:
            path_params['filterId'] = params['filter_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filter_entry' in params:
            body_params = params['filter_entry']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
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

