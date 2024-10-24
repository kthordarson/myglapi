import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class SystemsessionsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def new_session(self, login_request, **kwargs):
        """
        Create a new session
        This request creates a new session for a user or reactivates an existing session: the equivalent of logging in.

        >>> thread = api.new_session(login_request, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param SessionCreateRequest login_request: Username and credentials (required)
        :return: SessionResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.new_session_with_http_info(login_request, **kwargs)
        else:
            (data) = self.new_session_with_http_info(login_request, **kwargs)
            return data

    def new_session_with_http_info(self, login_request, **kwargs):
        """
        Create a new session
        This request creates a new session for a user or reactivates an existing session: the equivalent of logging in.

        >>> thread = api.new_session_with_http_info(login_request, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param SessionCreateRequest login_request: Username and credentials (required)
        :return: SessionResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['login_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'login_request' is set
        if ('login_request' not in params) or (params['login_request'] is None):
            raise ValueError("Missing the required parameter `login_request` when calling `new_session`")

        resource_path = '/system/sessions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'login_request' in params:
            body_params = params['login_request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SessionResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def terminate_session(self, session_id, **kwargs):
        """
        Terminate an existing session
        Destroys the session with the given ID: the equivalent of logging out.

        >>> thread = api.terminate_session(session_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object session_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.terminate_session_with_http_info(session_id, **kwargs)
        else:
            (data) = self.terminate_session_with_http_info(session_id, **kwargs)
            return data

    def terminate_session_with_http_info(self, session_id, **kwargs):
        """
        Terminate an existing session
        Destroys the session with the given ID: the equivalent of logging out.

        >>> thread = api.terminate_session_with_http_info(session_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object session_id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['session_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `terminate_session`")

        resource_path = '/system/sessions/{sessionId}'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

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

    def validate_session(self, **kwargs):
        """
        Validate an existing session
        Checks the session with the given ID: returns http status 204 (No Content) if session is valid.

        >>> thread = api.validate_session(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: SessionValidationResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.validate_session_with_http_info(**kwargs)
        else:
            (data) = self.validate_session_with_http_info(**kwargs)
            return data

    def validate_session_with_http_info(self, **kwargs):
        """
        Validate an existing session
        Checks the session with the given ID: returns http status 204 (No Content) if session is valid.

        >>> thread = api.validate_session_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: SessionValidationResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/sessions'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SessionValidationResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
