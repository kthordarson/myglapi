import sys
import os
import re
from myglapi.configuration import Configuration
from myglapi.api_client import ApiClient
from loguru import logger


class PluginsorggraylogpluginspipelineprocessorsystempipelinesconnectionsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def connect_pipelines(self, json_body, **kwargs):
        """
        Connect processing pipelines to a stream


        >>> thread = api.connect_pipelines(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param PipelineConnections json_body:  (required)
        :return: PipelineConnections If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.connect_pipelines_with_http_info(json_body, **kwargs)
        else:
            (data) = self.connect_pipelines_with_http_info(json_body, **kwargs)
            return data

    def connect_pipelines_with_http_info(self, json_body, **kwargs):
        """
        Connect processing pipelines to a stream


        >>> thread = api.connect_pipelines_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param PipelineConnections json_body:  (required)
        :return: PipelineConnections If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `json_body` when calling `connect_pipelines`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/connections'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='PipelineConnections', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_all(self, **kwargs):
        """
        Get all pipeline connections


        >>> thread = api.get_all(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Set If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_with_http_info(**kwargs)
        else:
            (data) = self.get_all_with_http_info(**kwargs)
            return data

    def get_all_with_http_info(self, **kwargs):
        """
        Get all pipeline connections


        >>> thread = api.get_all_with_http_info(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return: Set If the method is called asynchronously, returns the request thread.
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

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/connections'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='Set', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get_pipelines_for_stream(self, stream_id, **kwargs):
        """
        Get pipeline connections for the given stream


        >>> thread = api.get_pipelines_for_stream(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: PipelineConnections If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pipelines_for_stream_with_http_info(stream_id, **kwargs)
        else:
            (data) = self.get_pipelines_for_stream_with_http_info(stream_id, **kwargs)
            return data

    def get_pipelines_for_stream_with_http_info(self, stream_id, **kwargs):
        """
        Get pipeline connections for the given stream


        >>> thread = api.get_pipelines_for_stream_with_http_info(stream_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object stream_id:  (required)
        :return: PipelineConnections If the method is called asynchronously, returns the request thread.
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
            raise ValueError("Missing the required parameter `stream_id` when calling `get_pipelines_for_stream`")

        resource_path = '/plugins/org.graylog.plugins.pipelineprocessor/system/pipelines/connections/{streamId}'.replace('{format}', 'json')
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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='PipelineConnections', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
