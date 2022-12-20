import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemldapApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_ldap_settings(self, **kwargs):
        """
        Remove the LDAP configuration
        

        >>> thread = api.delete_ldap_settings(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_ldap_settings_with_http_info(**kwargs)
        else:
            (data) = self.delete_ldap_settings_with_http_info(**kwargs)
            return data

    def delete_ldap_settings_with_http_info(self, **kwargs):
        """
        Remove the LDAP configuration
        

        >>> thread = api.delete_ldap_settings_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s None If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/ldap/settings'.replace('{format}', 'json')
        path_params = {}

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

    def get_ldap_settings(self, **kwargs):
        """
        Get the LDAP configuration if it is configured
        

        >>> thread = api.get_ldap_settings(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s LdapSettingsResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_ldap_settings_with_http_info(**kwargs)
        else:
            (data) = self.get_ldap_settings_with_http_info(**kwargs)
            return data

    def get_ldap_settings_with_http_info(self, **kwargs):
        """
        Get the LDAP configuration if it is configured
        

        >>> thread = api.get_ldap_settings_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s LdapSettingsResponse If the method is called asynchronously, returns the request thread.
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

        resource_path = '/system/ldap/settings'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='LdapSettingsResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def read_group_mapping(self, **kwargs):
        """
        Get the LDAP group to Graylog role mapping
        The return value is a simple hash with keys being the LDAP group names and the values the corresponding Graylog role names.

        >>> thread = api.read_group_mapping(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.read_group_mapping_with_http_info(**kwargs)
        else:
            (data) = self.read_group_mapping_with_http_info(**kwargs)
            return data

    def read_group_mapping_with_http_info(self, **kwargs):
        """
        Get the LDAP group to Graylog role mapping
        The return value is a simple hash with keys being the LDAP group names and the values the corresponding Graylog role names.

        >>> thread = api.read_group_mapping_with_http_info(callback=callback_function)

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

        resource_path = '/system/ldap/settings/groups'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Map', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def read_groups(self, **kwargs):
        """
        Get the available LDAP groups
        

        >>> thread = api.read_groups(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Set If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.read_groups_with_http_info(**kwargs)
        else:
            (data) = self.read_groups_with_http_info(**kwargs)
            return data

    def read_groups_with_http_info(self, **kwargs):
        """
        Get the available LDAP groups
        

        >>> thread = api.read_groups_with_http_info(callback=callback_function)

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

        resource_path = '/system/ldap/groups'.replace('{format}', 'json')
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

    def test_ldap_configuration(self, configuration_to_test, **kwargs):
        """
        Test LDAP Configuration
        

        >>> thread = api.test_ldap_configuration(configuration_to_test, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param LdapTestConfigRequest configuration_to_test:  (required)
        :return:\s LdapTestConfigResponse If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_ldap_configuration_with_http_info(configuration_to_test, **kwargs)
        else:
            (data) = self.test_ldap_configuration_with_http_info(configuration_to_test, **kwargs)
            return data

    def test_ldap_configuration_with_http_info(self, configuration_to_test, **kwargs):
        """
        Test LDAP Configuration
        

        >>> thread = api.test_ldap_configuration_with_http_info(configuration_to_test, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param LdapTestConfigRequest configuration_to_test:  (required)
        :return:\s LdapTestConfigResponse If the method is called asynchronously, returns the request thread.
        """

        all_params = ['configuration_to_test']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'configuration_to_test' is set
        if ('configuration_to_test' not in params) or (params['configuration_to_test'] is None):
            raise ValueError("Missing the required parameter `configuration_to_test` when calling `test_ldap_configuration`")

        resource_path = '/system/ldap/test'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'configuration_to_test' in params:
            body_params = params['configuration_to_test']

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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='LdapTestConfigResponse', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update_group_mapping_settings(self, json_body, **kwargs):
        """
        Update the LDAP group to Graylog role mapping
        Corresponds directly to the output of GET /system/ldap/settings/groups

        >>> thread = api.update_group_mapping_settings(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Map json_body: A hash in which the keys are the LDAP group names and values is the Graylog role name. (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_group_mapping_settings_with_http_info(json_body, **kwargs)
        else:
            (data) = self.update_group_mapping_settings_with_http_info(json_body, **kwargs)
            return data

    def update_group_mapping_settings_with_http_info(self, json_body, **kwargs):
        """
        Update the LDAP group to Graylog role mapping
        Corresponds directly to the output of GET /system/ldap/settings/groups

        >>> thread = api.update_group_mapping_settings_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Map json_body: A hash in which the keys are the LDAP group names and values is the Graylog role name. (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `json_body` when calling `update_group_mapping_settings`")

        resource_path = '/system/ldap/settings/groups'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

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


    def update_ldap_settings(self, json_body, **kwargs):
        """
        Update the LDAP configuration
        

        >>> thread = api.update_ldap_settings(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param LdapSettingsRequest json_body:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_ldap_settings_with_http_info(json_body, **kwargs)
        else:
            (data) = self.update_ldap_settings_with_http_info(json_body, **kwargs)
            return data

    def update_ldap_settings_with_http_info(self, json_body, **kwargs):
        """
        Update the LDAP configuration
        

        >>> thread = api.update_ldap_settings_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param LdapSettingsRequest json_body:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `json_body` when calling `update_ldap_settings`")

        resource_path = '/system/ldap/settings'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'json_body' in params:
            body_params = params['json_body']

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

