import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class SystemindexerindicesApi(object):
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
        List all open, closed and reopened indices
        >>> thread = api.all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: AllIndices If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.all_with_http_info(**kwargs)
        else:
            (data) = self.all_with_http_info(**kwargs)
            return data

    def all_with_http_info(self, **kwargs):
        """
        List all open, closed and reopened indices
        >>> thread = api.all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: AllIndices If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/indexer/indices'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='AllIndices', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def close(self, index, **kwargs):
        """
        Close an index. This will also trigger an index ranges rebuild job
        >>> thread = api.close(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.close_with_http_info(index, **kwargs)
        else:
            (data) = self.close_with_http_info(index, **kwargs)
            return data

    def close_with_http_info(self, index, **kwargs):
        """
        Close an index. This will also trigger an index ranges rebuild job
        >>> thread = api.close_with_http_info(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['index']
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
            raise ValueError("Missing the required parameter `index` when calling `close`")

        resource_path = '/system/indexer/indices/{index}/close'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def closed(self, **kwargs):
        """
        Get a list of closed indices that can be reopened
        >>> thread = api.closed(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: ClosedIndices If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.closed_with_http_info(**kwargs)
        else:
            (data) = self.closed_with_http_info(**kwargs)
            return data

    def closed_with_http_info(self, **kwargs):
        """
        Get a list of closed indices that can be reopened
        >>> thread = api.closed_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: ClosedIndices If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/indexer/indices/closed'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ClosedIndices', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, index, **kwargs):
        """
        Delete an index. This will also trigger an index ranges rebuild job
        >>> thread = api.delete(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(index, **kwargs)
        else:
            (data) = self.delete_with_http_info(index, **kwargs)
            return data

    def delete_with_http_info(self, index, **kwargs):
        """
        Delete an index. This will also trigger an index ranges rebuild job
        >>> thread = api.delete_with_http_info(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['index']
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
            raise ValueError("Missing the required parameter `index` when calling `delete`")

        resource_path = '/system/indexer/indices/{index}'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']

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

    def multiple(self, requested_indices, **kwargs):
        """
        Get information of all specified indices and their shards
        >>> thread = api.multiple(requested_indices, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param IndicesReadRequest requested_indices:  (required)
        :return: Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.multiple_with_http_info(requested_indices, **kwargs)
        else:
            (data) = self.multiple_with_http_info(requested_indices, **kwargs)
            return data

    def multiple_with_http_info(self, requested_indices, **kwargs):
        """
        Get information of all specified indices and their shards
        >>> thread = api.multiple_with_http_info(requested_indices, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param IndicesReadRequest requested_indices:  (required)
        :return: Map If the method is called asynchronously, returns the request thread.
        """

        all_params = ['requested_indices']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'requested_indices' is set
        if ('requested_indices' not in params) or (params['requested_indices'] is None):
            raise ValueError("Missing the required parameter `requested_indices` when calling `multiple`")

        resource_path = '/system/indexer/indices/multiple'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'requested_indices' in params:
            body_params = params['requested_indices']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def open(self, **kwargs):
        """
        Get information of all open indices managed by Graylog and their shards
        >>> thread = api.open(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: OpenIndicesInfo If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.open_with_http_info(**kwargs)
        else:
            (data) = self.open_with_http_info(**kwargs)
            return data

    def open_with_http_info(self, **kwargs):
        """
        Get information of all open indices managed by Graylog and their shards
        >>> thread = api.open_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: OpenIndicesInfo If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/indexer/indices/open'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='OpenIndicesInfo', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def reopen(self, index, **kwargs):
        """
        Reopen a closed index. This will also trigger an index ranges rebuild job
        >>> thread = api.reopen(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.reopen_with_http_info(index, **kwargs)
        else:
            (data) = self.reopen_with_http_info(index, **kwargs)
            return data

    def reopen_with_http_info(self, index, **kwargs):
        """
        Reopen a closed index. This will also trigger an index ranges rebuild job
        >>> thread = api.reopen_with_http_info(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['index']
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
            raise ValueError("Missing the required parameter `index` when calling `reopen`")

        resource_path = '/system/indexer/indices/{index}/reopen'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def reopened(self, **kwargs):
        """
        Get a list of reopened indices, which will not be cleaned by retention cleaning


        >>> thread = api.reopened(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: ClosedIndices If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.reopened_with_http_info(**kwargs)
        else:
            (data) = self.reopened_with_http_info(**kwargs)
            return data

    def reopened_with_http_info(self, **kwargs):
        """
        Get a list of reopened indices, which will not be cleaned by retention cleaning


        >>> thread = api.reopened_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: ClosedIndices If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/indexer/indices/reopened'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ClosedIndices', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def single(self, index, **kwargs):
        """
        Get information of an index and its shards
        >>> thread = api.single(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: IndexInfo If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.single_with_http_info(index, **kwargs)
        else:
            (data) = self.single_with_http_info(index, **kwargs)
            return data

    def single_with_http_info(self, index, **kwargs):
        """
        Get information of an index and its shards
        >>> thread = api.single_with_http_info(index, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object index:  (required)
        :return: IndexInfo If the method is called asynchronously, returns the request thread.
        """

        all_params = ['index']
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
            raise ValueError("Missing the required parameter `index` when calling `single`")

        resource_path = '/system/indexer/indices/{index}'.replace('{format}', 'json')
        path_params = {}
        if 'index' in params:
            path_params['index'] = params['index']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='IndexInfo', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
