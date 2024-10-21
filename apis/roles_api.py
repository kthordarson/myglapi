import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class RolesApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_member(self, rolename, username, **kwargs):
        """
        Add a user to a role


        >>> thread = api.add_member(rolename, username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :param Object username:  (required)
        :param String json_body: Placeholder because PUT requests should have a body. Set to '{}', the content will be ignored.
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_member_with_http_info(rolename, username, **kwargs)
        else:
            (data) = self.add_member_with_http_info(rolename, username, **kwargs)
            return data

    def add_member_with_http_info(self, rolename, username, **kwargs):
        """
        Add a user to a role


        >>> thread = api.add_member_with_http_info(rolename, username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :param Object username:  (required)
        :param String json_body: Placeholder because PUT requests should have a body. Set to '{}', the content will be ignored.
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rolename', 'username', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rolename' is set
        if ('rolename' not in params) or (params['rolename'] is None):
            raise ValueError("Missing the required parameter `rolename` when calling `add_member`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `add_member`")

        resource_path = '/roles/{rolename}/members/{username}'.replace('{format}', 'json')
        path_params = {}
        if 'rolename' in params:
            path_params['rolename'] = params['rolename']
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
        Create a new role


        >>> thread = api.create(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param RoleResponse json_body: The new role to create (required)
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
        Create a new role


        >>> thread = api.create_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param RoleResponse json_body: The new role to create (required)
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

        resource_path = '/roles'.replace('{format}', 'json')
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

    def delete(self, rolename, **kwargs):
        """
        Remove the named role and dissociate any users from it


        >>> thread = api.delete(rolename, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(rolename, **kwargs)
        else:
            (data) = self.delete_with_http_info(rolename, **kwargs)
            return data

    def delete_with_http_info(self, rolename, **kwargs):
        """
        Remove the named role and dissociate any users from it


        >>> thread = api.delete_with_http_info(rolename, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rolename']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rolename' is set
        if ('rolename' not in params) or (params['rolename'] is None):
            raise ValueError("Missing the required parameter `rolename` when calling `delete`")

        resource_path = '/roles/{rolename}'.replace('{format}', 'json')
        path_params = {}
        if 'rolename' in params:
            path_params['rolename'] = params['rolename']

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

    def get_members(self, rolename, **kwargs):
        """
        Retrieve the role's members


        >>> thread = api.get_members(rolename, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :return: RoleMembershipResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_members_with_http_info(rolename, **kwargs)
        else:
            (data) = self.get_members_with_http_info(rolename, **kwargs)
            return data

    def get_members_with_http_info(self, rolename, **kwargs):
        """
        Retrieve the role's members


        >>> thread = api.get_members_with_http_info(rolename, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :return: RoleMembershipResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rolename']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rolename' is set
        if ('rolename' not in params) or (params['rolename'] is None):
            raise ValueError("Missing the required parameter `rolename` when calling `get_members`")

        resource_path = '/roles/{rolename}/members'.replace('{format}', 'json')
        path_params = {}
        if 'rolename' in params:
            path_params['rolename'] = params['rolename']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RoleMembershipResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list_all(self, **kwargs):
        """
        List all roles


        >>> thread = api.list_all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: RolesResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_all_with_http_info(**kwargs)
        else:
            (data) = self.list_all_with_http_info(**kwargs)
            return data

    def list_all_with_http_info(self, **kwargs):
        """
        List all roles


        >>> thread = api.list_all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: RolesResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/roles'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RolesResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def read(self, rolename, **kwargs):
        """
        Retrieve permissions for a single role


        >>> thread = api.read(rolename, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :return: RoleResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.read_with_http_info(rolename, **kwargs)
        else:
            (data) = self.read_with_http_info(rolename, **kwargs)
            return data

    def read_with_http_info(self, rolename, **kwargs):
        """
        Retrieve permissions for a single role


        >>> thread = api.read_with_http_info(rolename, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :return: RoleResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rolename']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rolename' is set
        if ('rolename' not in params) or (params['rolename'] is None):
            raise ValueError("Missing the required parameter `rolename` when calling `read`")

        resource_path = '/roles/{rolename}'.replace('{format}', 'json')
        path_params = {}
        if 'rolename' in params:
            path_params['rolename'] = params['rolename']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RoleResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def remove_member(self, rolename, username, **kwargs):
        """
        Remove a user from a role


        >>> thread = api.remove_member(rolename, username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :param Object username:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_member_with_http_info(rolename, username, **kwargs)
        else:
            (data) = self.remove_member_with_http_info(rolename, username, **kwargs)
            return data

    def remove_member_with_http_info(self, rolename, username, **kwargs):
        """
        Remove a user from a role


        >>> thread = api.remove_member_with_http_info(rolename, username, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :param Object username:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rolename', 'username']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rolename' is set
        if ('rolename' not in params) or (params['rolename'] is None):
            raise ValueError("Missing the required parameter `rolename` when calling `remove_member`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `remove_member`")

        resource_path = '/roles/{rolename}/members/{username}'.replace('{format}', 'json')
        path_params = {}
        if 'rolename' in params:
            path_params['rolename'] = params['rolename']
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

    def update(self, rolename, json_body, **kwargs):
        """
        Update an existing role


        >>> thread = api.update(rolename, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :param RoleResponse json_body: The new representation of the role (required)
        :return: RoleResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(rolename, json_body, **kwargs)
        else:
            (data) = self.update_with_http_info(rolename, json_body, **kwargs)
            return data

    def update_with_http_info(self, rolename, json_body, **kwargs):
        """
        Update an existing role


        >>> thread = api.update_with_http_info(rolename, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object rolename:  (required)
        :param RoleResponse json_body: The new representation of the role (required)
        :return: RoleResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rolename', 'json_body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rolename' is set
        if ('rolename' not in params) or (params['rolename'] is None):
            raise ValueError("Missing the required parameter `rolename` when calling `update`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `update`")

        resource_path = '/roles/{rolename}'.replace('{format}', 'json')
        path_params = {}
        if 'rolename' in params:
            path_params['rolename'] = params['rolename']

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

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RoleResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
