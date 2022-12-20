import sys
import os
import re
from configuration import Configuration
from api_client import ApiClient
from loguru import logger


class SystemjobsApi(object):
    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cancel(self, job_id, **kwargs):
        """
        Cancel running job
        

        >>> thread = api.cancel(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_with_http_info(job_id, **kwargs)
        else:
            (data) = self.cancel_with_http_info(job_id, **kwargs)
            return data

    def cancel_with_http_info(self, job_id, **kwargs):
        """
        Cancel running job
        

        >>> thread = api.cancel_with_http_info(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `cancel`")

        resource_path = '/system/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

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

        return self.api_client.call_api(resource_path, 'DELETE', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SystemJobSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def get(self, job_id, **kwargs):
        """
        Get information of a specific currently running job
        

        >>> thread = api.get(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(job_id, **kwargs)
        else:
            (data) = self.get_with_http_info(job_id, **kwargs)
            return data

    def get_with_http_info(self, job_id, **kwargs):
        """
        Get information of a specific currently running job
        

        >>> thread = api.get_with_http_info(job_id, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param Object job_id:  (required)
        :return:\s SystemJobSummary If the method is called asynchronously, returns the request thread.
        """

        all_params = ['job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key in params['kwargs']:
            val = params['kwargs'][key]
            if key not in all_params:
                raise TypeError(f"Got an unexpected keyword argument {key}")
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get`")

        resource_path = '/system/jobs/{jobId}'.replace('{format}', 'json')
        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

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

        return self.api_client.call_api(resource_path, 'GET', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type='SystemJobSummary', auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        List currently running jobs
        

        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :return:\s Map If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        List currently running jobs
        

        >>> thread = api.list_with_http_info(callback=callback_function)

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

        resource_path = '/system/jobs'.replace('{format}', 'json')
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

    def trigger(self, json_body, **kwargs):
        """
        Trigger new job
        

        >>> thread = api.trigger(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param TriggerRequest json_body:  (required)
        :return:\s None If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.trigger_with_http_info(json_body, **kwargs)
        else:
            (data) = self.trigger_with_http_info(json_body, **kwargs)
            return data

    def trigger_with_http_info(self, json_body, **kwargs):
        """
        Trigger new job
        

        >>> thread = api.trigger_with_http_info(json_body, callback=callback_function)

        :param callback function: The callback function for asynchronous request. (optional)
        :param TriggerRequest json_body:  (required)
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
            raise ValueError("Missing the required parameter `json_body` when calling `trigger`")

        resource_path = '/system/jobs'.replace('{format}', 'json')
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
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST', path_params, query_params, header_params, body=body_params, post_params=form_params, files=local_var_files, response_type=None, auth_settings=auth_settings, callback=params.get('callback'), _return_http_data_only=params.get('_return_http_data_only'))
