import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class UsersApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def change_password(self, username, json_body, **kwargs):
        """
        Update the password for a user
        >>> thread = api.change_password(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user whose password to change. (required)
        :param ChangePasswordRequest json_body: The old and new passwords. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.change_password_with_http_info(username, json_body, **kwargs)
        else:
            (data) = self.change_password_with_http_info(username, json_body, **kwargs)
            return data

    def change_password_with_http_info(self, username, json_body, **kwargs):
        """
        Update the password for a user
        >>> thread = api.change_password_with_http_info(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user whose password to change. (required)
        :param ChangePasswordRequest json_body: The old and new passwords. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `change_password`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `change_password`")

        resource_path = '/users/{username}/password'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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


    def change_user(self, username, json_body, **kwargs):
        """
        Modify user details
        >>> thread = api.change_user(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :param ChangeUserRequest json_body: Updated user information. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.change_user_with_http_info(username, json_body, **kwargs)
        else:
            (data) = self.change_user_with_http_info(username, json_body, **kwargs)
            return data

    def change_user_with_http_info(self, username, json_body, **kwargs):
        """
        Modify user details
        >>> thread = api.change_user_with_http_info(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :param ChangeUserRequest json_body: Updated user information. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `change_user`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `change_user`")

        resource_path = '/users/{username}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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


    def create(self, json_body, **kwargs):
        """
        Create a new user account
        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateUserRequest json_body: Must contain username, full_name, email, password and a list of permissions. (required)
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
        Create a new user account
        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param CreateUserRequest json_body: Must contain username, full_name, email, password and a list of permissions. (required)
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

        resource_path = '/users'.replace('{format}', 'json')
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

    def delete_permissions(self, username, **kwargs):
        """
        Revoke all permissions for a user without deleting the account
        >>> thread = api.delete_permissions(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_permissions_with_http_info(username, **kwargs)
        else:
            (data) = self.delete_permissions_with_http_info(username, **kwargs)
            return data

    def delete_permissions_with_http_info(self, username, **kwargs):
        """
        Revoke all permissions for a user without deleting the account
        >>> thread = api.delete_permissions_with_http_info(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_permissions`")

        resource_path = '/users/{username}/permissions'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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

    def delete_user(self, username, **kwargs):
        """
        Removes a user account
        >>> thread = api.delete_user(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to delete. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_user_with_http_info(username, **kwargs)
        else:
            (data) = self.delete_user_with_http_info(username, **kwargs)
            return data

    def delete_user_with_http_info(self, username, **kwargs):
        """
        Removes a user account
        >>> thread = api.delete_user_with_http_info(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to delete. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_user`")

        resource_path = '/users/{username}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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

    def edit_permissions(self, username, json_body, **kwargs):
        """
        Update a user's permission set
        >>> thread = api.edit_permissions(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :param PermissionEditRequest json_body: The list of permissions to assign to the user. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.edit_permissions_with_http_info(username, json_body, **kwargs)
        else:
            (data) = self.edit_permissions_with_http_info(username, json_body, **kwargs)
            return data

    def edit_permissions_with_http_info(self, username, json_body, **kwargs):
        """
        Update a user's permission set
        >>> thread = api.edit_permissions_with_http_info(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :param PermissionEditRequest json_body: The list of permissions to assign to the user. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `edit_permissions`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `edit_permissions`")

        resource_path = '/users/{username}/permissions'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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


    def generate_new_token(self, username, name, **kwargs):
        """
        Generates a new access token for a user


        >>> thread = api.generate_new_token(username, name, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username:  (required)
        :param Object name: Descriptive name for this token (e.g. 'cronjob')  (required)
        :param String json_body: Placeholder because POST requests should have a body. Set to '{}', the content will be ignored.
        :return: Token If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.generate_new_token_with_http_info(username, name, **kwargs)
        else:
            (data) = self.generate_new_token_with_http_info(username, name, **kwargs)
            return data

    def generate_new_token_with_http_info(self, username, name, **kwargs):
        """
        Generates a new access token for a user


        >>> thread = api.generate_new_token_with_http_info(username, name, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username:  (required)
        :param Object name: Descriptive name for this token (e.g. 'cronjob')  (required)
        :param String json_body: Placeholder because POST requests should have a body. Set to '{}', the content will be ignored.
        :return: Token If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username', 'name', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `generate_new_token`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `generate_new_token`")

        resource_path = '/users/{username}/tokens/{name}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']
        if 'name' in params:
            path_params['name'] = params['name']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Token', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, username, **kwargs):
        """
        Get user details
        The user's permissions are only included if a user asks for his own account or for users with the necessary permissions to edit permissions.

        >>> thread = api.get(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The username to return information for. (required)
        :return: UserSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(username, **kwargs)
        else:
            (data) = self.get_with_http_info(username, **kwargs)
            return data

    def get_with_http_info(self, username, **kwargs):
        """
        Get user details
        The user's permissions are only included if a user asks for his own account or for users with the necessary permissions to edit permissions.

        >>> thread = api.get_with_http_info(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The username to return information for. (required)
        :return: UserSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `get`")

        resource_path = '/users/{username}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='UserSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_tokens(self, username, **kwargs):
        """
        Retrieves the list of access tokens for a user


        >>> thread = api.list_tokens(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username:  (required)
        :return: TokenList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_tokens_with_http_info(username, **kwargs)
        else:
            (data) = self.list_tokens_with_http_info(username, **kwargs)
            return data

    def list_tokens_with_http_info(self, username, **kwargs):
        """
        Retrieves the list of access tokens for a user


        >>> thread = api.list_tokens_with_http_info(username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username:  (required)
        :return: TokenList If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `list_tokens`")

        resource_path = '/users/{username}/tokens'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='TokenList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_users(self, **kwargs):
        """
        List all users
        The permissions assigned to the users are always included.

        >>> thread = api.list_users(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: UserList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_users_with_http_info(**kwargs)
        else:
            (data) = self.list_users_with_http_info(**kwargs)
            return data

    def list_users_with_http_info(self, **kwargs):
        """
        List all users
        The permissions assigned to the users are always included.

        >>> thread = api.list_users_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: UserList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/users'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='UserList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def revoke_token(self, username, token, **kwargs):
        """
        Removes a token for a user


        >>> thread = api.revoke_token(username, token, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username:  (required)
        :param Object token:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.revoke_token_with_http_info(username, token, **kwargs)
        else:
            (data) = self.revoke_token_with_http_info(username, token, **kwargs)
            return data

    def revoke_token_with_http_info(self, username, token, **kwargs):
        """
        Removes a token for a user


        >>> thread = api.revoke_token_with_http_info(username, token, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username:  (required)
        :param Object token:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `revoke_token`")
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `revoke_token`")

        resource_path = '/users/{username}/tokens/{token}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']
        if 'token' in params:
            path_params['token'] = params['token']

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

    def save_preferences(self, username, json_body, **kwargs):
        """
        Update a user's preferences set
        >>> thread = api.save_preferences(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :param UpdateUserPreferences json_body: The map of preferences to assign to the user. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.save_preferences_with_http_info(username, json_body, **kwargs)
        else:
            (data) = self.save_preferences_with_http_info(username, json_body, **kwargs)
            return data

    def save_preferences_with_http_info(self, username, json_body, **kwargs):
        """
        Update a user's preferences set
        >>> thread = api.save_preferences_with_http_info(username, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object username: The name of the user to modify. (required)
        :param UpdateUserPreferences json_body: The map of preferences to assign to the user. (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['username', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `save_preferences`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `save_preferences`")

        resource_path = '/users/{username}/preferences'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

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

