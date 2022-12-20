import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystembundlesApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def apply_bundle(self, bundle_id, **kwargs):
        """
        Set up entities described by content pack


        >>> thread = api.apply_bundle(bundle_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apply_bundle_with_http_info(bundle_id, **kwargs)
        else:
            (data) = self.apply_bundle_with_http_info(bundle_id, **kwargs)
            return data

    def apply_bundle_with_http_info(self, bundle_id, **kwargs):
        """
        Set up entities described by content pack


        >>> thread = api.apply_bundle_with_http_info(bundle_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['bundle_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `apply_bundle`")

        resource_path = '/system/bundles/{bundleId}/apply'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundleId'] = params['bundle_id']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def create_bundle(self, request_body, **kwargs):
        """
        Upload a content pack


        >>> thread = api.create_bundle(request_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param ConfigurationBundle request_body: Content pack (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_bundle_with_http_info(request_body, **kwargs)
        else:
            (data) = self.create_bundle_with_http_info(request_body, **kwargs)
            return data

    def create_bundle_with_http_info(self, request_body, **kwargs):
        """
        Upload a content pack


        >>> thread = api.create_bundle_with_http_info(request_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param ConfigurationBundle request_body: Content pack (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['request_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_body' is set
        if ('request_body' not in params) or (params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `create_bundle`")

        resource_path = '/system/bundles'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in params:
            body_params = params['request_body']

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

    def delete_bundle(self, bundle_id, **kwargs):
        """
        Delete content pack


        >>> thread = api.delete_bundle(bundle_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_bundle_with_http_info(bundle_id, **kwargs)
        else:
            (data) = self.delete_bundle_with_http_info(bundle_id, **kwargs)
            return data

    def delete_bundle_with_http_info(self, bundle_id, **kwargs):
        """
        Delete content pack


        >>> thread = api.delete_bundle_with_http_info(bundle_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['bundle_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `delete_bundle`")

        resource_path = '/system/bundles/{bundleId}'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundleId'] = params['bundle_id']

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

    def export_bundle(self, export_bundle, **kwargs):
        """
        Export entities as a content pack


        >>> thread = api.export_bundle(export_bundle, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param ExportBundle export_bundle: Export content pack (required)
        :return:\s ConfigurationBundle If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.export_bundle_with_http_info(export_bundle, **kwargs)
        else:
            (data) = self.export_bundle_with_http_info(export_bundle, **kwargs)
            return data

    def export_bundle_with_http_info(self, export_bundle, **kwargs):
        """
        Export entities as a content pack


        >>> thread = api.export_bundle_with_http_info(export_bundle, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param ExportBundle export_bundle: Export content pack (required)
        :return:\s ConfigurationBundle If the method is called asynchronously, returns the request thread.
        """

        all_params = ['export_bundle']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'export_bundle' is set
        if ('export_bundle' not in params) or (params['export_bundle'] is None):
            raise ValueError("Missing the required parameter `export_bundle` when calling `export_bundle`")

        resource_path = '/system/bundles/export'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'export_bundle' in params:
            body_params = params['export_bundle']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ConfigurationBundle', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_bundles(self, **kwargs):
        """
        List available content packs


        >>> thread = api.list_bundles(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Multimap If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_bundles_with_http_info(**kwargs)
        else:
            (data) = self.list_bundles_with_http_info(**kwargs)
            return data

    def list_bundles_with_http_info(self, **kwargs):
        """
        List available content packs


        >>> thread = api.list_bundles_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Multimap If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/bundles'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Multimap', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def show_bundle(self, bundle_id, **kwargs):
        """
        Show content pack


        >>> thread = api.show_bundle(bundle_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :return:\s ConfigurationBundle If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_bundle_with_http_info(bundle_id, **kwargs)
        else:
            (data) = self.show_bundle_with_http_info(bundle_id, **kwargs)
            return data

    def show_bundle_with_http_info(self, bundle_id, **kwargs):
        """
        Show content pack


        >>> thread = api.show_bundle_with_http_info(bundle_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :return:\s ConfigurationBundle If the method is called asynchronously, returns the request thread.
        """

        all_params = ['bundle_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `show_bundle`")

        resource_path = '/system/bundles/{bundleId}'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundleId'] = params['bundle_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='ConfigurationBundle', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update_bundle(self, bundle_id, request_body, **kwargs):
        """
        Update content pack


        >>> thread = api.update_bundle(bundle_id, request_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :param ConfigurationBundle request_body: Content pack (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_bundle_with_http_info(bundle_id, request_body, **kwargs)
        else:
            (data) = self.update_bundle_with_http_info(bundle_id, request_body, **kwargs)
            return data

    def update_bundle_with_http_info(self, bundle_id, request_body, **kwargs):
        """
        Update content pack


        >>> thread = api.update_bundle_with_http_info(bundle_id, request_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object bundle_id: Content pack ID (required)
        :param ConfigurationBundle request_body: Content pack (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['bundle_id', 'request_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `update_bundle`")
        # verify the required parameter 'request_body' is set
        if ('request_body' not in params) or (params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `update_bundle`")

        resource_path = '/system/bundles/{bundleId}'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundleId'] = params['bundle_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in params:
            body_params = params['request_body']

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

