import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger



class StreamsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def clone_stream(self, stream_id, json_body, **kwargs):
        """
        Clone a stream


        >>> thread = api.clone_stream(stream_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :param CloneStreamRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.clone_stream_with_http_info(stream_id, json_body, **kwargs)
        else:
            (data) = self.clone_stream_with_http_info(stream_id, json_body, **kwargs)
            return data

    def clone_stream_with_http_info(self, stream_id, json_body, **kwargs):
        """
        Clone a stream


        >>> thread = api.clone_stream_with_http_info(stream_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :param CloneStreamRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `clone_stream`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `clone_stream`")

        resource_path = '/streams/{streamId}/clone'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

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

    def create(self, json_body, **kwargs):
        """
        Create a stream


        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateStreamRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(json_body, **kwargs)
        else:
            (data) = self.create_with_http_info(json_body, **kwargs)
            return data

    def create_with_http_info(self, json_body, **kwargs):
        """
        Create a stream


        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateStreamRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
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

        resource_path = '/streams'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, stream_id, **kwargs):
        """
        Delete a stream


        >>> thread = api.delete(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(stream_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(stream_id, **kwargs)
            return data

    def delete_with_http_info(self, stream_id, **kwargs):
        """
        Delete a stream


        >>> thread = api.delete_with_http_info(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `delete`")

        resource_path = '/streams/{streamId}'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, **kwargs):
        """
        Get a list of all streams


        >>> thread = api.get(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: StreamListResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(**kwargs)
        else:
            (data) = self.get_with_http_info(**kwargs)
            return data

    def get_with_http_info(self, **kwargs):
        """
        Get a list of all streams


        >>> thread = api.get_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: StreamListResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/streams'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='StreamListResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_0(self, stream_id, **kwargs):
        """
        Get a single stream


        >>> thread = api.get_0(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: StreamResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_0_with_http_info(stream_id, **kwargs)
        else:
            (data) = self.get_0_with_http_info(stream_id, **kwargs)
            return data

    def get_0_with_http_info(self, stream_id, **kwargs):
        """
        Get a single stream


        >>> thread = api.get_0_with_http_info(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: StreamResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `get_0`")

        resource_path = '/streams/{streamId}'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='StreamResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_enabled(self, **kwargs):
        """
        Get a list of all enabled streams


        >>> thread = api.get_enabled(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: StreamListResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_enabled_with_http_info(**kwargs)
        else:
            (data) = self.get_enabled_with_http_info(**kwargs)
            return data

    def get_enabled_with_http_info(self, **kwargs):
        """
        Get a list of all enabled streams


        >>> thread = api.get_enabled_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: StreamListResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/streams/enabled'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='StreamListResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def pause(self, stream_id, **kwargs):
        """
        Pause a stream


        >>> thread = api.pause(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pause_with_http_info(stream_id, **kwargs)
        else:
            (data) = self.pause_with_http_info(stream_id, **kwargs)
            return data

    def pause_with_http_info(self, stream_id, **kwargs):
        """
        Pause a stream


        >>> thread = api.pause_with_http_info(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `pause`")

        resource_path = '/streams/{streamId}/pause'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def resume(self, stream_id, **kwargs):
        """
        Resume a stream


        >>> thread = api.resume(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.resume_with_http_info(stream_id, **kwargs)
        else:
            (data) = self.resume_with_http_info(stream_id, **kwargs)
            return data

    def resume_with_http_info(self, stream_id, **kwargs):
        """
        Resume a stream


        >>> thread = api.resume_with_http_info(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `resume`")

        resource_path = '/streams/{streamId}/resume'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def test_match(self, stream_id, json_body, **kwargs):
        """
        Test matching of a stream against a supplied message


        >>> thread = api.test_match(stream_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :param Map json_body:  (required)
        :return: TestMatchResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_match_with_http_info(stream_id, json_body, **kwargs)
        else:
            (data) = self.test_match_with_http_info(stream_id, json_body, **kwargs)
            return data

    def test_match_with_http_info(self, stream_id, json_body, **kwargs):
        """
        Test matching of a stream against a supplied message


        >>> thread = api.test_match_with_http_info(stream_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :param Map json_body:  (required)
        :return: TestMatchResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `test_match`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `test_match`")

        resource_path = '/streams/{streamId}/testMatch'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='TestMatchResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update(self, stream_id, json_body, **kwargs):
        """
        Update a stream


        >>> thread = api.update(stream_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :param UpdateStreamRequest json_body:  (required)
        :return: StreamResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(stream_id, json_body, **kwargs)
        else:
            (data) = self.update_with_http_info(stream_id, json_body, **kwargs)
            return data

    def update_with_http_info(self, stream_id, json_body, **kwargs):
        """
        Update a stream


        >>> thread = api.update_with_http_info(stream_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :param UpdateStreamRequest json_body:  (required)
        :return: StreamResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['stream_id', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stream_id' is set
        if ('stream_id' not in params) or (params['stream_id'] is None):
            raise ValueError("Missing the required parameter `stream_id` when calling `update`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update`")

        resource_path = '/streams/{streamId}'.replace('{format}', 'json')
        path_params = {}
        if 'stream_id' in params:
            path_params['streamId'] = params['stream_id']

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

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='StreamResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
