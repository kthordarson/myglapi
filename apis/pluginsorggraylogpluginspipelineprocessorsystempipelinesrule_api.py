import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class PluginsorggraylogpluginspipelineprocessorsystempipelinesruleApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_from_parser(self, rule, **kwargs):
        """
        Create a processing rule from source


        >>> thread = api.create_from_parser(rule, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param RuleSource rule:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_from_parser_with_http_info(rule, **kwargs)
        else:
            (data) = self.create_from_parser_with_http_info(rule, **kwargs)
            return data

    def create_from_parser_with_http_info(self, rule, **kwargs):
        """
        Create a processing rule from source


        >>> thread = api.create_from_parser_with_http_info(rule, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param RuleSource rule:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rule']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rule' is set
        if ('rule' not in params) or (params['rule'] is None):
            raise ValueError("Missing the required parameter `rule` when calling `create_from_parser`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule' in params:
            body_params = params['rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RuleSource', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def delete(self, id, **kwargs):
        """
        Delete a processing rule
        It can take up to a second until the change is applied

        >>> thread = api.delete(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_with_http_info(id, **kwargs)
            return data

    def delete_with_http_info(self, id, **kwargs):
        """
        Delete a processing rule
        It can take up to a second until the change is applied

        >>> thread = api.delete_with_http_info(id, callback=callback_function)

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
            raise ValueError("Missing the required parameter `id` when calling `delete`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/{id}'.replace('{format}', 'json')
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

    def function_descriptors(self, **kwargs):
        """
        Get function descriptors


        >>> thread = api.function_descriptors(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Collection If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.function_descriptors_with_http_info(**kwargs)
        else:
            (data) = self.function_descriptors_with_http_info(**kwargs)
            return data

    def function_descriptors_with_http_info(self, **kwargs):
        """
        Get function descriptors


        >>> thread = api.function_descriptors_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Collection If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/functions'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Collection', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, id, **kwargs):
        """
        Get a processing rule
        It can take up to a second until the change is applied

        >>> thread = api.get(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(id, **kwargs)
        else:
            (data) = self.get_with_http_info(id, **kwargs)
            return data

    def get_with_http_info(self, id, **kwargs):
        """
        Get a processing rule
        It can take up to a second until the change is applied

        >>> thread = api.get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `id` when calling `get`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/{id}'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RuleSource', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_all(self, **kwargs):
        """
        Get all processing rules


        >>> thread = api.get_all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Collection If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_with_http_info(**kwargs)
        else:
            (data) = self.get_all_with_http_info(**kwargs)
            return data

    def get_all_with_http_info(self, **kwargs):
        """
        Get all processing rules


        >>> thread = api.get_all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Collection If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Collection', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_bulk(self, **kwargs):
        """
        Retrieve the named processing rules in bulk


        >>> thread = api.get_bulk(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param BulkRuleRequest : rules
        :return: Collection If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_bulk_with_http_info(**kwargs)
        else:
            (data) = self.get_bulk_with_http_info(**kwargs)
            return data

    def get_bulk_with_http_info(self, **kwargs):
        """
        Retrieve the named processing rules in bulk


        >>> thread = api.get_bulk_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param BulkRuleRequest : rules
        :return: Collection If the method is called asynchronously, returns the request thread.
        """

        all_params = ['']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/multiple'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if '' in params:
            body_params = params['']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Collection', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def parse(self, rule, **kwargs):
        """
        Parse a processing rule without saving it


        >>> thread = api.parse(rule, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param RuleSource rule:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.parse_with_http_info(rule, **kwargs)
        else:
            (data) = self.parse_with_http_info(rule, **kwargs)
            return data

    def parse_with_http_info(self, rule, **kwargs):
        """
        Parse a processing rule without saving it


        >>> thread = api.parse_with_http_info(rule, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param RuleSource rule:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """

        all_params = ['rule']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rule' is set
        if ('rule' not in params) or (params['rule'] is None):
            raise ValueError("Missing the required parameter `rule` when calling `parse`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/parse'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule' in params:
            body_params = params['rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RuleSource', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def update(self, id, rule, **kwargs):
        """
        Modify a processing rule
        It can take up to a second until the change is applied

        >>> thread = api.update(id, rule, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param RuleSource rule:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(id, rule, **kwargs)
        else:
            (data) = self.update_with_http_info(id, rule, **kwargs)
            return data

    def update_with_http_info(self, id, rule, **kwargs):
        """
        Modify a processing rule
        It can take up to a second until the change is applied

        >>> thread = api.update_with_http_info(id, rule, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object id:  (required)
        :param RuleSource rule:  (required)
        :return: RuleSource If the method is called asynchronously, returns the request thread.
        """

        all_params = ['id', 'rule']
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
            raise ValueError("Missing the required parameter `id` when calling `update`")
        # verify the required parameter 'rule' is set
        if ('rule' not in params) or (params['rule'] is None):
            raise ValueError("Missing the required parameter `rule` when calling `update`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/rule/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule' in params:
            body_params = params['rule']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='RuleSource', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
