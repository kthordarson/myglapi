import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class PluginsorggraylogpluginscollectorApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def copy_configuration(self, id, **kwargs):
        """
        Copy a configuration
        This is a stateless method which copies a collector configuration to one with another name

        >>> thread = api.copy_configuration(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.copy_configuration_with_http_info(id, **kwargs)
        else:
            (data) = self.copy_configuration_with_http_info(id, **kwargs)
            return data

    def copy_configuration_with_http_info(self, id, **kwargs):
        """
        Copy a configuration
        This is a stateless method which copies a collector configuration to one with another name

        >>> thread = api.copy_configuration_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key} to method copy_configuration")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `copy_configuration`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def copy_input(self, id, **kwargs):
        """
        Copy a configuration input
        This is a stateless method which copies a collector input to one with another name

        >>> thread = api.copy_input(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.copy_input_with_http_info(id, **kwargs)
        else:
            (data) = self.copy_input_with_http_info(id, **kwargs)
            return data

    def copy_input_with_http_info(self, id, **kwargs):
        """
        Copy a configuration input
        This is a stateless method which copies a collector input to one with another name

        >>> thread = api.copy_input_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `copy_input`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/inputs/{inputId}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def copy_output(self, id, **kwargs):
        """
        Copy a configuration output
        This is a stateless method which copies a collector output to one with another name

        >>> thread = api.copy_output(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.copy_output_with_http_info(id, **kwargs)
        else:
            (data) = self.copy_output_with_http_info(id, **kwargs)
            return data

    def copy_output_with_http_info(self, id, **kwargs):
        """
        Copy a configuration output
        This is a stateless method which copies a collector output to one with another name

        >>> thread = api.copy_output_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `copy_output`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/outputs/{outputId}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def copy_snippet(self, id, **kwargs):
        """
        Copy a configuration snippet
        This is a stateless method which copies a collector snippet to one with another name

        >>> thread = api.copy_snippet(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.copy_snippet_with_http_info(id, **kwargs)
        else:
            (data) = self.copy_snippet_with_http_info(id, **kwargs)
            return data

    def copy_snippet_with_http_info(self, id, **kwargs):
        """
        Copy a configuration snippet
        This is a stateless method which copies a collector snippet to one with another name

        >>> thread = api.copy_snippet_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `copy_snippet`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/snippets/{snippetId}/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def create_configuration(self, json_body, **kwargs):
        """
        Create new collector configuration
        >>> thread = api.create_configuration(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CollectorConfiguration json_body:  (required)
        :param Object create_defaults:
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_configuration_with_http_info(json_body, **kwargs)
        else:
            (data) = self.create_configuration_with_http_info(json_body, **kwargs)
            return data

    def create_configuration_with_http_info(self, json_body, **kwargs):
        """
        Create new collector configuration


        >>> thread = api.create_configuration_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CollectorConfiguration json_body:  (required)
        :param Object create_defaults:
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """

        all_params = ['json_body', 'create_defaults']
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
            raise ValueError("Missing the required parameter `json_body` when calling `create_configuration`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'create_defaults' in params:
            query_params['createDefaults'] = params['create_defaults']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorConfiguration', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def create_input(self, id, json_body, **kwargs):
        """
        Create a configuration input
        This is a stateless method which inserts a collector input

        >>> thread = api.create_input(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorInput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_input_with_http_info(id, json_body, **kwargs)
        else:
            (data) = self.create_input_with_http_info(id, json_body, **kwargs)
            return data

    def create_input_with_http_info(self, id, json_body, **kwargs):
        """
        Create a configuration input
        This is a stateless method which inserts a collector input

        >>> thread = api.create_input_with_http_info(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorInput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_input`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `create_input`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/inputs'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def create_output(self, id, json_body, **kwargs):
        """
        Create a configuration output
        This is a stateless method which inserts a collector output

        >>> thread = api.create_output(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorOutput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_output_with_http_info(id, json_body, **kwargs)
        else:
            (data) = self.create_output_with_http_info(id, json_body, **kwargs)
            return data

    def create_output_with_http_info(self, id, json_body, **kwargs):
        """
        Create a configuration output
        This is a stateless method which inserts a collector output

        >>> thread = api.create_output_with_http_info(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorOutput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_output`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `create_output`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/outputs'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def create_snippet(self, id, json_body, **kwargs):
        """
        Create a configuration snippet
        This is a stateless method which inserts a collector configuration snippet

        >>> thread = api.create_snippet(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorConfigurationSnippet json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_snippet_with_http_info(id, json_body, **kwargs)
        else:
            (data) = self.create_snippet_with_http_info(id, json_body, **kwargs)
            return data

    def create_snippet_with_http_info(self, id, json_body, **kwargs):
        """
        Create a configuration snippet
        This is a stateless method which inserts a collector configuration snippet

        >>> thread = api.create_snippet_with_http_info(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorConfigurationSnippet json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_snippet`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `create_snippet`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/snippets'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete_configuration(self, id, **kwargs):
        """
        Delete a collector configuration


        >>> thread = api.delete_configuration(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_configuration_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_configuration_with_http_info(id, **kwargs)
            return data

    def delete_configuration_with_http_info(self, id, **kwargs):
        """
        Delete a collector configuration


        >>> thread = api.delete_configuration_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_configuration`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def delete_input(self, id, **kwargs):
        """
        Delete input form configuration


        >>> thread = api.delete_input(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_input_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_input_with_http_info(id, **kwargs)
            return data

    def delete_input_with_http_info(self, id, **kwargs):
        """
        Delete input form configuration


        >>> thread = api.delete_input_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_input`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/inputs/{inputId}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def delete_output(self, id, **kwargs):
        """
        Delete output from configuration


        >>> thread = api.delete_output(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_output_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_output_with_http_info(id, **kwargs)
            return data

    def delete_output_with_http_info(self, id, **kwargs):
        """
        Delete output from configuration


        >>> thread = api.delete_output_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_output`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/outputs/{outputId}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def delete_snippet(self, id, **kwargs):
        """
        Delete snippet from configuration


        >>> thread = api.delete_snippet(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_snippet_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_snippet_with_http_info(id, **kwargs)
            return data

    def delete_snippet_with_http_info(self, id, **kwargs):
        """
        Delete snippet from configuration


        >>> thread = api.delete_snippet_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_snippet`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/snippets/{snippetId}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def get_configuration(self, collector_id, **kwargs):
        """
        Get a single collector configuration


        >>> thread = api.get_configuration(collector_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object collector_id:  (required)
        :param Object tags:
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configuration_with_http_info(collector_id, **kwargs)
        else:
            (data) = self.get_configuration_with_http_info(collector_id, **kwargs)
            return data

    def get_configuration_with_http_info(self, collector_id, **kwargs):
        """
        Get a single collector configuration


        >>> thread = api.get_configuration_with_http_info(collector_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object collector_id:  (required)
        :param Object tags:
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """

        all_params = ['collector_id', 'tags']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collector_id' is set
        if ('collector_id' not in params) or (params['collector_id'] is None):
            raise ValueError("Missing the required parameter `collector_id` when calling `get_configuration`")

        resource_path = '/plugins/org.graylog.plugins.collector/{collectorId}'.replace('{format}', 'json')
        path_params = {}
        if 'collector_id' in params:
            path_params['collectorId'] = params['collector_id']

        query_params = {}
        if 'tags' in params:
            query_params['tags'] = params['tags']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorConfiguration', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_configurations(self, id, **kwargs):
        """
        Show collector configuration details


        >>> thread = api.get_configurations(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configurations_with_http_info(id, **kwargs)
        else:
            (data) = self.get_configurations_with_http_info(id, **kwargs)
            return data

    def get_configurations_with_http_info(self, id, **kwargs):
        """
        Show collector configuration details


        >>> thread = api.get_configurations_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_configurations`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorConfiguration', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_tags(self, **kwargs):
        """
        List all used tags


        >>> thread = api.get_tags(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: List If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tags_with_http_info(**kwargs)
        else:
            (data) = self.get_tags_with_http_info(**kwargs)
            return data

    def get_tags_with_http_info(self, **kwargs):
        """
        List all used tags


        >>> thread = api.get_tags_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: List If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/tags'.replace('{format}', 'json')
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

    def list_configurations(self, **kwargs):
        """
        List all collector configurations


        >>> thread = api.list_configurations(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: CollectorConfigurationListResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_configurations_with_http_info(**kwargs)
        else:
            (data) = self.list_configurations_with_http_info(**kwargs)
            return data

    def list_configurations_with_http_info(self, **kwargs):
        """
        List all collector configurations


        >>> thread = api.list_configurations_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: CollectorConfigurationListResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.collector/configurations'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorConfigurationListResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update_configuration_name(self, id, json_body, **kwargs):
        """
        Updates a collector configuration name
        >>> thread = api.update_configuration_name(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorConfiguration json_body:  (required)
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_configuration_name_with_http_info(id, json_body, **kwargs)
        else:
            (data) = self.update_configuration_name_with_http_info(id, json_body, **kwargs)
            return data

    def update_configuration_name_with_http_info(self, id, json_body, **kwargs):
        """
        Updates a collector configuration name
        >>> thread = api.update_configuration_name_with_http_info(id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param CollectorConfiguration json_body:  (required)
        :return: CollectorConfiguration If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_configuration_name`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update_configuration_name`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/name'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorConfiguration', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update_input(self, id, input_id, json_body, **kwargs):
        """
        Update a configuration input
        This is a stateless method which updates a collector input

        >>> thread = api.update_input(id, input_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param Object input_id:  (required)
        :param CollectorInput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_input_with_http_info(id, input_id, json_body, **kwargs)
        else:
            (data) = self.update_input_with_http_info(id, input_id, json_body, **kwargs)
            return data

    def update_input_with_http_info(self, id, input_id, json_body, **kwargs):
        """
        Update a configuration input
        This is a stateless method which updates a collector input

        >>> thread = api.update_input_with_http_info(id, input_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param Object input_id:  (required)
        :param CollectorInput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'input_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_input`")
        # verify the required parameter 'input_id' is set
        if ('input_id' not in params) or (params['input_id'] is None):
            raise ValueError("Missing the required parameter `input_id` when calling `update_input`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update_input`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/inputs/{input_id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'input_id' in params:
            path_params['input_id'] = params['input_id']

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

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))


    def update_output(self, id, output_id, json_body, **kwargs):
        """
        Update a configuration output
        This is a stateless method which updates a collector output

        >>> thread = api.update_output(id, output_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param Object output_id:  (required)
        :param CollectorOutput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_output_with_http_info(id, output_id, json_body, **kwargs)
        else:
            (data) = self.update_output_with_http_info(id, output_id, json_body, **kwargs)
            return data

    def update_output_with_http_info(self, id, output_id, json_body, **kwargs):
        """
        Update a configuration output
        This is a stateless method which updates a collector output

        >>> thread = api.update_output_with_http_info(id, output_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param Object output_id:  (required)
        :param CollectorOutput json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'output_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_output`")
        # verify the required parameter 'output_id' is set
        if ('output_id' not in params) or (params['output_id'] is None):
            raise ValueError("Missing the required parameter `output_id` when calling `update_output`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update_output`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/outputs/{output_id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'output_id' in params:
            path_params['output_id'] = params['output_id']

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

        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))


    def update_snippet(self, id, snippet_id, json_body, **kwargs):
        """
        Update a configuration snippet
        This is a stateless method which updates a collector snippet

        >>> thread = api.update_snippet(id, snippet_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param Object snippet_id:  (required)
        :param CollectorConfigurationSnippet json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_snippet_with_http_info(id, snippet_id, json_body, **kwargs)
        else:
            (data) = self.update_snippet_with_http_info(id, snippet_id, json_body, **kwargs)
            return data

    def update_snippet_with_http_info(self, id, snippet_id, json_body, **kwargs):
        """
        Update a configuration snippet
        This is a stateless method which updates a collector snippet

        >>> thread = api.update_snippet_with_http_info(id, snippet_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param Object snippet_id:  (required)
        :param CollectorConfigurationSnippet json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'snippet_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_snippet`")
        # verify the required parameter 'snippet_id' is set
        if ('snippet_id' not in params) or (params['snippet_id'] is None):
            raise ValueError("Missing the required parameter `snippet_id` when calling `update_snippet`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update_snippet`")

        resource_path = '/plugins/org.graylog.plugins.collector/configurations/{id}/snippets/{snippet_id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'snippet_id' in params:
            path_params['snippet_id'] = params['snippet_id']

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
        res = None
        try:
            res = self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
        except Exception as e:
            logger.error(f'[err] {type(e)} {e}')
        return res # self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
