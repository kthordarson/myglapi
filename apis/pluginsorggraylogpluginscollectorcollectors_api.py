import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class PluginsorggraylogpluginscollectorcollectorsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get(self, collector_id, **kwargs):
        """
        Returns at most one collector summary for the specified collector id


        >>> thread = api.get(collector_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object collector_id:  (required)
        :return: CollectorSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(collector_id, **kwargs)
        else:
            (data) = self.get_with_http_info(collector_id, **kwargs)
            return data

    def get_with_http_info(self, collector_id, **kwargs):
        """
        Returns at most one collector summary for the specified collector id


        >>> thread = api.get_with_http_info(collector_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object collector_id:  (required)
        :return: CollectorSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['collector_id']
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
            raise ValueError("Missing the required parameter `collector_id` when calling `get`")

        resource_path = '/plugins/org.graylog.plugins.collector/collectors/{collectorId}'.replace('{format}', 'json')
        path_params = {}
        if 'collector_id' in params:
            path_params['collectorId'] = params['collector_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        Lists all existing collector registrations


        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: CollectorList If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        Lists all existing collector registrations


        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: CollectorList If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.collector/collectors'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='CollectorList', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def register(self, collector_id, json_body, **kwargs):
        """
        Create/update a collector registration
        This is a stateless method which upserts a collector registration

        >>> thread = api.register(collector_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object collector_id: The collector id this collector is registering as. (required)
        :param CollectorRegistrationRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.register_with_http_info(collector_id, json_body, **kwargs)
        else:
            (data) = self.register_with_http_info(collector_id, json_body, **kwargs)
            return data

    def register_with_http_info(self, collector_id, json_body, **kwargs):
        """
        Create/update a collector registration
        This is a stateless method which upserts a collector registration

        >>> thread = api.register_with_http_info(collector_id, json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object collector_id: The collector id this collector is registering as. (required)
        :param CollectorRegistrationRequest json_body:  (required)
        :return: None If the method is called asynchronously, returns the request thread.
        """

        all_params = ['collector_id', 'json_body']
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
            raise ValueError("Missing the required parameter `collector_id` when calling `register`")
        # verify the required parameter 'json_body' is set
        if ('json_body' not in params) or (params['json_body'] is None):
            raise ValueError("Missing the required parameter `json_body` when calling `register`")

        resource_path = '/plugins/org.graylog.plugins.collector/collectors/{collectorId}'.replace('{format}', 'json')
        path_params = {}
        if 'collector_id' in params:
            path_params['collectorId'] = params['collector_id']

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

